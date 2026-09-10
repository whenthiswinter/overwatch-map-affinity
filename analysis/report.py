import csv
import json
import math
import os
from collections import defaultdict

from config import MAP_VALID_FROM_SEASON, MIN_PICK_RATE

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "csv")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "report", "analysis_report.md")


def load_raw():
    raw = {}
    for fname in os.listdir(RAW_DIR):
        if fname.endswith("_cache.json"):
            slug = fname.replace("_cache.json", "")
            with open(os.path.join(RAW_DIR, fname), encoding="utf-8") as f:
                raw[slug] = json.load(f)
    return raw


def analyze(raw):
    deltas = defaultdict(lambda: defaultdict(list))
    gm_deltas = defaultdict(lambda: defaultdict(list))
    master_deltas = defaultdict(lambda: defaultdict(list))
    pr_lifts = defaultdict(lambda: defaultdict(list))

    for slug, seasons in raw.items():
        for s in seasons:
            season, tier = s["season"], s["tier"]
            measurements = [m for m in s.get("measurements", []) if m.get("pickRate") is not None and m.get("winRate") is not None]
            total_pr = sum(m["pickRate"] for m in measurements)
            if total_pr == 0:
                continue
            baseline_wr = sum(m["winRate"] * m["pickRate"] for m in measurements) / total_pr
            baseline_pr = total_pr / len(measurements)

            for m in measurements:
                map_slug = m["map"]["slug"]
                if m["pickRate"] < MIN_PICK_RATE:
                    continue
                if season < MAP_VALID_FROM_SEASON.get(map_slug, 1):
                    continue

                delta = m["winRate"] - baseline_wr
                pr_lift = m["pickRate"] - baseline_pr

                deltas[slug][map_slug].append(delta)
                pr_lifts[slug][map_slug].append(pr_lift)

                if tier == "GRANDMASTER_AND_CHAMPION":
                    gm_deltas[slug][map_slug].append(delta)
                elif tier == "MASTER":
                    master_deltas[slug][map_slug].append(delta)

    return deltas, gm_deltas, master_deltas, pr_lifts


def volatility_of(deltas):
    result = {}
    for hero, maps in deltas.items():
        avgs = [sum(d) / len(d) for d in maps.values() if len(d) >= 3]
        if len(avgs) >= 5:
            mean = sum(avgs) / len(avgs)
            result[hero] = math.sqrt(sum((x - mean) ** 2 for x in avgs) / len(avgs))
    return result


def tier_of(delta):
    if delta >= 3.0:
        return "S"
    if delta >= 1.2:
        return "A"
    if delta >= -1.2:
        return "B"
    if delta >= -3.0:
        return "C"
    return "D"


def presence_of(pr_lift):
    if pr_lift >= 3.0:
        return f"Map Priority (+{pr_lift:.1f}%)"
    if pr_lift >= 1.0:
        return f"Popular (+{pr_lift:.1f}%)"
    if pr_lift >= -1.0:
        return f"Standard ({pr_lift:+.1f}%)"
    return f"Niche ({pr_lift:.1f}%)"


def archetype_of(delta_wr, delta_pr):
    if delta_wr >= 1.5 and delta_pr >= 1.5:
        return "Meta"
    if delta_wr >= 1.5 and delta_pr < 0.0:
        return "Specialist"
    if delta_wr <= -1.5 and delta_pr >= 1.0:
        return "Trap Pick"
    if delta_wr <= -1.5 and delta_pr < 0.0:
        return "Deterrent"
    if delta_wr >= 1.2:
        return "Favorable"
    if delta_wr <= -1.2:
        return "Unfavorable"
    return "Neutral"


def rank_comparison(gm_vals, master_vals):
    if len(gm_vals) >= 2 and len(master_vals) >= 2:
        avg_gm = sum(gm_vals) / len(gm_vals)
        avg_m = sum(master_vals) / len(master_vals)
        diff = avg_gm - avg_m
        if diff >= 2.5:
            return "Better in GM+", diff, avg_m, avg_gm
        if diff <= -2.5:
            return "Better in Masters", diff, avg_m, avg_gm
        return "Even Across Ranks", diff, avg_m, avg_gm
    return "Even Across Ranks", 0.0, None, None


def run():
    os.makedirs(CSV_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

    raw = load_raw()
    deltas, gm_deltas, master_deltas, pr_lifts = analyze(raw)
    volatility = volatility_of(deltas)
    sorted_vol = sorted(volatility.items(), key=lambda x: x[1], reverse=True)

    csv_rows = []

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# Overwatch Map Affinity Report\n\n")
        f.write("Timeless per-hero, per-map win rate deltas, computed relative to each hero's baseline win rate in the same rank/region/patch slice, then averaged across every slice collected.\n\n")

        f.write("## Contents\n")
        f.write("1. [Map Sensitivity (Volatility)](#1-map-sensitivity-volatility)\n")
        f.write("2. [Rank Divergence](#2-rank-divergence)\n")
        f.write("3. [Map Tier Lists](#3-map-tier-lists)\n\n")

        f.write("## 1. Map Sensitivity (Volatility)\n\n")
        f.write("Standard deviation of a hero's average delta across all maps. High sigma means a hero swings hard between best and worst maps; low sigma means they're roughly the same everywhere.\n\n")
        f.write("| Hero | Sigma | Class |\n|---|---|---|\n")
        for hero, sigma in sorted_vol:
            cls = "Map-Dependent" if sigma >= 3.0 else "Flexible" if sigma >= 1.8 else "Map-Agnostic"
            f.write(f"| {hero.title()} | {sigma:.2f}% | {cls} |\n")
        f.write("\n---\n\n")

        f.write("## 2. Rank Divergence\n\n")
        f.write("Heroes whose map performance differs by 2.5% or more between Masters and GM+.\n\n")
        f.write("| Hero | Map | Masters | GM+ | Diff | Better In |\n|---|---|---|---|---|---|\n")

        divergence_rows = []
        for hero, maps in deltas.items():
            for map_slug in maps:
                comp, diff, avg_m, avg_gm = rank_comparison(gm_deltas[hero].get(map_slug, []), master_deltas[hero].get(map_slug, []))
                if comp != "Even Across Ranks":
                    divergence_rows.append((hero, map_slug, avg_m, avg_gm, diff, comp))
        divergence_rows.sort(key=lambda r: abs(r[4]), reverse=True)

        for hero, map_slug, avg_m, avg_gm, diff, comp in divergence_rows:
            f.write(f"| {hero.title()} | {map_slug} | {avg_m:+.2f}% | {avg_gm:+.2f}% | {diff:+.2f}% | {comp} |\n")
        f.write("\n---\n\n")

        f.write("## 3. Map Tier Lists\n\n")
        all_maps = sorted({m for maps in deltas.values() for m in maps})

        for map_slug in all_maps:
            f.write(f"### {map_slug.replace('-', ' ').title()}\n\n")
            f.write("| Tier | Hero | Delta WR | Presence | Archetype | Rank | n |\n|---|---|---|---|---|---|---|\n")

            entries = []
            for hero, maps in deltas.items():
                if map_slug not in maps:
                    continue
                d_list = maps[map_slug]
                avg_delta = sum(d_list) / len(d_list)
                avg_pr = sum(pr_lifts[hero][map_slug]) / len(pr_lifts[hero][map_slug])
                comp, _, _, _ = rank_comparison(gm_deltas[hero].get(map_slug, []), master_deltas[hero].get(map_slug, []))
                tier = tier_of(avg_delta)
                presence = presence_of(avg_pr)
                archetype = archetype_of(avg_delta, avg_pr)

                entries.append((tier, hero, avg_delta, avg_pr, presence, archetype, comp, len(d_list)))
                csv_rows.append({
                    "map": map_slug, "tier": tier, "hero": hero,
                    "delta_wr": round(avg_delta, 2), "delta_pr": round(avg_pr, 2),
                    "presence": presence, "archetype": archetype,
                    "rank_comparison": comp, "sample_size": len(d_list),
                })

            order = {"S": 0, "A": 1, "B": 2, "C": 3, "D": 4}
            entries.sort(key=lambda e: (order[e[0]], -e[2]))

            for tier, hero, delta, pr_l, presence, archetype, comp, n in entries:
                rank_str = comp if comp != "Even Across Ranks" else "-"
                f.write(f"| {tier} | {hero.title()} | {delta:+.2f}% | {presence} | {archetype} | {rank_str} | {n} |\n")
            f.write("\n")

    with open(os.path.join(CSV_DIR, "map_tierlists.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["map", "tier", "hero", "delta_wr", "delta_pr", "presence", "archetype", "rank_comparison", "sample_size"])
        writer.writeheader()
        writer.writerows(csv_rows)

    with open(os.path.join(CSV_DIR, "hero_volatility.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["hero", "volatility_sigma", "classification"])
        for hero, sigma in sorted_vol:
            cls = "Map-Dependent" if sigma >= 3.0 else "Flexible" if sigma >= 1.8 else "Map-Agnostic"
            writer.writerow([hero, round(sigma, 2), cls])

    print(f"wrote {REPORT_PATH}")
    print(f"wrote {CSV_DIR}/map_tierlists.csv and hero_volatility.csv")


if __name__ == "__main__":
    run()

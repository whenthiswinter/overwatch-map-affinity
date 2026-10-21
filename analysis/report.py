"""Markdown report and CSVs from the same numbers the site shows.

Reuses build_dataset.build_scope (all seasons, all ranks/regions), so tiers,
noise adjustment and map sensitivity can't drift from the dashboard.
"""
import csv
import os

import sources
from build_dataset import build_scope
from check_rank_region import run_checks
from config import hero_name, map_name, season_usable

CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "csv")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "report", "analysis_report.md")

TIER_ORDER = {"S": 0, "A": 1, "B": 2, "C": 3, "D": 4}


def short_class(volatility_class):
    return volatility_class.split(" (")[0]


def run():
    os.makedirs(CSV_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

    combos = build_scope(sources.load_all(), season_usable, flag_provisional=True)
    overall = combos["ALL_ALL"]
    rank_region = run_checks()
    heroes = sorted(overall["heroes"].items(), key=lambda kv: kv[1]["volatility"], reverse=True)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# Overwatch Map Affinity Report\n\n")
        f.write("Timeless per-hero, per-map win rate deltas, computed relative to each hero's baseline win rate in the same rank/region/patch slice, then averaged across every slice collected. "
                "Each average is then adjusted for noise: pulled toward the hero's mean in proportion to how much its slices disagree, so thin or inconsistent numbers don't land in extreme tiers by chance. "
                "The raw average and its 95% range are listed next to it.\n\n")

        f.write("## Contents\n")
        f.write("1. [Map Sensitivity (Volatility)](#1-map-sensitivity-volatility)\n")
        f.write("2. [Rank and Region](#2-rank-and-region)\n")
        f.write("3. [Map Tier Lists](#3-map-tier-lists)\n\n")

        f.write("## 1. Map Sensitivity (Volatility)\n\n")
        f.write("How much a hero's win rate really varies from map to map: the standard deviation of their map averages, minus the part explained by sampling noise. "
                "Map-Agnostic below 1.2 (most maps stay within the B band), Map-Dependent from 3.0 (a third or more of maps reach S or D).\n\n")
        f.write("| Hero | Sigma | Class |\n|---|---|---|\n")
        for hero, h in heroes:
            sigma = "-" if h["volatility_class"].startswith("Too early") else f"{h['volatility']:.2f}%"
            f.write(f"| {hero_name(hero)} | {sigma} | {short_class(h['volatility_class'])} |\n")
        f.write("\n---\n\n")

        f.write("## 2. Rank and Region\n\n")
        f.write("Does a hero's map affinity differ between Masters and GM+, or between regions? Each hero-map pair's slices are split into two independent halves "
                "(season first halves vs midseasons) and the gap is measured in each. A real difference would repeat between the halves; noise wouldn't. "
                "A difference counts only if the halves correlate with one-sided p < 0.05 over all pairs (region tests share it: 0.0125 each). "
                "This rule was fixed on 2026-10-21 and is rerun every season (`analysis/check_rank_region.py`).\n\n")
        f.write("| Comparison | Split-half correlation | Pairs | p | Detected |\n|---|---|---|---|---|\n")
        for res in rank_region:
            f.write(f"| {res['test']} | {res['r']:+.3f} | {res['pairs']} | {res['p']:.4f} | {'yes' if res['real'] else 'no'} |\n")
        f.write("\nAs of the 2026-10-21 analysis (the table above is recomputed on every run): the rank groups show no detectable difference. Europe shows a small consistent one (a typical hero-map gap of about 1 point), "
                "but even for European numbers the all-regions estimate predicts held-out data better than Europe alone, because a quarter of the data adds more noise "
                "than the regional difference is worth. The same holds for GM+. So the all-ranks, all-regions view is the most reliable one for everyone.\n\n---\n\n")

        f.write("## 3. Map Tier Lists\n\n")
        by_map = {}
        for e in overall["entries"]:
            by_map.setdefault(e["map"], []).append(e)

        for map_slug in sorted(by_map):
            f.write(f"### {map_name(map_slug)}\n\n")
            f.write("| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |\n|---|---|---|---|---|---|---|---|\n")
            for e in sorted(by_map[map_slug], key=lambda e: (TIER_ORDER[e["tier"]], -e["delta_wr"])):
                name = hero_name(e["hero"]) + (" *(provisional)*" if e["provisional"] else "")
                f.write(f"| {e['tier']} | {e['tier_p']}% | {name} | {e['delta_wr']:+.2f}% | {e['raw_delta_wr']:+.2f}% ±{e['ci']:.1f} | "
                        f"{e['presence']} | {e['archetype']} | {e['sample_size']} |\n")
            f.write("\n")

    fields = ["map", "tier", "hero", "delta_wr", "pr_lift_pct", "presence", "archetype",
              "sample_size", "raw_delta_wr", "ci95", "tier_probability_pct", "provisional"]
    with open(os.path.join(CSV_DIR, "map_tierlists.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for e in sorted(overall["entries"], key=lambda e: (e["map"], TIER_ORDER[e["tier"]], -e["delta_wr"])):
            writer.writerow({
                "map": e["map"], "tier": e["tier"], "hero": e["hero"],
                "delta_wr": e["delta_wr"], "pr_lift_pct": e["pr_lift"],
                "presence": e["presence"], "archetype": e["archetype"],
                "sample_size": e["sample_size"], "raw_delta_wr": e["raw_delta_wr"], "ci95": e["ci"], "tier_probability_pct": e["tier_p"],
                "provisional": e["provisional"],
            })

    with open(os.path.join(CSV_DIR, "hero_volatility.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["hero", "volatility_sigma", "classification"])
        for hero, h in heroes:
            writer.writerow([hero, h["volatility"], short_class(h["volatility_class"])])

    print(f"wrote {REPORT_PATH}")
    print(f"wrote {CSV_DIR}/map_tierlists.csv and hero_volatility.csv")


if __name__ == "__main__":
    run()

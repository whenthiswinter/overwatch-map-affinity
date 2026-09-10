import json
import math
import os
from collections import defaultdict

from config import HERO_RELEASE_SEASON, MAP_MODES, MAP_VALID_FROM_SEASON, MIN_PICK_RATE, hero_role

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "web_data.json")

RANKS = ["ALL", "MASTER", "GRANDMASTER_AND_CHAMPION"]
REGIONS = ["ALL", "AMER", "EU", "ASIA", "KR"]


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


def presence_label(pr_lift):
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


def load_raw():
    raw = {}
    for fname in os.listdir(RAW_DIR):
        if fname.endswith("_cache.json"):
            slug = fname.replace("_cache.json", "")
            with open(os.path.join(RAW_DIR, fname), encoding="utf-8") as f:
                raw[slug] = json.load(f)
    return raw


def flatten(raw):
    slices = defaultdict(list)
    rank_slices = defaultdict(lambda: defaultdict(lambda: {"MASTER": [], "GM": []}))

    for hero_slug, seasons in raw.items():
        earliest = HERO_RELEASE_SEASON.get(hero_slug.title(), 1)
        role = hero_role(hero_slug)

        for s in seasons:
            season = s["season"]
            if season < earliest:
                continue

            tier = s["tier"]
            region = s["region"]
            measurements = [m for m in s.get("measurements", []) if m.get("pickRate") is not None and m.get("winRate") is not None]
            total_pr = sum(m["pickRate"] for m in measurements)
            if total_pr == 0:
                continue

            baseline_wr = sum(m["winRate"] * m["pickRate"] for m in measurements) / total_pr
            baseline_pr = total_pr / len(measurements)

            for m in measurements:
                map_slug = m["map"]["slug"]
                if season < MAP_VALID_FROM_SEASON.get(map_slug, 1):
                    continue
                if m["pickRate"] < MIN_PICK_RATE:
                    continue

                d_wr = m["winRate"] - baseline_wr
                d_pr = m["pickRate"] - baseline_pr

                slices[hero_slug].append({
                    "season": season, "tier": tier, "region": region,
                    "map_slug": map_slug, "role": role,
                    "delta_wr": d_wr, "delta_pr": d_pr,
                })

                if tier == "MASTER":
                    rank_slices[hero_slug][map_slug]["MASTER"].append(d_wr)
                elif tier == "GRANDMASTER_AND_CHAMPION":
                    rank_slices[hero_slug][map_slug]["GM"].append(d_wr)

    return slices, rank_slices


def rank_divergence(rank_slices):
    divergence = defaultdict(dict)
    for hero_slug, maps in rank_slices.items():
        for map_slug, ranks in maps.items():
            m_vals, gm_vals = ranks["MASTER"], ranks["GM"]
            if len(m_vals) >= 2 and len(gm_vals) >= 2:
                diff = (sum(gm_vals) / len(gm_vals)) - (sum(m_vals) / len(m_vals))
                if diff >= 2.5:
                    divergence[hero_slug][map_slug] = "Better in GM+"
                elif diff <= -2.5:
                    divergence[hero_slug][map_slug] = "Better in Masters"
                else:
                    divergence[hero_slug][map_slug] = "Even Across Ranks"
            else:
                divergence[hero_slug][map_slug] = "Even Across Ranks"
    return divergence


def build():
    raw = load_raw()
    slices, rank_slices = flatten(raw)
    divergence = rank_divergence(rank_slices)

    database = {}
    for rank_filter in RANKS:
        for region_filter in REGIONS:
            combo = f"{rank_filter}_{region_filter}"
            hero_map_wr = defaultdict(lambda: defaultdict(list))
            hero_map_pr = defaultdict(lambda: defaultdict(list))

            for hero_slug, items in slices.items():
                for item in items:
                    if rank_filter != "ALL" and item["tier"] != rank_filter:
                        continue
                    if region_filter != "ALL" and item["region"] != region_filter:
                        continue
                    hero_map_wr[hero_slug][item["map_slug"]].append(item["delta_wr"])
                    hero_map_pr[hero_slug][item["map_slug"]].append(item["delta_pr"])

            maps_aggregate = defaultdict(list)
            heroes_aggregate = {}

            for hero_slug, maps in hero_map_wr.items():
                role = hero_role(hero_slug)
                mode_deltas = defaultdict(list)
                entries = []

                for map_slug, deltas in maps.items():
                    if not deltas:
                        continue
                    avg_wr = sum(deltas) / len(deltas)
                    avg_pr = sum(hero_map_pr[hero_slug][map_slug]) / len(hero_map_pr[hero_slug][map_slug])
                    mode = MAP_MODES.get(map_slug, "Other")
                    mode_deltas[mode].append(avg_wr)

                    entry = {
                        "hero": hero_slug, "role": role, "map": map_slug, "mode": mode,
                        "delta_wr": round(avg_wr, 2), "delta_pr": round(avg_pr, 2),
                        "tier": tier_of(avg_wr), "presence": presence_label(avg_pr),
                        "archetype": archetype_of(avg_wr, avg_pr),
                        "rank_skew": divergence[hero_slug].get(map_slug, "Even Across Ranks"),
                        "sample_size": len(deltas),
                    }
                    maps_aggregate[map_slug].append(entry)
                    entries.append(entry)

                hero_modes = {m: round(sum(d) / len(d), 2) for m, d in mode_deltas.items() if d}

                all_d = [e["delta_wr"] for e in entries]
                sigma = 0.0
                if len(all_d) >= 5:
                    mean = sum(all_d) / len(all_d)
                    sigma = round(math.sqrt(sum((x - mean) ** 2 for x in all_d) / len(all_d)), 2)

                vol_class = (
                    "Map-Dependent (σ ≥ 3.0%)" if sigma >= 3.0
                    else "Flexible (1.8% ≤ σ < 3.0%)" if sigma >= 1.8
                    else "Map-Agnostic (σ < 1.8%)"
                )

                heroes_aggregate[hero_slug] = {
                    "role": role, "modes": hero_modes,
                    "volatility": sigma, "volatility_class": vol_class,
                    "maps": entries,
                }

            database[combo] = {"maps": maps_aggregate, "heroes": heroes_aggregate}

    payload = {
        "database": database,
        "map_list": sorted(MAP_MODES.keys()),
        "hero_list": sorted(raw.keys()),
        "hero_roles": {h: hero_role(h) for h in raw.keys()},
        "map_modes": MAP_MODES,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f)

    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    build()

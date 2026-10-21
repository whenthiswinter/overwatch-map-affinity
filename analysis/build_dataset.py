import datetime
import json
import math
import os
from collections import defaultdict

import sources
from config import (
    CURRENT_IS_MIDSEASON, CURRENT_PATCH, CURRENT_PATCH_MATURE, CURRENT_SEASON, DATA_THROUGH,
    DAYS_INTO_PATCH, HERO_VALID_FROM_SEASON, MAP_MODES, MATURITY_DAYS, MIN_PICK_RATE, MIN_SAMPLE_SIZE,
    hero_name, hero_role, in_current_patch, is_provisional, period, season_usable,
)

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "web_data.json")

RANKS = ["ALL", "MASTER", "GRANDMASTER_AND_CHAMPION"]
REGIONS = ["ALL", "AMER", "EU", "ASIA", "KR"]

# OWTics reports Korea as "KOREA" in the raw payload, but the site uses the
# shorter "KR" everywhere else. Map the site-facing filter back to the raw
# region code when matching against harvested data.
REGION_CODE = {"KR": "KOREA"}


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



def flatten(raw, usable):
    """Per-hero list of qualifying (hero, map) slice deltas. `usable(hero, map,
    season, is_midseason)` decides which slices count for the scope."""
    slices = defaultdict(list)
    rank_slices = defaultdict(lambda: defaultdict(lambda: {"MASTER": [], "GM": []}))
    raw_slice_counts = defaultdict(list)

    for hero_slug, seasons in raw.items():
        earliest = HERO_VALID_FROM_SEASON.get(hero_slug, 1)
        role = hero_role(hero_slug)

        for s in seasons:
            season = s["season"]
            is_mid = s.get("isMidseason", False)
            if period(season, is_mid) < earliest:
                continue

            tier = s["tier"]
            region = s["region"]
            measurements = [m for m in s.get("measurements", []) if m.get("pickRate") is not None and m.get("winRate") is not None]
            total_pr = sum(m["pickRate"] for m in measurements)
            if total_pr == 0:
                continue

            raw_slice_counts[hero_slug].append((season, is_mid, tier, region))

            baseline_wr = sum(m["winRate"] * m["pickRate"] for m in measurements) / total_pr
            baseline_pr = total_pr / len(measurements)

            for m in measurements:
                map_slug = m["map"]["slug"]
                if not usable(hero_slug, map_slug, season, is_mid):
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

    return slices, rank_slices, raw_slice_counts


def max_possible_slices(raw_slice_counts, usable, hero_slug, map_slug, rank_filter, region_filter):
    """How many raw slices could this hero-map pair ever have under this
    rank/region filter, given which seasons count for the pair.
    A brand-new hero or a recently-reworked map will always fall short of
    MIN_SAMPLE_SIZE once you narrow to one rank or region - this is the
    ceiling we compare against instead of a flat minimum in that case."""
    region_code = REGION_CODE.get(region_filter, region_filter)

    count = 0
    for season, is_mid, tier, region in raw_slice_counts.get(hero_slug, []):
        if not usable(hero_slug, map_slug, season, is_mid):
            continue
        if rank_filter != "ALL" and tier != rank_filter:
            continue
        if region_filter != "ALL" and region != region_code:
            continue
        count += 1
    return count


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


def ci95(values):
    """Rough 95% range of a pair's average delta, from how much its slices
    disagree. Slices of one season are correlated, so treat it as a lower bound."""
    if len(values) < 2:
        return None
    mean = sum(values) / len(values)
    sd = math.sqrt(sum((v - mean) ** 2 for v in values) / (len(values) - 1))
    return round(1.96 * sd / math.sqrt(len(values)), 2)


def build_scope(raw, usable, flag_provisional):
    """Every rank x region combo for one scope. Each hero-map entry is stored
    once; the site rebuilds the per-map and per-hero indexes on load."""
    slices, rank_slices, raw_slice_counts = flatten(raw, usable)
    divergence = rank_divergence(rank_slices)

    combos = {}
    for rank_filter in RANKS:
        for region_filter in REGIONS:
            region_code = REGION_CODE.get(region_filter, region_filter)
            hero_map_wr = defaultdict(lambda: defaultdict(list))
            hero_map_pr = defaultdict(lambda: defaultdict(list))

            for hero_slug, items in slices.items():
                for item in items:
                    if rank_filter != "ALL" and item["tier"] != rank_filter:
                        continue
                    if region_filter != "ALL" and item["region"] != region_code:
                        continue
                    hero_map_wr[hero_slug][item["map_slug"]].append(item["delta_wr"])
                    hero_map_pr[hero_slug][item["map_slug"]].append(item["delta_pr"])

            entries = []
            heroes = {}

            for hero_slug, maps in hero_map_wr.items():
                mode_deltas = defaultdict(list)
                hero_entries = []

                for map_slug, deltas in maps.items():
                    possible = max_possible_slices(raw_slice_counts, usable, hero_slug, map_slug, rank_filter, region_filter)
                    if len(deltas) < min(MIN_SAMPLE_SIZE, possible):
                        continue
                    avg_wr = sum(deltas) / len(deltas)
                    avg_pr = sum(hero_map_pr[hero_slug][map_slug]) / len(hero_map_pr[hero_slug][map_slug])
                    mode_deltas[MAP_MODES.get(map_slug, "Other")].append(avg_wr)

                    hero_entries.append({
                        "hero": hero_slug, "map": map_slug,
                        "delta_wr": round(avg_wr, 2), "delta_pr": round(avg_pr, 2),
                        "tier": tier_of(avg_wr), "presence": presence_label(avg_pr),
                        "archetype": archetype_of(avg_wr, avg_pr),
                        "rank_skew": divergence[hero_slug].get(map_slug, "Even Across Ranks"),
                        "sample_size": len(deltas),
                        "ci": ci95(deltas),
                        "provisional": flag_provisional and is_provisional(hero_slug, map_slug),
                    })

                hero_modes = {m: round(sum(d) / len(d), 2) for m, d in mode_deltas.items() if d}

                all_d = [e["delta_wr"] for e in hero_entries]
                sigma = 0.0
                if len(all_d) >= 5:
                    mean = sum(all_d) / len(all_d)
                    sigma = round(math.sqrt(sum((x - mean) ** 2 for x in all_d) / len(all_d)), 2)

                vol_class = (
                    "Map-Dependent (σ ≥ 3.0%)" if sigma >= 3.0
                    else "Flexible (1.8% ≤ σ < 3.0%)" if sigma >= 1.8
                    else "Map-Agnostic (σ < 1.8%)"
                )

                heroes[hero_slug] = {
                    "modes": hero_modes,
                    "volatility": sigma, "volatility_class": vol_class,
                    "provisional": bool(hero_entries) and all(e["provisional"] for e in hero_entries),
                }
                entries.extend(hero_entries)

            combos[f"{rank_filter}_{region_filter}"] = {"entries": entries, "heroes": heroes}
    return combos


def build():
    raw = sources.load_all()

    payload = {
        "meta": {
            "data_through": DATA_THROUGH,
            "built_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="minutes"),
            "patch": CURRENT_PATCH["id"],
            "season": CURRENT_SEASON,
            "is_midseason": CURRENT_IS_MIDSEASON,
            "patch_started": CURRENT_PATCH["started"],
            "days_into_patch": DAYS_INTO_PATCH,
            "maturity_days": MATURITY_DAYS,
            "mature": CURRENT_PATCH_MATURE,
        },
        "scopes": {
            "all": build_scope(raw, season_usable, flag_provisional=True),
            "patch": build_scope(raw, in_current_patch, flag_provisional=False),
        },
        "map_list": sorted(MAP_MODES.keys()),
        "hero_list": sorted(raw.keys()),
        "hero_roles": {h: hero_role(h) for h in raw.keys()},
        "hero_names": {h: hero_name(h) for h in raw.keys()},
        "map_modes": MAP_MODES,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))

    print(f"wrote {OUT_PATH} ({os.path.getsize(OUT_PATH) // 1024} KB)")


if __name__ == "__main__":
    build()

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


# Tier lines on the (noise-adjusted) win rate delta, in points. They sit at
# ~0.6x / 1.4x the game-wide spread of real map effects (2.1) and were checked
# against split-half reproducibility on 2026-10-21 (PLAN.md phase 5 item 4).
TIER_INNER, TIER_OUTER = 1.2, 3.0

# Presence lines on the relative pick-rate lift (map pick rate vs the hero's
# average, in %), placed by the same rule: ~0.6x / 1.4x its spread (33%).
PRESENCE_INNER, PRESENCE_OUTER = 20.0, 50.0


def tier_of(delta):
    if delta >= TIER_OUTER:
        return "S"
    if delta >= TIER_INNER:
        return "A"
    if delta >= -TIER_INNER:
        return "B"
    if delta >= -TIER_OUTER:
        return "C"
    return "D"


def presence_label(pr_lift):
    if pr_lift >= PRESENCE_OUTER:
        return f"Map Priority ({pr_lift:+.0f}%)"
    if pr_lift >= PRESENCE_INNER:
        return f"Popular ({pr_lift:+.0f}%)"
    if pr_lift > -PRESENCE_INNER:
        return f"Standard ({pr_lift:+.0f}%)"
    return f"Niche ({pr_lift:+.0f}%)"


def archetype_of(delta_wr, pr_lift):
    """Win side from the tier lines (A or better / B / C or worse), pick side
    from the presence lines (Popular or more / Standard / Niche)."""
    tier = tier_of(delta_wr)
    picked_more, picked_less = pr_lift >= PRESENCE_INNER, pr_lift <= -PRESENCE_INNER
    if tier in "SA":
        return "Meta" if picked_more else "Specialist" if picked_less else "Favorable"
    if tier in "CD":
        return "Trap Pick" if picked_more else "Deterrent" if picked_less else "Unfavorable"
    return "Neutral"



def flatten(raw, usable):
    """Per-hero list of qualifying (hero, map) slice deltas. `usable(hero, map,
    season, is_midseason)` decides which slices count for the scope."""
    slices = defaultdict(list)
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
                # Relative, so heroes with very different overall pick rates compare fairly.
                pr_lift = (m["pickRate"] / baseline_pr - 1) * 100

                slices[hero_slug].append({
                    "season": season, "is_midseason": is_mid, "tier": tier, "region": region,
                    "map_slug": map_slug, "role": role,
                    "delta_wr": d_wr, "pr_lift": pr_lift,
                })

    return slices, raw_slice_counts


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


# --- Noise model -------------------------------------------------------------
# A hero-map number is the average of a few slices that disagree with each
# other, so part of every number is noise. Per hero (within one rank/region
# combo):
#   - each pair's slice variance is pulled toward the hero's pooled variance
#     (POOL_WEIGHT pseudo-slices), so thin pairs borrow from the hero's others;
#     its noise is se^2 = variance / n;
#   - the hero's real map sensitivity is tau^2 = observed variance of its map
#     averages minus the average se^2 (the "noise-corrected sigma");
#   - each pair is shrunk toward the hero's mean by tau^2 / (tau^2 + se^2):
#     well-measured pairs barely move, noisy ones move a lot.
# Heroes without established (non-provisional) history can't estimate tau
# from two weeks of data, so they borrow the combo's typical tau^2.
POOL_WEIGHT = 4
MIN_PAIRS_FOR_TAU = 5


def mean_of(values):
    return sum(values) / len(values)


def variance_of(values):
    m = mean_of(values)
    return sum((v - m) ** 2 for v in values) / (len(values) - 1)


def pooled_variance(pair_deltas):
    """Within-pair variance pooled over a hero's pairs, or None if too thin."""
    dof = sum(len(d) - 1 for d in pair_deltas)
    if dof < 5:
        return None
    return sum(variance_of(d) * (len(d) - 1) for d in pair_deltas if len(d) > 1) / dof


def pair_noise(deltas, pooled):
    """se^2 of a pair's average, its variance pulled toward the hero's pooled one."""
    n = len(deltas)
    var = ((n - 1) * variance_of(deltas) + POOL_WEIGHT * pooled) / (n - 1 + POOL_WEIGHT) if n > 1 else pooled
    return var / n


def signal_variance(means, noises):
    """Real spread of a hero's map effects: observed variance minus noise."""
    mu = mean_of(means)
    observed = sum((m - mu) ** 2 for m in means) / len(means)
    return max(observed - mean_of(noises), 0.0)


# For the confidence figure only (never the estimate itself): never treat a
# hero's real map effect as exactly zero, or "no detected effect" turns into
# "100% certain B". 2.0 calibrated best on 2026-10-21: forecasts of held-out
# tiers were off by 1.9 points on average (4.2 without a floor).
CONFIDENCE_TAU2_FLOOR = 2.0


def normal_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def tier_probability(adjusted, se2, tau2):
    """Chance the true value lies in the shown tier, from the noise model."""
    t2 = max(tau2, CONFIDENCE_TAU2_FLOOR)
    sd = math.sqrt(t2 * se2 / (t2 + se2))
    edges = [-math.inf, -TIER_OUTER, -TIER_INNER, TIER_INNER, TIER_OUTER, math.inf]
    i = "DCBAS".index(tier_of(adjusted))
    return normal_cdf((edges[i + 1] - adjusted) / sd) - normal_cdf((edges[i] - adjusted) / sd)


def volatility_class(sigma, provisional):
    if provisional:
        return "Too early to tell (new or reworked)"
    if sigma >= 3.0:
        return "Map-Dependent (σ ≥ 3.0%)"
    if sigma >= 1.2:
        return "Flexible (1.2% ≤ σ < 3.0%)"
    return "Map-Agnostic (σ < 1.2%)"


def build_scope(raw, usable, flag_provisional):
    """Every rank x region combo for one scope. Each hero-map entry is stored
    once; the site rebuilds the per-map and per-hero indexes on load."""
    slices, raw_slice_counts = flatten(raw, usable)

    # Fallback noise levels from all ranks/regions together, for combos too
    # narrow to measure their own (e.g. one patch, one rank, one region = 1 slice).
    scope_pairs = {}
    for hero_slug, items in slices.items():
        by_map = defaultdict(list)
        for item in items:
            by_map[item["map_slug"]].append(item["delta_wr"])
        scope_pairs[hero_slug] = list(by_map.values())
    scope_pooled = {h: pooled_variance(p) for h, p in scope_pairs.items()}
    scope_pooled_all = pooled_variance([d for p in scope_pairs.values() for d in p]) or 0.0

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
                    hero_map_pr[hero_slug][item["map_slug"]].append(item["pr_lift"])

            # Pairs that pass the sample-size rule, per hero.
            eligible = {}
            for hero_slug, maps in hero_map_wr.items():
                kept = {}
                for map_slug, deltas in maps.items():
                    possible = max_possible_slices(raw_slice_counts, usable, hero_slug, map_slug, rank_filter, region_filter)
                    if len(deltas) >= min(MIN_SAMPLE_SIZE, possible):
                        kept[map_slug] = deltas
                if kept:
                    eligible[hero_slug] = kept

            # Noise per pair, and each hero's real map sensitivity (tau^2).
            noise, tau2 = {}, {}
            for hero_slug, kept in eligible.items():
                pooled = pooled_variance(list(kept.values())) or scope_pooled.get(hero_slug) or scope_pooled_all
                noise[hero_slug] = {m: pair_noise(d, pooled) for m, d in kept.items()}
                established = [m for m in kept if not is_provisional(hero_slug, m)]
                if len(established) >= MIN_PAIRS_FOR_TAU:
                    tau2[hero_slug] = signal_variance([mean_of(kept[m]) for m in established], [noise[hero_slug][m] for m in established])
            typical_tau2 = mean_of(list(tau2.values())) if tau2 else 0.0

            entries = []
            heroes = {}

            for hero_slug, kept in eligible.items():
                hero_tau2 = tau2.get(hero_slug, typical_tau2)
                hero_mean = mean_of([mean_of(d) for d in kept.values()])
                mode_deltas = defaultdict(list)
                hero_entries = []

                for map_slug, deltas in kept.items():
                    raw_wr = mean_of(deltas)
                    se2 = noise[hero_slug][map_slug]
                    weight = hero_tau2 / (hero_tau2 + se2) if hero_tau2 + se2 > 0 else 0.0
                    adj_wr = hero_mean + weight * (raw_wr - hero_mean)
                    pr_lift = mean_of(hero_map_pr[hero_slug][map_slug])
                    mode_deltas[MAP_MODES.get(map_slug, "Other")].append(adj_wr)

                    hero_entries.append({
                        "hero": hero_slug, "map": map_slug,
                        "delta_wr": round(adj_wr, 2), "raw_delta_wr": round(raw_wr, 2),
                        "pr_lift": round(pr_lift, 1),
                        "tier": tier_of(adj_wr), "presence": presence_label(pr_lift),
                        "archetype": archetype_of(adj_wr, pr_lift),
                        "sample_size": len(deltas),
                        "ci": round(1.96 * math.sqrt(se2), 2),
                        "tier_p": round(100 * tier_probability(adj_wr, se2, hero_tau2)),
                        "provisional": flag_provisional and is_provisional(hero_slug, map_slug),
                    })

                hero_modes = {m: round(mean_of(d), 2) for m, d in mode_deltas.items() if d}
                hero_provisional = hero_slug not in tau2
                sigma = round(math.sqrt(tau2.get(hero_slug, 0.0)), 2)

                heroes[hero_slug] = {
                    "modes": hero_modes,
                    "volatility": sigma,
                    "volatility_class": volatility_class(sigma, hero_provisional),
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

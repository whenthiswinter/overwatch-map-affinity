import datetime
import json
import math
import os
from collections import defaultdict
from fractions import Fraction

import sources
from config import (
    CURRENT_IS_MIDSEASON, CURRENT_PATCH, CURRENT_PATCH_MATURE, CURRENT_SEASON, DATA_THROUGH,
    DAYS_INTO_PATCH, MAP_MODES, MATURITY_DAYS, MIN_PICK_RATE, MIN_SAMPLE_SIZE, hero_valid_from,
    hero_name, hero_role, in_current_patch, is_provisional, map_name, period, season_usable,
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
        earliest = hero_valid_from(hero_slug)
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
# other, so part of every number is noise. Slices also include wild outliers
# (Lifeweaver on King's Row: +43 in one S1 Masters Asia slice, -1 to -3 in most
# others), so a pair's value is a TRIMMED average: the top and bottom TRIM of
# its slices are dropped. Picked 2026-10-21 by held-out tests over 1,529 pairs:
# split-half reproducibility 0.50 (plain mean) -> 0.70 (30% trim), error vs the
# held-out half 2.98 -> 2.48; 30-35% tied best, median/Huber close behind.
# Per hero (within one rank/region combo):
#   - each pair's winsorized slice variance is pulled toward the hero's pooled
#     one (POOL_WEIGHT pseudo-slices), so thin pairs borrow from the hero's
#     others. The pooled one is winsorized at the pair's own trim share: a
#     1-3 slice pair trims nothing, so it borrows the plain variance, outliers
#     included. Its noise is the trimmed mean's se^2 in Yuen's small-sample
#     form, winsorized variance * (n-1) / (kept * (kept-1)). Held-out check
#     (first halves vs midseasons): standardized SD 0.94-0.99 on every filter
#     tried (plain n / kept^2 form: up to 1.19 on narrow filters);
#   - the hero's real map sensitivity tau^2 (the "noise-corrected sigma") is
#     estimated across heroes at once (map_sensitivity): each hero's own map
#     averages say how likely each tau^2 is, and heroes in general (a
#     log-normal fitted to all of them) fill in where a hero's own evidence
#     is weak. Replaced "observed variance minus noise, clamped at 0" on
#     2026-10-21: the clamp set Sierra and Venture to exactly 0 (every map
#     the same value) although a raw-data audit put them around 0.5-1. On
#     held-out data it was better in 6 of 8 filter/patch groups (tie in the
#     other 2) and for 35 of 51 heroes; the strongest specialists shrink a
#     little (Widowmaker 6.98 -> 6.43);
#   - each pair is shrunk toward the hero's mean by tau^2 / (tau^2 + se^2):
#     well-measured pairs barely move, noisy ones move a lot.
# Heroes without established (non-provisional) history can't estimate tau
# from two weeks of data, so they get the typical hero's (the fitted
# distribution's mean).
# Narrow filters (one rank and/or region) take each hero's tau^2 from the
# scope's All/All view: their own estimate is mostly noise and often hits 0,
# which flattened every map (62% of heroes on one rank + one region). The
# pre-registered test (check_rank_region.py) finds map effects don't differ
# by rank/region, and borrowing predicted held-out data better on every
# filter group and patch tested (2026-10-21). Values still come from the
# filter's own slices; only how far they're trusted is shared.
# The patch scope takes it from the all-data All/All view the same way: two
# weeks of one patch flattened 29% of heroes; borrowing cut that to 5% and
# predicted the held-out midseason better (S1-S4 first half -> midseason).
POOL_WEIGHT = 4
MIN_PAIRS_FOR_TAU = 5
TRIM = 0.30


def mean_of(values):
    return sum(values) / len(values)


def trim_count(n):
    return int(n * TRIM)


def trimmed_mean(values):
    v = sorted(values)
    c = trim_count(len(v))
    return mean_of(v[c:len(v) - c])


def winsorized_variance(values, share=None):
    """Sample variance after clipping the trimmed share of slices to the
    nearest kept value, the spread measure that matches a trimmed mean.
    share (a Fraction) overrides the trim share; None means this list's own."""
    v = sorted(values)
    c = trim_count(len(v)) if share is None else int(len(v) * share)
    if c:
        v = [v[c]] * c + v[c:len(v) - c] + [v[len(v) - c - 1]] * c
    m = mean_of(v)
    return sum((x - m) ** 2 for x in v) / (len(v) - 1)


def pooled_variance(pair_deltas, share):
    """Within-pair variance winsorized at share, pooled over a hero's pairs, or None if too thin."""
    dof = sum(len(d) - 1 for d in pair_deltas)
    if dof < 5:
        return None
    return sum(winsorized_variance(d, share) * (len(d) - 1) for d in pair_deltas if len(d) > 1) / dof


def pool_at(pair_deltas, fallback):
    """share -> pooled_variance(pair_deltas, share), cached, or fallback(share) if too thin."""
    cache = {}

    def pooled(share):
        if share not in cache:
            cache[share] = pooled_variance(pair_deltas, share) or fallback(share)
        return cache[share]
    return pooled


def pair_noise(deltas, pooled):
    """se^2 of a pair's trimmed mean, its variance pulled toward the hero's
    pooled one (pooled: share -> variance) at the same trim share."""
    n = len(deltas)
    c = trim_count(n)
    p = pooled(Fraction(c, n))
    var = ((n - 1) * winsorized_variance(deltas) + POOL_WEIGHT * p) / (n - 1 + POOL_WEIGHT) if n > 1 else p
    kept = n - 2 * c
    return var * (n - 1) / (kept * (kept - 1)) if kept > 1 else var


TAU2_GRID = [math.exp(-6 + 12 * i / 240) for i in range(241)]  # tau^2 0.0025 .. 403


def tau2_loglik(means, noises, t2):
    """Log-likelihood of a hero's map averages if their real spread were t2."""
    mu = mean_of(means)
    return sum(-0.5 * (math.log(t2 + s) + (m - mu) ** 2 / (t2 + s)) for m, s in zip(means, noises))


def map_sensitivity(evidence):
    """evidence: hero -> (map averages, their se^2). Returns (tau^2 by hero,
    typical tau^2, chance by hero that the true sigma is in the class shown).
    log tau^2 across heroes is taken as Normal(a, b^2), with a and b fitted by
    marginal likelihood on a grid; each hero's tau^2 is its posterior mean."""
    if not evidence:
        return {}, 0.0, {}
    logs = [math.log(t) for t in TAU2_GRID]
    lls = {h: [tau2_loglik(m, s, t) for t in TAU2_GRID] for h, (m, s) in evidence.items()}
    peaks = {h: max(ll) for h, ll in lls.items()}
    rel = {h: [math.exp(v - peaks[h]) for v in ll] for h, ll in lls.items()}
    best = None
    for a in (x / 4 for x in range(-16, 25)):
        for b in (k / 4 for k in range(1, 13)):
            prior = [math.exp(-0.5 * ((l - a) / b) ** 2) for l in logs]
            z = sum(prior)
            prior = [p / z for p in prior]
            fit = sum(math.log(sum(p * r for p, r in zip(prior, rs)) or 1e-300) for rs in rel.values())
            if best is None or fit > best[0]:
                best = (fit, prior)
    prior = best[1]
    tau2, class_p = {}, {}
    for h, rs in rel.items():
        w = [p * r for p, r in zip(prior, rs)]
        z = sum(w)
        tau2[h] = sum(x * t for x, t in zip(w, TAU2_GRID)) / z
        shown = sigma_band(round(math.sqrt(tau2[h]), 2))
        class_p[h] = sum(x for x, t in zip(w, TAU2_GRID) if sigma_band(math.sqrt(t)) == shown) / z
    return tau2, sum(p * t for p, t in zip(prior, TAU2_GRID)), class_p


# No floor on tau^2 here any more: it existed so a clamped tau^2 of 0 didn't
# turn into "100% certain B", and map_sensitivity never returns 0. Without it
# held-out tier forecasts (~150k, 2026-10-21) are off by 1.3 points on All/All,
# 2.1-2.3 on one rank or region, 4.1 on one rank + region (floor 2.0: 1.2 /
# 2.5 / 4.1).
def normal_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def tier_probability(adjusted, se2, tau2):
    """Chance the true value lies in the shown tier, from the noise model."""
    sd = math.sqrt(tau2 * se2 / (tau2 + se2)) if tau2 + se2 > 0 else 0.0
    if sd == 0:
        return 1.0
    edges = [-math.inf, -TIER_OUTER, -TIER_INNER, TIER_INNER, TIER_OUTER, math.inf]
    i = "DCBAS".index(tier_of(adjusted))
    return normal_cdf((edges[i + 1] - adjusted) / sd) - normal_cdf((edges[i] - adjusted) / sd)


# A class with a chance under 75% (the site's High-confidence line) is shown
# as borderline: the hero sits close enough to a line that its own data can't
# say which side. 12 of 51 heroes on 2026-10-21 (sigma 1.13-1.36, 3.03-3.25).
SIGMA_CLASSES = ["Map-Agnostic (σ < 1.2%)", "Flexible (1.2% ≤ σ < 3.0%)", "Map-Dependent (σ ≥ 3.0%)"]


def sigma_band(sigma):
    return 2 if sigma >= 3.0 else 1 if sigma >= 1.2 else 0


def volatility_class(sigma, provisional):
    if provisional:
        return "Too early to tell (new or reworked)"
    return SIGMA_CLASSES[sigma_band(sigma)]


def build_scope(raw, usable, flag_provisional, sensitivity=None):
    """Every rank x region combo for one scope, and the map sensitivity
    (tau^2 by hero, typical tau^2) its All/All view used. Each hero-map entry
    is stored once; the site rebuilds the per-map and per-hero indexes on load.
    sensitivity: another scope's, used for every combo instead of measuring."""
    slices, raw_slice_counts = flatten(raw, usable)

    # Fallback noise levels from all ranks/regions together, for combos too
    # narrow to measure their own (e.g. one patch, one rank, one region = 1 slice).
    scope_pairs = {}
    for hero_slug, items in slices.items():
        by_map = defaultdict(list)
        for item in items:
            by_map[item["map_slug"]].append(item["delta_wr"])
        scope_pairs[hero_slug] = list(by_map.values())
    scope_pooled_all = pool_at([d for p in scope_pairs.values() for d in p], lambda share: 0.0)
    scope_pooled = {h: pool_at(p, scope_pooled_all) for h, p in scope_pairs.items()}

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
            noise, evidence = {}, {}
            for hero_slug, kept in eligible.items():
                pooled = pool_at(list(kept.values()), scope_pooled.get(hero_slug, scope_pooled_all))
                noise[hero_slug] = {m: pair_noise(d, pooled) for m, d in kept.items()}
                established = [m for m in kept if not is_provisional(hero_slug, m)]
                if sensitivity is None and len(established) >= MIN_PAIRS_FOR_TAU:
                    evidence[hero_slug] = ([trimmed_mean(kept[m]) for m in established], [noise[hero_slug][m] for m in established])
            if sensitivity is None:  # first combo built is ALL_ALL
                sensitivity = map_sensitivity(evidence)
            tau2 = {h: sensitivity[0][h] for h in eligible if h in sensitivity[0]}
            typical_tau2, class_p = sensitivity[1], sensitivity[2]

            entries = []
            heroes = {}

            for hero_slug, kept in eligible.items():
                hero_tau2 = tau2.get(hero_slug, typical_tau2)
                hero_mean = mean_of([trimmed_mean(d) for d in kept.values()])
                mode_deltas = defaultdict(list)
                hero_entries = []

                for map_slug, deltas in kept.items():
                    raw_wr = trimmed_mean(deltas)
                    se2 = noise[hero_slug][map_slug]
                    weight = hero_tau2 / (hero_tau2 + se2) if hero_tau2 + se2 > 0 else 0.0
                    adj_wr = hero_mean + weight * (raw_wr - hero_mean)
                    # Labels come from the rounded values the site shows, so a
                    # "+1.20%" is never labelled B because it was really 1.1996.
                    shown_wr = round(adj_wr, 2)
                    pr_lift = round(mean_of(hero_map_pr[hero_slug][map_slug]), 1)
                    mode_deltas[MAP_MODES.get(map_slug, "Other")].append(adj_wr)

                    hero_entries.append({
                        "hero": hero_slug, "map": map_slug,
                        "delta_wr": shown_wr, "raw_delta_wr": round(raw_wr, 2),
                        "pr_lift": pr_lift,
                        "tier": tier_of(shown_wr), "presence": presence_label(pr_lift),
                        "archetype": archetype_of(shown_wr, pr_lift),
                        "sample_size": len(deltas),
                        "ci": round(1.96 * math.sqrt(se2), 2),
                        "tier_p": round(100 * tier_probability(shown_wr, se2, hero_tau2)),
                        "provisional": flag_provisional and is_provisional(hero_slug, map_slug),
                    })

                hero_modes = {m: round(mean_of(d), 2) for m, d in mode_deltas.items() if d}
                hero_provisional = hero_slug not in tau2
                sigma = round(math.sqrt(tau2.get(hero_slug, 0.0)), 2)

                heroes[hero_slug] = {
                    "modes": hero_modes,
                    "volatility": sigma,
                    "volatility_class": volatility_class(sigma, hero_provisional),
                    "volatility_p": None if hero_provisional else round(100 * class_p[hero_slug]),
                    "provisional": bool(hero_entries) and all(e["provisional"] for e in hero_entries),
                }
                entries.extend(hero_entries)

            combos[f"{rank_filter}_{region_filter}"] = {"entries": entries, "heroes": heroes}
    return combos, sensitivity


def build():
    raw = sources.load_all()
    all_scope, all_view = build_scope(raw, season_usable, flag_provisional=True)
    patch_scope, _ = build_scope(raw, in_current_patch, flag_provisional=False, sensitivity=all_view)

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
        "scopes": {"all": all_scope, "patch": patch_scope},
        "map_list": sorted(MAP_MODES.keys()),
        "hero_list": sorted(raw.keys()),
        "hero_roles": {h: hero_role(h) for h in raw.keys()},
        "hero_names": {h: hero_name(h) for h in raw.keys()},
        "map_modes": MAP_MODES,
        "map_names": {m: map_name(m) for m in MAP_MODES},
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))

    print(f"wrote {OUT_PATH} ({os.path.getsize(OUT_PATH) // 1024} KB)")


if __name__ == "__main__":
    build()

"""Pre-registered test: does a hero's map affinity depend on rank group or region?

Rule fixed on 2026-10-21, before any later data was seen. Run it at the end of
every season; don't change the rule after looking at a result.

  Split each hero-map pair's slices into two independent halves (season first
  halves vs midseasons). For every pair, measure the gap in each half:
    rank:   GM+ average minus Masters average
    region: that region's average minus the other regions' average
  If the gaps are real, a pair's gap in one half predicts its gap in the other,
  so the two halves correlate positively across all pairs. If they're noise,
  the correlation is ~0.

  A dependence counts as real only if that correlation is positive with a
  one-sided p < 0.05, tested over all established pairs at once (not hero by
  hero). The four region tests share the 0.05 (Bonferroni, 0.0125 each).
  Only then does a rank/region feature come back, and it then goes through the
  same noise adjustment as the tiers, never raw gaps.

Amended 2026-10-26: how p is computed (the rule above is unchanged).
  p used to come from Fisher's z, which assumes every pair is equally noisy.
  They aren't: a thin pair is noisy in both halves, which widens chance
  correlations ~1.4-1.6x. Simulated with no real difference, the old p fired
  13% of the time at the 5% bar (rank) and 5.5-10% at the 1.25% bars
  (regions). p now comes from that simulation: the group label (region, or
  rank) is shuffled among slices of the same pair, half, season and other
  dimension, NULL_RUNS times with a fixed seed; p = share of shuffles with a
  correlation at least as high as the real one. The change was made after
  seeing results, and it goes against the one positive finding (EU).

Result on 2026-10-21 (rule written after a first look at these numbers, so
this run is exploratory; it binds from the next season on):
  rank GM+ vs Masters r = -0.021 (1,526 pairs): not detected.
  regions: AMER -0.010, ASIA -0.014, KOREA +0.018 not detected.
  EU +0.069 passed with the old Fisher p (0.003), but its simulated p is
  0.06 (2026-10-26): not detected either. Out of sample, the "All" view also
  predicts EU and GM+ numbers better than the EU-only / GM+-only view.
"""
from collections import defaultdict

import numpy as np

import sources
from build_dataset import flatten
from config import is_provisional, season_usable

ALPHA = 0.05
REGIONS = ["AMER", "EU", "ASIA", "KOREA"]
TIERS = ["MASTER", "GRANDMASTER_AND_CHAMPION"]
MIN_SLICES = 2  # per side and half
NULL_RUNS = 2000
SEED = 20261021


def load_rows():
    """Established slices as arrays: pair-half id (2*pair + half), season, tier, region, delta."""
    slices, _ = flatten(sources.load_all(), season_usable)
    pair_ids = {}
    cols = defaultdict(list)
    for hero, items in slices.items():
        for it in items:
            if is_provisional(hero, it["map_slug"]):
                continue
            pid = pair_ids.setdefault((hero, it["map_slug"]), len(pair_ids))
            cols["ph"].append(2 * pid + (1 if it["is_midseason"] else 0))
            cols["season"].append(it["season"])
            cols["tier"].append(TIERS.index(it["tier"]))
            cols["region"].append(REGIONS.index(it["region"]))
            cols["delta"].append(it["delta_wr"])
    rows = {k: np.array(v) for k, v in cols.items()}
    rows["pairs"] = len(pair_ids)
    return rows


def split_half(rows, inside):
    """Correlation over pairs of the inside-minus-outside gap in the first half vs the midseason half."""
    size = 2 * rows["pairs"]
    ph, delta = rows["ph"], rows["delta"]
    n_in = np.bincount(ph, weights=inside, minlength=size)
    n_out = np.bincount(ph, weights=~inside, minlength=size)
    s_in = np.bincount(ph, weights=delta * inside, minlength=size)
    s_out = np.bincount(ph, weights=delta * ~inside, minlength=size)
    ok = (n_in >= MIN_SLICES) & (n_out >= MIN_SLICES)
    with np.errstate(invalid="ignore", divide="ignore"):
        gap = s_in / n_in - s_out / n_out
    both = ok[0::2] & ok[1::2]
    xs, ys = gap[0::2][both], gap[1::2][both]
    return float(np.corrcoef(xs, ys)[0, 1]), int(both.sum())


def shuffle_within(labels, strata, stable, rng):
    """labels permuted at random inside each stratum (each stratum keeps its own labels).
    stable = np.argsort(strata, kind="stable"); strata must be integers."""
    randomized = np.argsort(strata + rng.random(len(labels)))
    out = np.empty_like(labels)
    out[stable] = labels[randomized]
    return out


def simulated_p(rows, label, other, group, r_obs, rng, runs):
    """Share of label shuffles (within pair, half, season, other dimension) whose correlation reaches r_obs."""
    strata = (rows["ph"] * 10 + rows["season"]) * 10 + rows[other]
    stable = np.argsort(strata, kind="stable")
    hits = 0
    for _ in range(runs):
        r, _ = split_half(rows, shuffle_within(rows[label], strata, stable, rng) == group)
        hits += r >= r_obs
    return (1 + hits) / (1 + runs)


def run_checks(runs=NULL_RUNS):
    rows = load_rows()
    rng = np.random.default_rng(SEED)
    tests = [("rank: GM+ vs Masters", "tier", "region", TIERS.index("GRANDMASTER_AND_CHAMPION"), ALPHA)]
    tests += [(f"region: {reg} vs rest", "region", "tier", i, ALPHA / len(REGIONS)) for i, reg in enumerate(REGIONS)]

    results = []
    for name, label, other, group, alpha in tests:
        r, n = split_half(rows, rows[label] == group)
        p = simulated_p(rows, label, other, group, r, rng, runs)
        results.append({"test": name, "r": round(r, 3), "pairs": n, "p": round(p, 4), "alpha": alpha, "real": p < alpha})
    return results


def main():
    results = run_checks()
    for res in results:
        verdict = "REAL - see the rule above" if res["real"] else "not detected"
        print(f"{res['test']:24} r = {res['r']:+.3f}  pairs {res['pairs']}  p = {res['p']:.4f} (needs < {res['alpha']:.4f})  -> {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

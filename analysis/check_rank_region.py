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

Result on 2026-10-21 (rule written after a first look at these numbers, so
this run is exploratory; it binds from the next season on):
  rank GM+ vs Masters r = -0.021 (1,526 pairs, p 0.79): not detected.
  regions: AMER -0.010, ASIA -0.014, KOREA +0.018 not detected;
  EU +0.069 (p 0.003) passes, but is small: the real EU gap varies with
  SD ~0.9 points (half-split covariance), against ~4 points of noise per half.
  Out of sample, the "All" view still predicts EU (and GM+) numbers better
  than the EU-only (GM+-only) view, so no region/rank feature was added; the
  filters stay as they are, with a note.
"""
import math
from collections import defaultdict

import sources
from build_dataset import flatten, mean_of
from config import is_provisional, season_usable

ALPHA = 0.05
REGIONS = ["AMER", "EU", "ASIA", "KOREA"]
MIN_SLICES = 2  # per side and half


def one_sided_p(r, n):
    """P(correlation this high or higher | no real effect), Fisher z."""
    z = math.atanh(r) * math.sqrt(n - 3)
    return 0.5 * math.erfc(z / math.sqrt(2))


def correlation(xs, ys):
    mx, my = mean_of(xs), mean_of(ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))


def grouped():
    """hero -> map -> half ("first"/"mid") -> list of (tier, region, delta_wr), established pairs only."""
    slices, _ = flatten(sources.load_all(), season_usable)
    out = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for hero, items in slices.items():
        for it in items:
            if not is_provisional(hero, it["map_slug"]):
                half = "mid" if it["is_midseason"] else "first"
                out[hero][it["map_slug"]][half].append((it["tier"], it["region"], it["delta_wr"]))
    return out


def gap(rows, in_group):
    inside = [d for t, r, d in rows if in_group(t, r)]
    outside = [d for t, r, d in rows if not in_group(t, r)]
    if len(inside) < MIN_SLICES or len(outside) < MIN_SLICES:
        return None
    return mean_of(inside) - mean_of(outside)


def split_half(data, in_group):
    xs, ys = [], []
    for maps in data.values():
        for halves in maps.values():
            a, b = gap(halves["first"], in_group), gap(halves["mid"], in_group)
            if a is not None and b is not None:
                xs.append(a)
                ys.append(b)
    r = correlation(xs, ys)
    return r, len(xs), one_sided_p(r, len(xs))


def run_checks():
    data = grouped()
    tests = [("rank: GM+ vs Masters", lambda t, r: t == "GRANDMASTER_AND_CHAMPION", ALPHA)]
    tests += [(f"region: {reg} vs rest", (lambda reg: lambda t, r: r == reg)(reg), ALPHA / len(REGIONS)) for reg in REGIONS]

    results = []
    for name, in_group, alpha in tests:
        r, n, p = split_half(data, in_group)
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

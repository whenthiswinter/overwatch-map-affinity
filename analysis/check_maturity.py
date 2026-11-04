"""Measure from which day a patch's cumulative snapshot is worth counting.

Run when a patch has finished (the patch-change issue reminds you):
    python analysis/check_maturity.py [PATCH]     # default: the newest finished patch

Rule (fixed 2026-11-04, before measuring S5): the cutoff is the first snapshot
day from which adding the patch never makes the all-seasons numbers worse.

  Test A (the decision): leave one finished half out, build All/All from every
  other finished half plus the patch as it looked on day d (or without it), and
  score the adjusted values against the left-out half's raw trimmed averages.
  "Worse" = the mean RMSE change over the left-out halves is above 0.
  Test B (supporting): the patch's own averages on day d vs on its last day,
  next to how far two consecutive whole halves sit apart.

Result for S5 (2026-11-04, 22 snapshots, days 7-29): days 7-13 +0.000 to +0.001
(noise, ±0.005), day 14 onwards always negative (-0.005, reaching -0.011 by day
28). Test B: day 14 is the first day S5's numbers were closer to their final
values (3.42) than two consecutive whole halves are to each other (3.48 on
average). MATURITY_DAYS set to 14 (was a 21-day placeholder). Takes ~3 minutes.
"""
import datetime
import math
import statistics as st
import sys
from collections import defaultdict

import build_dataset as bd
import snapshots
import sources
from config import canonical_slug, load_patch_state, period, valid_from


def to_raw(snap):
    return {canonical_slug(h): sl for h, sl in snapshots.to_slices(snap).items()}


def merged(*parts):
    out = defaultdict(list)
    for part in parts:
        for hero, sl in part.items():
            out[hero].extend(sl)
    return dict(out)


def pair_averages(raw, keep):
    """Raw trimmed average per pair over the slices keep(season, is_mid) selects."""
    slices, _ = bd.flatten(raw, lambda h, m, s, im: keep(s, im) and period(s, im) >= valid_from(h, m))
    pairs = defaultdict(list)
    for hero, items in slices.items():
        for it in items:
            pairs[(hero, it["map_slug"])].append(it["delta_wr"])
    return {k: bd.trimmed_mean(v) for k, v in pairs.items() if len(v) >= 3}


def rmse(a, b):
    keys = a.keys() & b.keys()
    return math.sqrt(st.mean([(a[k] - b[k]) ** 2 for k in keys])), keys


def main():
    state = load_patch_state()
    finished = [p for p in state["patches"] if p["id"] != state["current"]]
    # Named explicitly, any patch can be measured (e.g. the current one at its end,
    # before the next reset is detected); by default the newest finished one.
    wanted = sys.argv[1] if len(sys.argv) > 1 else (finished[-1]["id"] if finished else None)
    patch = next((p for p in state["patches"] if p["id"] == wanted), None)
    if patch is None:
        print(f"no patch {wanted!r} in state.json (finished: {[p['id'] for p in finished]})")
        return 1

    start = datetime.date.fromisoformat(patch["started"])
    daily = [snapshots.load_snapshot(p) for p in snapshots.snapshot_paths()]
    daily = [(( datetime.date.fromisoformat(s["date"]) - start).days, s) for s in daily if snapshots.patch_of(s) == patch["id"]]
    if len(daily) < 3:
        print(f"only {len(daily)} snapshots of {patch['id']}; nothing to measure")
        return 1
    tested = (patch["season"], patch["is_midseason"])

    # Everything finished except the tested patch: the OWTics history plus the
    # final snapshot of every other finished patch (never the one in progress).
    base = sources.load_history()
    for pid, snap in snapshots.latest_per_patch().items():
        if pid not in (patch["id"], state["current"]):
            base = merged(base, to_raw(snap))
    halves = sorted({(s["season"], s.get("isMidseason", False)) for sl in base.values() for s in sl} - {tested})
    targets = {h: pair_averages(base, lambda s, im, h=h: (s, im) == h) for h in halves}

    bd.RANKS, bd.REGIONS = ["ALL"], ["ALL"]  # only the All/All view is scored

    def score(raw, held):
        usable = lambda h, m, s, im: period(s, im) >= valid_from(h, m) and (s, im) != held
        combos, _ = bd.build_scope(raw, usable, flag_provisional=False)
        est = {(e["hero"], e["map"]): e["delta_wr"] for e in combos["ALL_ALL"]["entries"]}
        return rmse(est, targets[held])[0]

    print(f"{patch['id']}: {len(daily)} snapshots, days {daily[0][0]}-{daily[-1][0]}; {len(halves)} finished halves to leave out", flush=True)
    without = {h: score(base, h) for h in halves}
    change = {}
    for day, snap in daily:
        raw = merged(base, to_raw(snap))
        diffs = [score(raw, h) - without[h] for h in halves]
        change[day] = (st.mean(diffs), st.stdev(diffs) / math.sqrt(len(diffs)), sum(d < 0 for d in diffs))
        print(f"  day {day:2d}: RMSE change {change[day][0]:+.4f} ± {change[day][1]:.4f}, better in {change[day][2]}/{len(halves)}", flush=True)

    cutoff = next((d for d, _ in daily if all(change[e][0] <= 0 for e, _ in daily if e >= d)), None)

    print(f"\nTest B: {patch['id']}'s own averages vs its last day")
    final = pair_averages(to_raw(daily[-1][1]), lambda s, im: True)
    gaps = [rmse(targets[a], targets[b])[0] for a, b in zip(halves, halves[1:])]
    print(f"  two consecutive whole halves sit {st.mean(gaps):.2f} apart on average")
    for day, snap in daily:
        dist, keys = rmse(pair_averages(to_raw(snap), lambda s, im: True), final)
        print(f"  day {day:2d}: {dist:.2f} from the last day")

    print(f"\nCutoff by the rule: day {cutoff}" if cutoff is not None else "\nAdding the patch still hurts on its last day: no cutoff")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Spot a new patch in the daily snapshots and keep data/snapshots/state.json current.

Blizzard's rates are cumulative since the current patch started and refresh in
batches every 2-3 days. A season or midseason patch resets them; balance
hotfixes don't (the 2026-10-13 hotfix left the data untouched). A reset is
recognised by comparing the newest snapshot with the last one that differs:

  normal refresh: overall pick rate moves ~0.1-0.2 (median), per-map WR ~1.5-2.5
  reset:          overall pick rate moves ~1.0+,              per-map WR ~5.5-8
  (calibrated 2026-10-20 on S4 -> S4 midseason -> S5 transitions)

On a reset the newest snapshot is re-stamped with a new patch, labelled from
Blizzard's patch notes ("Season N" = new season, "Mid-Season" = midseason,
anything else = another reset inside the current half). Whatever needs a
human is collected into one issue, written as JSON to $ISSUE_OUT for the
workflow to file (or printed when run locally).
"""
import datetime
import json
import os
import re
import statistics

import snapshots
import sources
from collect_live import get
from config import HERO_VALID_FROM_SEASON, PATCH_STATE_PATH, load_patch_state, period

PATCH_NOTES = "https://overwatch.blizzard.com/en-us/news/patch-notes/"

RESET_PR_SHIFT = 0.5      # median |overall pick rate change|
RESET_MAP_WR_SHIFT = 4.0  # median |per-map win rate change|
NOTES_GRACE_DAYS = 3      # Blizzard can lag a day; past this, a missing reset is suspicious


def rates_by_key(snapshot, overall):
    out = {}
    for s in snapshot["slices"]:
        if (s["map"] == "all-maps") != overall:
            continue
        for hero, (wr, pr) in s["rates"].items():
            if wr is not None and pr is not None:
                out[(s["region"], s["tier"], s["map"], hero)] = (wr, pr)
    return out


def shift(new, old):
    """Median movement between two snapshots: overall pick rate, per-map win rate."""
    a, b = rates_by_key(new, True), rates_by_key(old, True)
    pr = [abs(a[k][1] - b[k][1]) for k in a.keys() & b.keys()]
    a, b = rates_by_key(new, False), rates_by_key(old, False)
    wr = [abs(a[k][0] - b[k][0]) for k in a.keys() & b.keys()]
    return statistics.median(pr), statistics.median(wr)


def major_patches():
    """Season / midseason entries from Blizzard's patch notes, newest first:
    [(date, "season" | "midseason", season number or None, heading)]."""
    page = get(PATCH_NOTES, as_json=False)
    found = []
    for entry in re.split(r'(?=<div class="PatchNotes-patch[ "])', page)[1:]:
        date = re.search(r'id="patch-(\d{4}-\d{2}-\d{2})"', entry)
        heading = re.search(r'class="PatchNotes-sectionTitle"[^>]*>(.*?)</h4>', entry, re.S)
        if not date or not heading:
            continue
        title = re.sub(r"<[^>]+>", "", heading.group(1)).strip()
        if re.search(r"mid-?\s?season", title, re.I):
            found.append((date.group(1), "midseason", None, title))
        elif m := re.search(r"\bSeason\s+(\d+)\b", title):
            found.append((date.group(1), "season", int(m.group(1)), title))
    return found


def label_new_patch(state, current, reset_date, notes):
    """Which patch the reset belongs to, preferring patch notes, else guessing."""
    recent = [n for n in notes if current["started"] < n[0] <= reset_date]
    if recent:
        date, kind, number, heading = recent[0]
        if kind == "season" and number and number > current["season"]:
            return {"id": f"S{number}", "season": number, "is_midseason": False, "started": date}, f'patch notes: "{heading}"'
        if kind == "midseason" and not current["is_midseason"]:
            return {"id": f"S{current['season']}-mid", "season": current["season"], "is_midseason": True, "started": date}, f'patch notes: "{heading}"'

    # No matching notes: treat it as another reset within the current half.
    base = re.sub(r"-\d+$", "", current["id"])
    taken = {p["id"] for p in state["patches"]}
    k = 2
    while f"{base}-{k}" in taken:
        k += 1
    patch = {"id": f"{base}-{k}", "season": current["season"], "is_midseason": current["is_midseason"], "started": reset_date}
    return patch, "no season/midseason patch notes found, so filed under the current half"


def history_roster():
    """Heroes and maps in the OWTics history, counting only rows from on/after
    a hero's valid-from. OWTics returns the current season's numbers for any
    season asked about a hero who didn't exist yet, so Doctrine has fake S4
    rows, and those even list the S5-only map Grimsvotn."""
    heroes, maps = set(), set()
    for hero, slices in sources.load_history().items():
        for s in slices:
            if period(s["season"], s.get("isMidseason", False)) < HERO_VALID_FROM_SEASON.get(hero, 1):
                continue
            heroes.add(hero)
            maps.update(m["map"]["slug"] for m in s["measurements"])
    return heroes, maps


def update_roster(state, newest, paths, notified):
    """Record when heroes/maps unknown to the history first appear (config.py
    uses that as their valid-from, so they show up as provisional at once) and
    flag role or mode changes, which usually mean a rework."""
    first_seen = state.setdefault("first_seen", {"heroes": {}, "maps": {}})
    known_heroes, known_maps = history_roster()
    now = period(newest["season"], newest.get("is_midseason", False))
    patch = snapshots.patch_of(newest)
    problems = []

    for hero, info in sorted(newest["heroes"].items()):
        if hero not in known_heroes and hero not in first_seen["heroes"]:
            first_seen["heroes"][hero] = now
            problems.append(f"- **New hero: {info['name']}** ({info['role']}), first seen in `{patch}`. Shown automatically, marked provisional. "
                            f"Nothing to do unless it's really an existing hero under a new name.")
    for slug, info in sorted(newest["maps"].items()):
        if slug not in known_maps and slug not in first_seen["maps"]:
            first_seen["maps"][slug] = now
            problems.append(f"- **New map: {info['name']}** ({info['mode']}), first seen in `{patch}`. Shown automatically, marked provisional.")

    if len(paths) > 1:
        previous = snapshots.load_snapshot(paths[-2])
        for hero, info in sorted(newest["heroes"].items()):
            old = previous["heroes"].get(hero)
            key = f"role:{hero}:{info['role']}"
            if old and old["role"] != info["role"] and key not in notified:
                notified.add(key)
                problems.append(f"- **{info['name']} changed role: {old['role']} → {info['role']}.** That usually means a rework: add "
                                f"`\"{hero}\": {now}` to `HERO_VALID_FROM_SEASON` in `analysis/config.py`, so older data stops counting.")
        for slug, info in sorted(newest["maps"].items()):
            old = previous["maps"].get(slug)
            key = f"mode:{slug}:{info['mode']}"
            if old and old["mode"] != info["mode"] and key not in notified:
                notified.add(key)
                problems.append(f"- **{info['name']} changed mode: {old['mode']} → {info['mode']}.** Probably a rework: add "
                                f"`\"{slug}\": {now}` to `MAP_VALID_FROM_SEASON` in `analysis/config.py`.")
    return problems


def main():
    state = load_patch_state()
    current = next(p for p in state["patches"] if p["id"] == state["current"])
    notified = set(state.setdefault("notified", []))
    problems = []

    paths = snapshots.snapshot_paths()
    if not paths:
        print("no snapshots yet")
        return 0
    newest_path = paths[-1]
    newest = snapshots.load_snapshot(newest_path)
    today = newest["date"]

    try:
        notes = major_patches()
    except Exception as exc:
        notes = []
        print(f"could not read patch notes: {exc}")

    # The last earlier snapshot of the same patch whose numbers differ.
    previous = None
    for path in reversed(paths[:-1]):
        snap = snapshots.load_snapshot(path)
        if snapshots.patch_of(snap) != snapshots.patch_of(newest):
            break
        if snap["slices"] != newest["slices"]:
            previous = snap
            break

    if previous is None:
        print(f"{today}: no data refresh to compare against")
    else:
        pr_shift, wr_shift = shift(newest, previous)
        print(f"{today} vs {previous['date']}: overall PR shift {pr_shift:.2f}, per-map WR shift {wr_shift:.2f}")
        is_pr, is_wr = pr_shift >= RESET_PR_SHIFT, wr_shift >= RESET_MAP_WR_SHIFT

        if is_pr and is_wr:
            patch, reason = label_new_patch(state, current, today, notes)
            patch["detected_by"] = f"reset on {today} vs {previous['date']} (PR {pr_shift:.2f}, WR {wr_shift:.2f}); {reason}"
            state["patches"].append(patch)
            state["current"] = patch["id"]
            newest.update({"patch": patch["id"], "season": patch["season"], "is_midseason": patch["is_midseason"]})
            snapshots.save_snapshot(newest_path, newest)
            problems.append(
                f"- **New patch detected: `{patch['id']}`** (season {patch['season']}, {'midseason' if patch['is_midseason'] else 'first half'}, "
                f"started {patch['started']}). {patch['detected_by']}. `{current['id']}` is now frozen at {previous['date']}'s snapshot.\n"
                f"  - Check the patch notes for **reworked heroes or maps** and add them to `HERO_VALID_FROM_SEASON` / `MAP_VALID_FROM_SEASON` "
                f"(use `{patch['season']}{'.5' if patch['is_midseason'] else ''}`).\n"
                f"  - If the label is wrong, fix `data/snapshots/state.json` and the snapshot's `patch` field."
                + (f"\n  - **Season {current['season']} is complete:** run the pre-registered rank/region test "
                   f"(`python analysis/check_rank_region.py`, rule fixed 2026-10-21; don't change it after seeing the result), "
                   f"then regenerate the report and charts."
                   if patch["season"] > current["season"] else "")
            )
            print(f"NEW PATCH {patch['id']}")
        elif is_pr or is_wr:
            key = f"ambiguous:{today}"
            if key not in notified:
                problems.append(f"- **Possible patch reset on {today}** (PR shift {pr_shift:.2f}, WR shift {wr_shift:.2f}), but only one signal passed. Not acted on; check the data.")
                notified.add(key)

    problems += update_roster(state, newest, paths, notified)

    # Season/midseason notes with no reset after a few days.
    if state["current"] == current["id"]:
        for date, kind, number, heading in notes:
            stale = (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(date)).days > NOTES_GRACE_DAYS
            key = f"notes-no-reset:{date}"
            if date > current["started"] and stale and key not in notified:
                problems.append(f'- **Patch notes from {date} ("{heading}") but no data reset seen** in {NOTES_GRACE_DAYS}+ days. Check the snapshots.')
                notified.add(key)

    state["notified"] = sorted(notified)
    with open(PATCH_STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
        f.write("\n")

    if problems:
        issue = {"title": f"Data pipeline: action needed ({today})", "body": "\n".join(problems)}
        out = os.environ.get("ISSUE_OUT")
        if out:
            with open(out, "w", encoding="utf-8") as f:
                json.dump(issue, f)
        else:
            print(f"\n{issue['title']}\n{issue['body']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

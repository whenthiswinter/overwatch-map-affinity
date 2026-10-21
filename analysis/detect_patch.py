"""Spot a new patch in the daily snapshots and keep data/snapshots/state.json current.

Blizzard's rates are cumulative since the current patch started and refresh in
batches every 2-3 days. A season or midseason patch resets them; balance
hotfixes don't (the 2026-10-13 hotfix left the data untouched). A reset is
recognised by comparing the newest snapshot with the last one that differs:

  normal refresh: overall pick rate moves ~0.1-0.2 (median), per-map WR ~1.5-2.5
  reset:          overall pick rate moves ~1.0+,              per-map WR ~5.5-8
  (calibrated 2026-10-20 on S4 -> S4 midseason -> S5 transitions)

On a reset the newest snapshot is re-stamped with a new patch. The label comes
from three independent signals (label_new_patch): a "Season N" patch-notes
heading, the season on Blizzard's homepage, and China's season calendar. No
season signal inside a season's first half means the midseason, confirmed by
a big patch in the notes and/or the calendar midpoint. Backtested 2026-10-21
on the real S4 midseason (2 confirmations) and S5 launch (3). Whatever needs
a human is collected into one issue, written as JSON to $ISSUE_OUT for the
workflow to file (or printed when run locally).
"""
import datetime
import html
import json
import os
import re
import statistics

import snapshots
import sources
from collect_live import get
from config import HERO_VALID_FROM_SEASON, PATCH_STATE_PATH, load_patch_state, period

PATCH_NOTES = "https://overwatch.blizzard.com/en-us/news/patch-notes/"
PATCH_NOTES_MONTH = "https://overwatch.blizzard.com/en-us/news/patch-notes/live/{year}/{month:02d}/"
HOMEPAGE = "https://overwatch.blizzard.com/en-us/"
CHINA_CALENDAR = "https://webapi.blizzard.cn/ow-armory-server/index"

MAJOR_PATCH_HERO_UPDATES = 10  # 2026: hotfixes 0-5 hero changes, S4 midseason 27, season launches 32-46
NEW_SEASON_WINDOW_DAYS = 7     # calendar season start vs the reset we saw
MIDSEASON_WINDOW_DAYS = 14     # S4's midseason landed 1 day from its calendar midpoint

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


def parse_patch_notes(page):
    """[{date, heading, season, hero_updates}] for each patch on a notes page.
    `season` is N when the first section is a "Season N" launch heading."""
    found = []
    for entry in re.split(r'(?=<div class="PatchNotes-patch[ "])', page)[1:]:
        date = re.search(r'id="patch-(\d{4}-\d{2}-\d{2})"', entry)
        if not date:
            continue
        heading = re.search(r'class="PatchNotes-sectionTitle"[^>]*>(.*?)</h4>', entry, re.S)
        title = html.unescape(re.sub(r"<[^>]+>", "", heading.group(1))).strip() if heading else ""
        season = re.search(r"\bSeason\s+(\d+)\b", title)
        found.append({
            "date": date.group(1), "heading": title,
            "season": int(season.group(1)) if season else None,
            "hero_updates": len(re.findall(r'class="PatchNotesHeroUpdate-name"', entry)),
        })
    return found


def patch_notes(since):
    """Every patch since `since`: the main page plus the monthly archives, so
    a midseason patch isn't lost behind a few hotfixes."""
    pages = [PATCH_NOTES]
    month = datetime.date.fromisoformat(since).replace(day=1)
    while month <= datetime.date.today():
        pages.append(PATCH_NOTES_MONTH.format(year=month.year, month=month.month))
        month = (month + datetime.timedelta(days=32)).replace(day=1)
    notes = {}
    for url in pages:
        for n in parse_patch_notes(get(url, as_json=False)):
            notes[n["date"]] = n
    return sorted(notes.values(), key=lambda n: n["date"], reverse=True)


def homepage_season():
    """The season Blizzard's homepage advertises ("Season 5: A Grim Doctrine")."""
    text = html.unescape(re.sub(r"<[^>]+>", " ", get(HOMEPAGE, as_json=False)))
    numbers = [int(n) for n in re.findall(r"\bSeason\s+(\d+)\s*:", text)]
    return max(numbers) if numbers else None


def china_calendar():
    """[{season, start, end}] from the Chinese armory's season list."""
    seasons = get(CHINA_CALENDAR)["data"]["seasons"]
    out = []
    for s in seasons:
        start, end = re.findall(r"\d{4}-\d{2}-\d{2}", s["desc"])
        out.append({"season": int(s["id"]), "start": start, "end": end})
    return out


def gather_signals(since):
    """Independent hints about which patch is live; any of them may be missing."""
    signals = {}
    for name, fetch in (("notes", lambda: patch_notes(since)), ("homepage", homepage_season), ("calendar", china_calendar)):
        try:
            signals[name] = fetch()
        except Exception as exc:
            signals[name] = None
            print(f"signal {name} unavailable: {exc}")
    return signals


def days_between(a, b):
    return abs((datetime.date.fromisoformat(a) - datetime.date.fromisoformat(b)).days)


def label_new_patch(state, current, reset_date, signals):
    """(patch, reasons, confirmed) for a detected reset.

    Only season and midseason patches reset the numbers (2026: the 10-13 balance
    hotfix didn't), so a reset is a new season if any season signal says so,
    otherwise the midseason if we're in a season's first half. Midseason patch
    notes never say "midseason" (S4's opened with "Junkrat's Loot Hunt"), but
    they're big: 27 hero changes vs 0-5 for hotfixes."""
    notes = [n for n in (signals.get("notes") or []) if current["started"] < n["date"] <= reset_date]
    calendar = signals.get("calendar") or []

    votes = {}
    for n in notes:
        if n["season"] and n["season"] > current["season"]:
            votes.setdefault(n["season"], []).append((n["date"], f'patch notes {n["date"]}: "{n["heading"]}"'))
    homepage = signals.get("homepage")
    if homepage and homepage > current["season"]:
        votes.setdefault(homepage, []).append((reset_date, f"Blizzard homepage shows Season {homepage}"))
    for s in calendar:
        if s["season"] > current["season"] and days_between(s["start"], reset_date) <= NEW_SEASON_WINDOW_DAYS:
            votes.setdefault(s["season"], []).append((s["start"], f"China calendar: Season {s['season']} starts {s['start']}"))

    if votes:
        number = max(votes)
        reasons = [r for _, r in votes[number]]
        if len(votes) > 1:
            reasons.append(f"**signals disagree on the season number** ({sorted(votes)}), used the highest")
        started = min(d for d, _ in votes[number])
        patch = {"id": f"S{number}", "season": number, "is_midseason": False, "started": started}
        return patch, reasons, len(votes) == 1

    if not current["is_midseason"]:
        reasons = []
        big = [n for n in notes if n["hero_updates"] >= MAJOR_PATCH_HERO_UPDATES]
        if big:
            reasons.append(f'big patch on {big[-1]["date"]} ({big[-1]["hero_updates"]} hero changes)')
        season = next((s for s in calendar if s["season"] == current["season"]), None)
        if season:
            start, end = (datetime.date.fromisoformat(season[k]) for k in ("start", "end"))
            middle = (start + (end - start) / 2).isoformat()
            if days_between(middle, reset_date) <= MIDSEASON_WINDOW_DAYS:
                reasons.append(f"reset is near the middle of Season {current['season']} (calendar midpoint {middle})")
        started = big[-1]["date"] if big else reset_date
        patch = {"id": f"S{current['season']}-mid", "season": current["season"], "is_midseason": True, "started": started}
        return patch, reasons or ["unconfirmed: no big patch in the notes and no calendar support"], bool(reasons)

    # A second reset inside a midseason half, with no new-season signal: unexpected.
    base = re.sub(r"-\d+$", "", current["id"])
    taken = {p["id"] for p in state["patches"]}
    k = 2
    while f"{base}-{k}" in taken:
        k += 1
    patch = {"id": f"{base}-{k}", "season": current["season"], "is_midseason": current["is_midseason"], "started": reset_date}
    return patch, ["unexpected: a reset during a midseason with no sign of a new season"], False


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

    signals = gather_signals(current["started"])
    # Kept in state.json (committed by the workflow) so it's visible whether
    # each signal is reachable from GitHub's runners.
    state["signals"] = {name: "ok" if value is not None else "unavailable" for name, value in signals.items()}

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
            patch, reasons, confirmed = label_new_patch(state, current, today, signals)
            patch["detected_by"] = f"reset on {today} vs {previous['date']} (PR {pr_shift:.2f}, WR {wr_shift:.2f}); " + "; ".join(reasons)
            if not confirmed:
                patch["detected_by"] += " **[label unconfirmed: please check]**"
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

    # A big patch or a newer season on the homepage, but no reset after a few days.
    if state["current"] == current["id"]:
        for n in signals.get("notes") or []:
            big = n["season"] or n["hero_updates"] >= MAJOR_PATCH_HERO_UPDATES
            key = f"notes-no-reset:{n['date']}"
            if big and n["date"] > current["started"] and days_between(today, n["date"]) > NOTES_GRACE_DAYS and key not in notified:
                problems.append(f'- **Big patch on {n["date"]} ("{n["heading"]}", {n["hero_updates"]} hero changes) but no data reset seen** '
                                f"in {NOTES_GRACE_DAYS}+ days. Check the snapshots.")
                notified.add(key)
        homepage = signals.get("homepage")
        key = f"homepage-no-reset:{homepage}"
        if homepage and homepage > current["season"] and key not in notified:
            problems.append(f"- **Blizzard's homepage shows Season {homepage}, but the data hasn't reset yet** (current patch `{current['id']}`). "
                            "Usually it resets within a day or two; if this persists, check the snapshots.")
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

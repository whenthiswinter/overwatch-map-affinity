"""Daily snapshot of current-patch per-map rates from the official sources.

Blizzard (Americas/Europe/Asia) and Nexon (Korea) only serve the current
patch, cumulative since the patch started, so the backlog has to be built by
saving a snapshot every day. Safe to run repeatedly: it exits right away once
today's snapshot exists with Korea in it, and writes nothing unless every
Blizzard request succeeded.

Nexon's Cloudflare refuses some GitHub runners (403), so Korea may fail on its
own: the snapshot is then saved without it, and later runs that day (or a run
from a local PC) try Korea again and add it. Builders fill a missing Korea from
the newest snapshot of the same patch that has it (snapshots.latest_per_patch).
"""
import datetime
import html
import json
import os
import re
import sys
import time
import traceback

from curl_cffi import requests

import snapshots
from config import SNAPSHOT_DIR, canonical_slug, current_patch

LOG_PATH = os.path.join(SNAPSHOT_DIR, "collect.log")
RUNS_PATH = os.path.join(SNAPSHOT_DIR, "runs.log")

BLIZZARD_PAGE = "https://overwatch.blizzard.com/en-us/rates/"
BLIZZARD_DATA = "https://overwatch.blizzard.com/en-us/rates/data/"
NEXON_PAGE = "https://overwatch.nexon.com/hero/rate"
NEXON_DATA = "https://overwatch-api.nexon.com/HeroRate"

BLIZZARD_REGIONS = {"Americas": "AMER", "Europe": "EU", "Asia": "ASIA"}
BLIZZARD_TIERS = {"Master": "MASTER", "Grandmaster": "GRANDMASTER_AND_CHAMPION"}
NEXON_TIERS = {"master": "MASTER", "grandmaster": "GRANDMASTER_AND_CHAMPION"}

# Overall rates (all maps) are collected too; they make patch resets easy to spot.
ALL_MAPS = "all-maps"
# A sanity floor for the overall (all maps) lists only, which always name every
# hero. Per-map lists only include heroes with games on that map, so right after
# a patch reset they're legitimately short (Korea GM, Blizzard World, 2 days
# into S5-mid: 15 heroes), which blocked collection 2026-11-05..07.
MIN_HEROES = 40
MAX_EMPTY_KR_MAPS = 8
DELAY = 0.4
RETRIES = 3

session = requests.Session(impersonate="chrome")


def log(msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(line, flush=True)
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def get(url, params=None, as_json=True):
    for attempt in range(1, RETRIES + 1):
        try:
            res = session.get(url, params=params, timeout=20)
            res.raise_for_status()
            return res.json() if as_json else res.text
        except Exception as exc:
            if attempt == RETRIES:
                raise RuntimeError(f"{url} {params}: {exc}") from exc
            time.sleep(3 * attempt)


def rate(value):
    """Rates come back as numbers, or as '--' when there isn't enough data."""
    return value if isinstance(value, (int, float)) else None


def select_block(page, select_id):
    match = re.search(rf'<select[^>]*id="{select_id}".*?</select>', page, re.S)
    if not match:
        raise RuntimeError(f"Blizzard page layout changed: no #{select_id}")
    return match.group(0)


def blizzard_filters():
    page = get(BLIZZARD_PAGE, as_json=False)

    rq_options = dict(re.findall(r'<option[^>]*data-title="([^"]*)"[^>]*value="([^"]*)"', select_block(page, "filter-rq-select")))
    rq = rq_options.get("Competitive - Role Queue")
    if rq is None:
        raise RuntimeError(f"no competitive role queue option in {rq_options}")

    maps = {}
    groups = re.findall(r'<optgroup[^>]*label="([^"]*)"[^>]*>(.*?)</optgroup>', select_block(page, "filter-map-select"), re.S)
    for mode, body in groups:
        for title, slug in re.findall(r'<option[^>]*data-title="([^"]*)"[^>]*value="([^"]*)"', body):
            maps[slug] = {"name": html.unescape(title), "mode": mode}
    if len(maps) < 20:
        raise RuntimeError(f"only {len(maps)} maps found on the Blizzard page")
    return rq, maps


def nexon_rq():
    page = get(NEXON_PAGE, as_json=False)
    match = re.search(r'<script[^>]*id="__NUXT_DATA__"[^>]*>(.*?)</script>', page, re.S)
    if not match:
        raise RuntimeError("Nexon page layout changed: no __NUXT_DATA__")
    state = json.loads(match.group(1))
    for i, value in enumerate(state):
        if "경쟁전 - 역할 고정" in str(value):  # "Competitive - Role Queue"
            return str(state[i - 1])
    raise RuntimeError("no competitive role queue code on the Nexon page")


def collect_blizzard(rq, map_slugs, heroes):
    slices = []
    for region, region_code in BLIZZARD_REGIONS.items():
        for tier, tier_code in BLIZZARD_TIERS.items():
            for map_slug in [ALL_MAPS] + map_slugs:
                params = {"input": "PC", "map": map_slug, "region": region, "role": "All", "rq": rq, "tier": tier}
                data = get(BLIZZARD_DATA, params)
                selected = data["rates"]["selected"]
                if any(str(selected.get(k)) != str(v) for k, v in params.items()):
                    raise RuntimeError(f"Blizzard answered {selected} for {params}")

                rows = data["rates"]["rates"]
                if len(rows) < (MIN_HEROES if map_slug == ALL_MAPS else 1):
                    raise RuntimeError(f"only {len(rows)} heroes for {params}")

                rates = {}
                for row in rows:
                    slug = canonical_slug(row["id"])
                    rates[slug] = [rate(row["cells"].get("winrate")), rate(row["cells"].get("pickrate"))]
                    heroes.setdefault(slug, {
                        "name": row["hero"]["name"],
                        "role": row["hero"]["role"].title(),
                        "subrole": row["hero"].get("subrole"),
                    })
                slices.append({"region": region_code, "tier": tier_code, "map": map_slug, "rates": rates})
                time.sleep(DELAY)
    return slices


def collect_nexon(rq, map_slugs):
    slices = []
    empty = []
    for tier, tier_code in NEXON_TIERS.items():
        for map_slug in [ALL_MAPS] + map_slugs:
            params = {"map": "all" if map_slug == ALL_MAPS else map_slug, "role": "all", "rq": rq, "input": "pc", "region": "korea", "rank": tier}
            rows = get(NEXON_DATA, params)["data"]["list"]
            # Korea can have no data at all for a map that isn't in its pool
            # (Hollywood in S5); OWTics shows the same gap. Many empty maps at
            # once would mean something is broken, though.
            if not rows and map_slug != ALL_MAPS:
                empty.append(f"{map_slug}/{tier}")
                if len(empty) > MAX_EMPTY_KR_MAPS:
                    raise RuntimeError(f"too many empty Nexon maps: {empty}")
                continue
            if map_slug == ALL_MAPS and len(rows) < MIN_HEROES:
                raise RuntimeError(f"only {len(rows)} heroes for Nexon {params}")

            rates = {canonical_slug(r["heroId"]): [rate(r.get("winRate")), rate(r.get("pickRate"))] for r in rows}
            slices.append({"region": "KOREA", "tier": tier_code, "map": map_slug, "rates": rates})
            time.sleep(DELAY)
    return slices, empty


def note_run(outcome):
    """One line per invocation, so a scheduled task that never fires (or dies
    before logging) shows up as a gap instead of silence."""
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    with open(RUNS_PATH, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {outcome}\n")


def collect_korea(map_slugs):
    """(Korea slices, nexon source info); no slices when Nexon refuses."""
    try:
        kr_rq = nexon_rq()
        kr_slices, kr_empty = collect_nexon(kr_rq, map_slugs)
    except Exception as exc:
        return [], {"status": "failed", "error": str(exc)[:300]}
    return kr_slices, {"status": "ok", "rq": kr_rq, "empty_maps": kr_empty}


def add_korea(path):
    """Today's snapshot was saved without Korea: try Korea again."""
    snapshot = snapshots.load_snapshot(path)
    kr_slices, nexon = collect_korea(sorted(snapshot["maps"]))
    if not kr_slices:
        log(f"Korea still unavailable for {os.path.basename(path)}: {nexon['error']}")
        note_run("skipped (Korea still failing)")
        return 0
    snapshot["slices"] += kr_slices
    snapshot["sources"]["nexon"] = nexon
    snapshots.save_snapshot(path, snapshot)
    log(f"added Korea to {os.path.basename(path)}: {len(kr_slices)} slices")
    note_run("Korea added")
    return 0


def main():
    today = datetime.date.today().isoformat()
    path = os.path.join(SNAPSHOT_DIR, f"{today}.json.gz")
    if os.path.exists(path):
        if not snapshots.has_korea(snapshots.load_snapshot(path)):
            return add_korea(path)
        print(f"{path} already exists, nothing to do")
        note_run("skipped (already collected today)")
        return 0

    started = time.time()
    try:
        bliz_rq, maps = blizzard_filters()
        heroes = {}
        map_slugs = sorted(maps)
        slices = collect_blizzard(bliz_rq, map_slugs, heroes)
    except Exception as exc:
        log(f"FAILED: {exc}")
        note_run("failed")
        return 1
    kr_slices, nexon = collect_korea(map_slugs)
    slices += kr_slices

    patch = current_patch()
    snapshot = {
        "date": today,
        "collected_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "patch": patch["id"],
        "season": patch["season"],
        "is_midseason": patch["is_midseason"],
        "sources": {"blizzard": {"rq": bliz_rq}, "nexon": nexon},
        "heroes": heroes,
        "maps": maps,
        "slices": slices,
    }
    snapshots.save_snapshot(path, snapshot)

    log(f"saved {os.path.basename(path)}: {len(slices)} slices, {len(heroes)} heroes, {len(maps)} maps, "
        f"{os.path.getsize(path) // 1024} KB, {time.time() - started:.0f}s")
    if nexon["status"] == "ok":
        note_run("saved")
        if nexon["empty_maps"]:
            log(f"note: no Korea data for {', '.join(nexon['empty_maps'])}")
    else:
        log(f"saved without Korea (Nexon: {nexon['error']}); later runs today will retry it")
        note_run("saved without Korea")
    return 0


if __name__ == "__main__":
    # Under pythonw there is no console, so an uncaught error would vanish.
    try:
        code = main()
    except Exception:
        log("CRASHED:\n" + traceback.format_exc())
        note_run("crashed")
        code = 1
    sys.exit(code)

"""Read daily snapshots from collect_live.py in the raw cache's slice format."""
import gzip
import json
import os
from collections import defaultdict

SNAPSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "snapshots")


def snapshot_paths():
    if not os.path.isdir(SNAPSHOT_DIR):
        return []
    return sorted(os.path.join(SNAPSHOT_DIR, f) for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json.gz"))


def load_snapshot(path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def save_snapshot(path, snapshot):
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump(snapshot, f, separators=(",", ":"))
    os.replace(tmp, path)


def latest_roster():
    """Heroes (name, role, subrole) and maps (name, mode) as Blizzard listed
    them in the newest snapshot; empty before the first snapshot exists."""
    paths = snapshot_paths()
    if not paths:
        return {"heroes": {}, "maps": {}}
    snapshot = load_snapshot(paths[-1])
    return {"heroes": snapshot["heroes"], "maps": snapshot["maps"]}


def patch_of(snapshot):
    # Snapshots from before patch ids existed (2026-10-13 to 10-20) are all S5.
    return snapshot.get("patch") or f"S{snapshot['season']}{'-mid' if snapshot.get('is_midseason') else ''}"


def latest_per_patch():
    """The newest snapshot of every patch. Snapshots are cumulative since the
    patch started, so only the newest one of each patch may be counted."""
    latest = {}
    for path in snapshot_paths():
        snapshot = load_snapshot(path)
        latest[patch_of(snapshot)] = snapshot  # paths are date-sorted
    return latest


def to_slices(snapshot):
    """Per-hero slices shaped like data/raw/*_cache.json entries:
    {season, isMidseason, tier, region, measurements: [{map: {slug}, winRate, pickRate}]}.
    Overall (all-maps) rates and "--" cells are left out."""
    grouped = defaultdict(lambda: defaultdict(list))
    for s in snapshot["slices"]:
        if s["map"] == "all-maps":
            continue
        for hero, (win_rate, pick_rate) in s["rates"].items():
            if win_rate is None or pick_rate is None:
                continue
            grouped[hero][(s["tier"], s["region"])].append({"map": {"slug": s["map"]}, "winRate": win_rate, "pickRate": pick_rate})

    is_mid = snapshot.get("is_midseason", False)
    return {
        hero: [
            {"season": snapshot["season"], "isMidseason": is_mid, "tier": tier, "region": region, "measurements": ms}
            for (tier, region), ms in sorted(by_slice.items())
        ]
        for hero, by_slice in grouped.items()
    }

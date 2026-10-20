"""Everything the builders read, as {hero_slug: [slice, ...]} in the raw cache format.

- data/history/owtics.json.gz: frozen OWTics harvest of completed seasons.
- data/snapshots/: the newest daily snapshot of every patch since collection
  started (2026-10-13, Season 5). Older snapshots of a patch are already
  contained in its newest one.
"""
import gzip
import json
import os

import snapshots
from config import canonical_slug

HISTORY_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "history", "owtics.json.gz")


def load_history():
    with gzip.open(HISTORY_PATH, "rt", encoding="utf-8") as f:
        return {canonical_slug(h): slices for h, slices in json.load(f).items()}


def load_all():
    data = load_history()
    history_seasons = {s["season"] for slices in data.values() for s in slices}

    for snapshot in snapshots.latest_per_patch().values():
        if snapshot["season"] in history_seasons:
            raise RuntimeError(f"season {snapshot['season']} is in both the OWTics history and the snapshots; it would be double-counted")
        for hero, slices in snapshots.to_slices(snapshot).items():
            data.setdefault(canonical_slug(hero), []).extend(slices)
    return data

"""Freeze the OWTics harvest (data/raw/, local only) into data/history/owtics.json.gz.

Only completed periods go in. The season in progress comes from the daily
snapshots instead, so it isn't counted twice. Rerun this only after
re-harvesting OWTics, e.g. to backfill a period the collector missed.
"""
import gzip
import json
import os

from config import CURRENT_SEASON, canonical_slug

BASE = os.path.join(os.path.dirname(__file__), "..")
RAW_DIR = os.path.join(BASE, "data", "raw")
OUT_PATH = os.path.join(BASE, "data", "history", "owtics.json.gz")


def main():
    history = {}
    for fname in sorted(os.listdir(RAW_DIR)):
        if not fname.endswith("_cache.json"):
            continue
        with open(os.path.join(RAW_DIR, fname), encoding="utf-8") as f:
            slices = [s for s in json.load(f) if s["season"] < CURRENT_SEASON]
        if slices:
            history.setdefault(canonical_slug(fname.replace("_cache.json", "")), []).extend(slices)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with gzip.open(OUT_PATH, "wt", encoding="utf-8") as f:
        json.dump(history, f, separators=(",", ":"))

    count = sum(len(v) for v in history.values())
    print(f"wrote {OUT_PATH}: {len(history)} heroes, {count} slices, {os.path.getsize(OUT_PATH) // 1024} KB")


if __name__ == "__main__":
    main()

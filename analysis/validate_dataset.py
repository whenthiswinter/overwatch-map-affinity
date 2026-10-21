"""Sanity checks on data/web_data.json before it goes live.

The workflow runs this after build_dataset.py; a non-zero exit skips the
deploy, so the site keeps its last good version, and opens an issue. The
checks are deliberately loose: they catch a broken source or build (heroes
or maps vanishing, impossible values), not ordinary data movement.
"""
import json
import math
import os
import sys

from build_dataset import OUT_PATH, RANKS, REGIONS, tier_of

MIN_HEROES = 40
MIN_MAPS = 25
MIN_MAIN_VIEW_ENTRIES = 1000
ROLES = {"Tank", "Damage", "Support"}
MODES = {"Escort", "Hybrid", "Control", "Push", "Flashpoint"}


def check(data):
    problems = []

    def need(condition, message):
        if not condition:
            problems.append(message)

    meta = data.get("meta", {})
    for key in ("data_through", "patch", "season", "days_into_patch", "mature"):
        need(key in meta, f"meta.{key} missing")

    heroes, maps = data.get("hero_list", []), data.get("map_list", [])
    need(len(heroes) >= MIN_HEROES, f"only {len(heroes)} heroes (expected {MIN_HEROES}+)")
    need(len(maps) >= MIN_MAPS, f"only {len(maps)} maps (expected {MIN_MAPS}+)")
    missing_names = sorted(set(maps) - set(data.get("map_names", {})))
    need(not missing_names, f"maps without a display name: {missing_names}")
    bad_roles = {h: r for h, r in data.get("hero_roles", {}).items() if r not in ROLES}
    need(not bad_roles, f"unknown roles: {bad_roles}")
    bad_modes = {m: md for m, md in data.get("map_modes", {}).items() if md not in MODES}
    need(not bad_modes, f"unknown map modes: {bad_modes}")

    for scope in ("all", "patch"):
        combos = data.get("scopes", {}).get(scope, {})
        need(len(combos) == len(RANKS) * len(REGIONS), f"scope {scope}: {len(combos)} combos")
        for name, combo in combos.items():
            for e in combo.get("entries", []):
                where = f"{scope}/{name} {e.get('hero')}/{e.get('map')}"
                numbers = [e.get(k) for k in ("delta_wr", "raw_delta_wr", "pr_lift", "ci")]
                if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in numbers):
                    problems.append(f"{where}: non-numeric or infinite value")
                    continue
                need(e["tier"] == tier_of(e["delta_wr"]), f"{where}: tier {e['tier']} doesn't match {e['delta_wr']}")
                need(0 <= e.get("tier_p", -1) <= 100, f"{where}: tier probability {e.get('tier_p')}")
                need(e["ci"] > 0 and e.get("sample_size", 0) >= 1, f"{where}: ci/sample size")
                need(e["hero"] in heroes and e["map"] in maps, f"{where}: unknown hero or map")
            for hero, h in combo.get("heroes", {}).items():
                p = h.get("volatility_p")
                too_early = h.get("volatility_class", "").startswith("Too early")
                need(p is None if too_early else 0 <= (p if p is not None else -1) <= 100,
                     f"{scope}/{name} {hero}: sigma class probability {p}")

    main = data.get("scopes", {}).get("all", {}).get("ALL_ALL", {}).get("entries", [])
    need(len(main) >= MIN_MAIN_VIEW_ENTRIES, f"main view has only {len(main)} entries (expected {MIN_MAIN_VIEW_ENTRIES}+)")
    missing = sorted(set(heroes) - {e["hero"] for e in main})
    need(not missing, f"heroes with no entries in the main view: {missing}")
    return problems


def main():
    with open(OUT_PATH, encoding="utf-8") as f:
        problems = check(json.load(f))
    if problems:
        print(f"{len(problems)} problem(s) in {os.path.basename(OUT_PATH)}:")
        for p in problems[:50]:
            print(f"  - {p}")
        return 1
    print("web_data.json looks sane")
    return 0


if __name__ == "__main__":
    sys.exit(main())

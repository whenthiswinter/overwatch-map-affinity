"""Snapshots, the history/snapshot merge, patch labelling and roster tracking."""
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "analysis"))

import detect_patch  # noqa: E402
import snapshots  # noqa: E402
import sources  # noqa: E402


def snapshot(date, patch="S5", season=5, mid=False, rates=None, heroes=None, maps=None):
    rates = rates or {"ana": [50.0, 20.0]}
    return {
        "date": date, "patch": patch, "season": season, "is_midseason": mid,
        "heroes": heroes or {"ana": {"name": "Ana", "role": "Support"}},
        "maps": maps or {"dorado": {"name": "Dorado", "mode": "Escort"}},
        "slices": [
            {"region": "EU", "tier": "MASTER", "map": "all-maps", "rates": rates},
            {"region": "EU", "tier": "MASTER", "map": "dorado", "rates": {**rates, "mercy": [None, 3.0]}},
        ],
    }


class SnapshotTests(unittest.TestCase):
    def test_to_slices_skips_overall_rates_and_missing_cells(self):
        out = snapshots.to_slices(snapshot("2026-10-20"))
        self.assertEqual(list(out), ["ana"])
        (s,) = out["ana"]
        self.assertEqual((s["season"], s["isMidseason"], s["tier"], s["region"]), (5, False, "MASTER", "EU"))
        self.assertEqual([m["map"]["slug"] for m in s["measurements"]], ["dorado"])

    def test_patch_of_defaults_for_old_snapshots(self):
        old = snapshot("2026-10-13")
        del old["patch"]
        self.assertEqual(snapshots.patch_of(old), "S5")
        old["is_midseason"] = True
        self.assertEqual(snapshots.patch_of(old), "S5-mid")

    def test_latest_per_patch_keeps_only_the_newest(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(snapshots, "SNAPSHOT_DIR", tmp):
            for date, patch in [("2026-10-13", "S5"), ("2026-10-20", "S5"), ("2026-11-12", "S5-mid")]:
                snapshots.save_snapshot(os.path.join(tmp, f"{date}.json.gz"), snapshot(date, patch=patch))
            latest = snapshots.latest_per_patch()
            self.assertEqual({p: s["date"] for p, s in latest.items()}, {"S5": "2026-10-20", "S5-mid": "2026-11-12"})


class SourcesTests(unittest.TestCase):
    def test_a_season_in_both_history_and_snapshots_is_refused(self):
        history = {"ana": [{"season": 5, "isMidseason": False, "tier": "MASTER", "region": "EU", "measurements": []}]}
        with mock.patch.object(sources, "load_history", return_value=history), \
             mock.patch.object(sources.snapshots, "latest_per_patch", return_value={"S5": snapshot("2026-10-20")}):
            with self.assertRaises(RuntimeError):
                sources.load_all()


class PatchLabelTests(unittest.TestCase):
    STATE = {"current": "S5", "patches": [{"id": "S5", "season": 5, "is_midseason": False, "started": "2026-10-06"}]}
    CURRENT = STATE["patches"][0]

    def label(self, notes, state=None):
        return detect_patch.label_new_patch(state or self.STATE, self.CURRENT, "2026-11-12", notes)[0]

    def test_season_heading_starts_a_new_season(self):
        p = self.label([("2026-11-11", "season", 6, "Season 6: Something")])
        self.assertEqual((p["id"], p["season"], p["is_midseason"], p["started"]), ("S6", 6, False, "2026-11-11"))

    def test_midseason_heading_starts_the_midseason(self):
        p = self.label([("2026-11-11", "midseason", None, "Mid-Season Patch")])
        self.assertEqual((p["id"], p["season"], p["is_midseason"]), ("S5-mid", 5, True))

    def test_no_notes_means_another_reset_in_the_same_half(self):
        self.assertEqual(self.label([])["id"], "S5-2")
        state = {"current": "S5-2", "patches": self.STATE["patches"] + [{"id": "S5-2", "season": 5, "is_midseason": False, "started": "2026-10-30"}]}
        self.assertEqual(self.label([], state)["id"], "S5-3")

    def test_old_notes_are_ignored(self):
        self.assertEqual(self.label([("2026-10-06", "season", 5, "Season 5")])["id"], "S5-2")

    def test_shift_tells_a_reset_from_a_normal_refresh(self):
        a = snapshot("2026-10-20", rates={"ana": [50.0, 20.0], "mercy": [48.0, 15.0]})
        small = snapshot("2026-10-22", rates={"ana": [50.3, 20.1], "mercy": [48.2, 15.1]})
        reset = snapshot("2026-11-12", rates={"ana": [44.0, 26.0], "mercy": [53.0, 9.0]})
        pr, wr = detect_patch.shift(small, a)
        self.assertLess(pr, detect_patch.RESET_PR_SHIFT)
        self.assertLess(wr, detect_patch.RESET_MAP_WR_SHIFT)
        pr, wr = detect_patch.shift(reset, a)
        self.assertGreaterEqual(pr, detect_patch.RESET_PR_SHIFT)
        self.assertGreaterEqual(wr, detect_patch.RESET_MAP_WR_SHIFT)


class RosterTests(unittest.TestCase):
    def run_roster(self, newest, previous, history=({"ana"}, {"dorado"}), state=None):
        state = state if state is not None else {}
        with tempfile.TemporaryDirectory() as tmp:
            paths = []
            for s in (previous, newest):
                path = os.path.join(tmp, f"{s['date']}.json.gz")
                snapshots.save_snapshot(path, s)
                paths.append(path)
            with mock.patch.object(detect_patch, "history_roster", return_value=history):
                problems = detect_patch.update_roster(state, newest, paths, set())
        return state, problems

    def test_new_hero_and_map_are_recorded_once(self):
        heroes = {"ana": {"name": "Ana", "role": "Support"}, "newbie": {"name": "Newbie", "role": "Tank"}}
        maps = {"dorado": {"name": "Dorado", "mode": "Escort"}, "newmap": {"name": "New Map", "mode": "Push"}}
        prev = snapshot("2026-11-11", season=6)
        new = snapshot("2026-11-12", patch="S6", season=6, heroes=heroes, maps=maps)
        state, problems = self.run_roster(new, prev)
        self.assertEqual(state["first_seen"], {"heroes": {"newbie": 6}, "maps": {"newmap": 6}})
        self.assertEqual(len(problems), 2)
        _, again = self.run_roster(new, prev, state=state)
        self.assertEqual(again, [])

    def test_role_change_is_flagged_as_a_rework(self):
        prev = snapshot("2026-11-11", heroes={"ana": {"name": "Ana", "role": "Damage"}})
        new = snapshot("2026-11-12", heroes={"ana": {"name": "Ana", "role": "Support"}})
        _, problems = self.run_roster(new, prev)
        self.assertEqual(len(problems), 1)
        self.assertIn("changed role", problems[0])


if __name__ == "__main__":
    unittest.main()

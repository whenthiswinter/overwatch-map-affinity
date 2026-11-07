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


def note(date, heading="Hotfix Update", season=None, hero_updates=0):
    return {"date": date, "heading": heading, "season": season, "hero_updates": hero_updates}


S5_CALENDAR = [{"season": 5, "start": "2026-10-07", "end": "2026-12-08"}]


class PatchLabelTests(unittest.TestCase):
    S5 = {"id": "S5", "season": 5, "is_midseason": False, "started": "2026-10-06"}
    S5_MID = {"id": "S5-mid", "season": 5, "is_midseason": True, "started": "2026-11-09"}

    def label(self, current, reset="2026-11-10", notes=None, homepage=None, calendar=None):
        state = {"current": current["id"], "patches": [current]}
        signals = {"notes": notes or [], "homepage": homepage, "calendar": calendar}
        return detect_patch.label_new_patch(state, current, reset, signals)

    def test_season_heading_starts_a_new_season(self):
        p, _, ok = self.label(self.S5_MID, "2026-12-09", notes=[note("2026-12-08", "Season 6: Something", season=6, hero_updates=40)])
        self.assertEqual((p["id"], p["season"], p["is_midseason"], p["started"], ok), ("S6", 6, False, "2026-12-08", True))

    def test_homepage_alone_is_enough_for_a_new_season(self):
        p, reasons, ok = self.label(self.S5_MID, "2026-12-09", homepage=6)
        self.assertEqual((p["id"], ok), ("S6", True))
        self.assertIn("homepage", reasons[0])

    def test_calendar_start_near_the_reset_means_a_new_season(self):
        calendar = S5_CALENDAR + [{"season": 6, "start": "2026-12-09", "end": "2027-02-09"}]
        p, _, _ = self.label(self.S5_MID, "2026-12-10", calendar=calendar)
        self.assertEqual(p["id"], "S6")

    def test_disagreeing_season_numbers_are_unconfirmed(self):
        p, _, ok = self.label(self.S5_MID, "2026-12-09", notes=[note("2026-12-08", "Season 6", season=6)], homepage=7)
        self.assertEqual((p["id"], ok), ("S7", False))

    def test_big_patch_in_a_first_half_is_the_midseason(self):
        # S4's midseason notes opened with an event name, not "midseason".
        p, reasons, ok = self.label(self.S5, notes=[note("2026-11-09", "Junkrat's Loot Hunt", hero_updates=27)])
        self.assertEqual((p["id"], p["is_midseason"], p["started"], ok), ("S5-mid", True, "2026-11-09", True))
        self.assertIn("27 hero changes", reasons[0])

    def test_calendar_midpoint_confirms_the_midseason(self):
        p, reasons, ok = self.label(self.S5, "2026-11-08", calendar=S5_CALENDAR)
        self.assertEqual((p["id"], ok), ("S5-mid", True))
        self.assertIn("middle of Season 5", reasons[0])

    def test_unsupported_midseason_is_flagged_unconfirmed(self):
        p, _, ok = self.label(self.S5, "2026-10-20", notes=[note("2026-10-13", hero_updates=5)], calendar=S5_CALENDAR)
        self.assertEqual((p["id"], ok), ("S5-mid", False))

    def test_a_second_reset_in_a_midseason_is_a_sub_patch(self):
        p, _, ok = self.label(self.S5_MID, "2026-11-25")
        self.assertEqual((p["id"], p["season"], p["is_midseason"], ok), ("S5-mid-2", 5, True, False))

    def test_notes_from_before_the_current_patch_are_ignored(self):
        p, _, _ = self.label(self.S5_MID, "2026-11-25", notes=[note("2026-10-06", "Season 5", season=5, hero_updates=46)])
        self.assertEqual(p["id"], "S5-mid-2")

    def test_parse_patch_notes(self):
        page = ('<div class="PatchNotes-patch PatchNotes-live"><div class="anchor" id="patch-2026-10-06"></div>'
                '<h4 class="PatchNotes-sectionTitle">Reign of Talon - Season 5: A Grim Doctrine</h4>'
                '<div class="PatchNotesHeroUpdate-name">Ana</div><div class="PatchNotesHeroUpdate-name">Mei</div></div>'
                '<div class="PatchNotes-patch"><div class="anchor" id="patch-2026-10-13"></div>'
                '<h4 class="PatchNotes-sectionTitle">Hotfix Update</h4></div>')
        out = detect_patch.parse_patch_notes(page)
        self.assertEqual(out[0], {"date": "2026-10-06", "heading": "Reign of Talon - Season 5: A Grim Doctrine", "season": 5, "hero_updates": 2})
        self.assertEqual((out[1]["season"], out[1]["hero_updates"]), (None, 0))

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


def with_korea(snap, wr=48.0):
    snap["slices"].append({"region": "KOREA", "tier": "MASTER", "map": "dorado", "rates": {"ana": [wr, 20.0]}})
    return snap


class KoreaFallbackTests(unittest.TestCase):
    """Nexon refuses some GitHub runners; Korea may be missing from a snapshot."""

    def test_missing_korea_comes_from_the_same_patch_only(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(snapshots, "SNAPSHOT_DIR", tmp):
            days = [(with_korea(snapshot("2026-11-02"), 47.0)), with_korea(snapshot("2026-11-03"), 49.0),
                    snapshot("2026-11-04"),  # S5, Korea refused
                    snapshot("2026-11-07", patch="S5-mid", mid=True)]  # new patch, Korea refused
            for s in days:
                snapshots.save_snapshot(os.path.join(tmp, f"{s['date']}.json.gz"), s)
            latest = snapshots.latest_per_patch()
        s5, mid = latest["S5"], latest["S5-mid"]
        self.assertEqual((s5["date"], s5["korea_date"]), ("2026-11-04", "2026-11-03"))
        (kr,) = [s for s in s5["slices"] if s["region"] == "KOREA"]
        self.assertEqual(kr["rates"]["ana"][0], 49.0)  # the newest Korea, not an older one
        self.assertIsNone(mid["korea_date"])  # never borrowed across the reset
        self.assertFalse(snapshots.has_korea(mid))

    def run_collector(self, tmp, nexon_ok):
        import collect_live
        nexon = (lambda rq, maps: ([{"region": "KOREA", "tier": "MASTER", "map": "dorado", "rates": {"ana": [50.0, 9.0]}}], [])) if nexon_ok \
            else mock.Mock(side_effect=RuntimeError("HTTP Error 403"))
        with mock.patch.multiple(collect_live, SNAPSHOT_DIR=tmp, log=mock.Mock(), note_run=mock.Mock(),
                                 blizzard_filters=mock.Mock(return_value=("2", {"dorado": {"name": "Dorado", "mode": "Escort"}})),
                                 collect_blizzard=mock.Mock(return_value=[{"region": "EU", "tier": "MASTER", "map": "dorado", "rates": {"ana": [51.0, 9.0]}}]),
                                 nexon_rq=mock.Mock(return_value="2"), collect_nexon=nexon,
                                 current_patch=mock.Mock(return_value={"id": "S5-mid", "season": 5, "is_midseason": True})):
            return collect_live.main(), collect_live.collect_blizzard.call_count

    def test_collector_saves_without_korea_then_adds_it_later(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _ = self.run_collector(tmp, nexon_ok=False)
            (name,) = os.listdir(tmp)
            saved = snapshots.load_snapshot(os.path.join(tmp, name))
            self.assertEqual(code, 0)
            self.assertFalse(snapshots.has_korea(saved))
            self.assertEqual(saved["sources"]["nexon"]["status"], "failed")

            code, blizzard_calls = self.run_collector(tmp, nexon_ok=True)  # a later run the same day
            saved = snapshots.load_snapshot(os.path.join(tmp, name))
            self.assertEqual(code, 0)
            self.assertEqual(blizzard_calls, 0)  # Blizzard isn't fetched again
            self.assertTrue(snapshots.has_korea(saved))
            self.assertEqual(saved["sources"]["nexon"]["status"], "ok")
            self.assertEqual(len(saved["slices"]), 2)

    def test_stale_korea_is_reported_once(self):
        state = {"current": "S5-mid", "patches": [{"id": "S5-mid", "started": "2026-11-03"}]}
        notified = set()
        self.assertIsNone(detect_patch.korea_stale(state, "2026-11-08", "2026-11-07", notified))  # a day behind: normal
        self.assertIn("Korea data is behind", detect_patch.korea_stale(state, "2026-11-09", "2026-11-07", notified))
        self.assertIsNone(detect_patch.korea_stale(state, "2026-11-10", "2026-11-07", notified))  # already reported
        self.assertIsNotNone(detect_patch.korea_stale(state, "2026-11-06", None, set()))  # none since the reset

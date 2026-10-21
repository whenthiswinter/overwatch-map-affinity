"""Validity periods, provisional/maturity rules, slugs and the label functions."""
import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "analysis"))

import build_dataset as bd  # noqa: E402
import config  # noqa: E402


def rules(current_period=5, mature=False, heroes=None, maps=None, first_seen=None):
    """Patch the module-level state the rule functions read."""
    return mock.patch.multiple(
        config,
        CURRENT_PERIOD=current_period,
        CURRENT_PATCH_MATURE=mature,
        HERO_VALID_FROM_SEASON=heroes or {},
        MAP_VALID_FROM_SEASON=maps or {},
        FIRST_SEEN=first_seen or {"heroes": {}, "maps": {}},
    )


class ValidityTests(unittest.TestCase):
    def test_period_puts_midseason_halfway(self):
        self.assertEqual(config.period(5), 5)
        self.assertEqual(config.period(5, True), 5.5)

    def test_valid_from_prefers_config_then_first_seen(self):
        with rules(heroes={"sombra": 5}, first_seen={"heroes": {"sombra": 3, "newbie": 6}, "maps": {"newmap": 6}}):
            self.assertEqual(config.hero_valid_from("sombra"), 5)
            self.assertEqual(config.hero_valid_from("newbie"), 6)
            self.assertEqual(config.hero_valid_from("ana"), 1)
            self.assertEqual(config.valid_from("ana", "newmap"), 6)

    def test_slices_before_valid_from_never_count(self):
        with rules(heroes={"sombra": 5}):
            self.assertFalse(config.season_usable("sombra", "dorado", 4, True))

    def test_immature_current_patch_only_counts_for_new_pairs(self):
        with rules(current_period=5, mature=False, heroes={"doctrine": 5}):
            self.assertFalse(config.season_usable("ana", "dorado", 5))
            self.assertTrue(config.season_usable("doctrine", "dorado", 5))
            self.assertTrue(config.is_provisional("doctrine", "dorado"))
            self.assertFalse(config.is_provisional("ana", "dorado"))

    def test_mature_patch_counts_for_everyone(self):
        with rules(current_period=5, mature=True, heroes={"doctrine": 5}):
            self.assertTrue(config.season_usable("ana", "dorado", 5))
            self.assertFalse(config.is_provisional("doctrine", "dorado"))

    def test_finished_first_half_counts_during_midseason(self):
        with rules(current_period=5.5, mature=False):
            self.assertTrue(config.season_usable("ana", "dorado", 5, False))
            self.assertFalse(config.season_usable("ana", "dorado", 5, True))

    def test_patch_scope_is_current_period_only(self):
        with rules(current_period=5):
            self.assertTrue(config.in_current_patch("ana", "dorado", 5))
            self.assertFalse(config.in_current_patch("ana", "dorado", 4, True))

    def test_tidy_name_fixes_blizzards_odd_cases(self):
        cases = [("NEON JUNCTION", "Neon Junction"), ("Circuit royal", "Circuit Royal"), ("King's Row", "King's Row"),
                 ("Watchpoint: Gibraltar", "Watchpoint: Gibraltar"), ("Paraíso", "Paraíso"), ("temple of anubis", "Temple of Anubis")]
        for raw, tidy in cases:
            self.assertEqual(config.tidy_name(raw), tidy, raw)

    def test_canonical_slug_aliases(self):
        for raw, slug in [("Soldier: 76", "soldier-76"), ("soldier76", "soldier-76"), ("D.Mon", "dmon"),
                          ("jetpackcat", "jetpack-cat"), ("Lúcio", "lucio"), ("wrecking_ball", "wrecking-ball")]:
            self.assertEqual(config.canonical_slug(raw), slug, raw)


class LabelTests(unittest.TestCase):
    def test_tier_lines(self):
        cases = [(3.0, "S"), (2.99, "A"), (1.2, "A"), (1.19, "B"), (-1.2, "B"), (-1.21, "C"), (-3.0, "C"), (-3.01, "D")]
        for delta, tier in cases:
            self.assertEqual(bd.tier_of(delta), tier, delta)

    def test_presence_lines(self):
        cases = [(50, "Map Priority"), (49, "Popular"), (20, "Popular"), (19, "Standard"), (-19, "Standard"), (-20, "Niche")]
        for lift, label in cases:
            self.assertTrue(bd.presence_label(lift).startswith(label), (lift, bd.presence_label(lift)))

    def test_archetype_grid(self):
        cases = [((2.0, 30), "Meta"), ((2.0, -30), "Specialist"), ((2.0, 0), "Favorable"),
                 ((-2.0, 30), "Trap Pick"), ((-2.0, -30), "Deterrent"), ((-2.0, 0), "Unfavorable"),
                 ((0.0, 80), "Neutral"), ((0.0, -80), "Neutral")]
        for (wr, lift), archetype in cases:
            self.assertEqual(bd.archetype_of(wr, lift), archetype, (wr, lift))

    def test_tier_probability(self):
        far_inside = bd.tier_probability(0.0, se2=0.01, tau2=4.0)
        on_the_edge = bd.tier_probability(1.2, se2=1.0, tau2=4.0)
        self.assertGreater(far_inside, 0.99)
        self.assertAlmostEqual(on_the_edge, 0.5, delta=0.05)
        for x in (-10, -3, -1, 0, 1, 2.5, 3, 10):
            p = bd.tier_probability(x, se2=2.0, tau2=0.0)
            self.assertTrue(0.0 <= p <= 1.0)

    def test_volatility_classes(self):
        self.assertTrue(bd.volatility_class(3.0, False).startswith("Map-Dependent"))
        self.assertTrue(bd.volatility_class(1.2, False).startswith("Flexible"))
        self.assertTrue(bd.volatility_class(1.19, False).startswith("Map-Agnostic"))
        self.assertTrue(bd.volatility_class(9.0, True).startswith("Too early"))


if __name__ == "__main__":
    unittest.main()

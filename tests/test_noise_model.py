"""The noise model's pieces, and build_scope end to end on synthetic data."""
import os
import random
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "analysis"))

import build_dataset as bd  # noqa: E402
import config  # noqa: E402

MAPS = ["dorado", "havana", "ilios", "nepal", "oasis", "busan", "numbani", "midtown"]


def synthetic_raw(true_effects, slice_noise=2.0, seed=0):
    """hero -> slices in the raw cache format, 4 seasons x 2 halves x 2 tiers x 2 regions.
    Win rates are 50 + true effect + noise; pick rates are equal, so the baseline is ~50."""
    rng = random.Random(seed)
    raw = {}
    for hero, effects in true_effects.items():
        slices = []
        for season in (1, 2, 3, 4):
            for mid in (False, True):
                for tier in ("MASTER", "GRANDMASTER_AND_CHAMPION"):
                    for region in ("AMER", "EU"):
                        ms = [{"map": {"slug": m}, "winRate": 50 + effects[m] + rng.gauss(0, slice_noise), "pickRate": 10.0} for m in MAPS]
                        slices.append({"season": season, "isMidseason": mid, "tier": tier, "region": region, "measurements": ms})
        raw[hero] = slices
    return raw


class PieceTests(unittest.TestCase):
    def test_pooled_variance_needs_enough_data(self):
        self.assertIsNone(bd.pooled_variance([[1.0, 2.0], [3.0]]))
        self.assertAlmostEqual(bd.pooled_variance([[0, 2, 4], [10, 12, 14], [1, 3, 5]]), 4.0)

    def test_pair_noise_falls_back_to_pooled_for_one_slice(self):
        self.assertAlmostEqual(bd.pair_noise([3.0], pooled=8.0), 8.0)
        self.assertLess(bd.pair_noise([1, 2, 3, 4, 5, 6, 7, 8], pooled=8.0), 8.0)

    def test_signal_variance_subtracts_noise_and_never_goes_negative(self):
        self.assertAlmostEqual(bd.signal_variance([-2.0, 2.0], [1.0, 1.0]), 3.0)
        self.assertEqual(bd.signal_variance([0.1, -0.1], [5.0, 5.0]), 0.0)


@mock.patch.multiple(config, CURRENT_PERIOD=5, CURRENT_PATCH_MATURE=False,
                     HERO_VALID_FROM_SEASON={}, MAP_VALID_FROM_SEASON={}, FIRST_SEEN={"heroes": {}, "maps": {}})
class BuildScopeTests(unittest.TestCase):
    def build(self, raw):
        return bd.build_scope(raw, config.season_usable, flag_provisional=True)

    def test_every_combo_and_pair_is_built(self):
        raw = synthetic_raw({"ana": dict(zip(MAPS, [4, -4, 2, -2, 0, 1, -1, 0]))})
        combos = self.build(raw)
        self.assertEqual(len(combos), len(bd.RANKS) * len(bd.REGIONS))
        self.assertEqual(len(combos["ALL_ALL"]["entries"]), len(MAPS))

    def test_adjusted_values_sit_between_raw_and_hero_mean(self):
        raw = synthetic_raw({"ana": dict(zip(MAPS, [4, -4, 2, -2, 0, 1, -1, 0]))}, slice_noise=6.0)
        entries = self.build(raw)["ALL_ALL"]["entries"]
        mean = sum(e["raw_delta_wr"] for e in entries) / len(entries)
        for e in entries:
            lo, hi = sorted((mean, e["raw_delta_wr"]))
            self.assertTrue(lo - 0.01 <= e["delta_wr"] <= hi + 0.01, e)
            self.assertTrue(0 <= e["tier_p"] <= 100)
            self.assertGreater(e["ci"], 0)

    def test_real_effects_survive_and_flat_heroes_flatten(self):
        raw = synthetic_raw({
            "widowmaker": dict(zip(MAPS, [12, -12, 8, -8, 0, 4, -4, 0])),
            "zenyatta": dict.fromkeys(MAPS, 0.0),
        })
        combos = self.build(raw)["ALL_ALL"]
        widow = {e["map"]: e for e in combos["entries"] if e["hero"] == "widowmaker"}
        self.assertEqual(widow["dorado"]["tier"], "S")
        self.assertEqual(widow["havana"]["tier"], "D")
        self.assertTrue(all(e["tier"] == "B" for e in combos["entries"] if e["hero"] == "zenyatta"))
        self.assertGreater(combos["heroes"]["widowmaker"]["volatility"], combos["heroes"]["zenyatta"]["volatility"])


if __name__ == "__main__":
    unittest.main()

"""The noise model's pieces, and build_scope end to end on synthetic data."""
import os
import random
import sys
import unittest
from fractions import Fraction
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "analysis"))

import build_dataset as bd  # noqa: E402
import config  # noqa: E402

MAPS = ["dorado", "havana", "ilios", "nepal", "oasis", "busan", "numbani", "midtown"]


def synthetic_raw(true_effects, slice_noise=2.0, seed=0, outlier_share=0.0, outlier_size=40.0):
    """hero -> slices in the raw cache format, 4 seasons x 2 halves x 2 tiers x 2 regions.
    Win rates are 50 + true effect + noise; pick rates are equal, so the baseline is ~50.
    A share of measurements can be wild outliers of +-outlier_size."""
    rng = random.Random(seed)

    def noise():
        if rng.random() < outlier_share:
            return rng.choice((-1, 1)) * outlier_size
        return rng.gauss(0, slice_noise)

    raw = {}
    for hero, effects in true_effects.items():
        slices = []
        for season in (1, 2, 3, 4):
            for mid in (False, True):
                for tier in ("MASTER", "GRANDMASTER_AND_CHAMPION"):
                    for region in ("AMER", "EU"):
                        ms = [{"map": {"slug": m}, "winRate": 50 + effects[m] + noise(), "pickRate": 10.0} for m in MAPS]
                        slices.append({"season": season, "isMidseason": mid, "tier": tier, "region": region, "measurements": ms})
        raw[hero] = slices
    return raw


class PieceTests(unittest.TestCase):
    def test_trimmed_mean_drops_the_extremes(self):
        self.assertAlmostEqual(bd.trimmed_mean([1, 2, 3, 4, 100]), 3.0)
        self.assertAlmostEqual(bd.trimmed_mean([1, 2, 6]), 3.0)  # too few slices to trim

    def test_winsorized_variance_clips_the_extremes(self):
        self.assertAlmostEqual(bd.winsorized_variance([1, 2, 3, 4, 100]), 1.0)  # [2, 2, 3, 4, 4]
        self.assertAlmostEqual(bd.winsorized_variance([0, 2, 4]), 4.0)

    def test_pair_noise_scales_for_the_trimmed_slices(self):
        # winsorized variance 1, pooled 1 -> var 1; 3 of 5 slices kept -> 1 * 4 / (3 * 2)
        self.assertAlmostEqual(bd.pair_noise([1, 2, 3, 4, 100], lambda share: 1.0), 2 / 3)
        # nothing trimmed -> the plain variance / n
        self.assertAlmostEqual(bd.pair_noise([0, 2, 4], lambda share: 4.0), 4 / 3)

    def test_pooled_variance_needs_enough_data(self):
        self.assertIsNone(bd.pooled_variance([[1.0, 2.0], [3.0]], share=0))
        self.assertAlmostEqual(bd.pooled_variance([[0, 2, 4], [10, 12, 14], [1, 3, 5]], share=0), 4.0)

    def test_pooled_variance_matches_the_pairs_trim_share(self):
        pairs = [[1, 2, 3, 4, 100], [1, 2, 3, 4, 100]]
        self.assertAlmostEqual(bd.pooled_variance(pairs, share=Fraction(1, 5)), 1.0)  # outlier clipped
        self.assertGreater(bd.pooled_variance(pairs, share=0), 1000)  # untrimmed pairs see it
        # a 3-slice pair trims nothing, so it borrows the plain (share 0) variance
        seen = []
        bd.pair_noise([1, 2, 3], lambda share: seen.append(share) or 1.0)
        self.assertEqual(seen, [0])

    def test_pair_noise_falls_back_to_pooled_for_one_slice(self):
        self.assertAlmostEqual(bd.pair_noise([3.0], lambda share: 8.0), 8.0)
        self.assertLess(bd.pair_noise([1, 2, 3, 4, 5, 6, 7, 8], lambda share: 8.0), 8.0)

    def test_map_sensitivity_borrows_from_other_heroes(self):
        rng = random.Random(5)
        evidence = {}
        for i, sd in enumerate([1.0, 1.5, 2.0, 2.5, 3.0, 1.2, 1.8, 2.2]):
            evidence[f"h{i}"] = ([rng.gauss(0, sd) for _ in range(30)], [0.2] * 30)
        evidence["flat"] = ([rng.gauss(0, 0.3) for _ in range(30)], [1.0] * 30)  # spread below its noise
        evidence["huge"] = ([rng.gauss(0, 7.0) for _ in range(30)], [0.2] * 30)
        tau2, typical, class_p = bd.map_sensitivity(evidence)
        # the old estimate (observed variance - noise) would be negative -> 0
        self.assertGreater(tau2["flat"], 0.0)
        self.assertLess(tau2["flat"], typical)
        # a precisely measured hero keeps (roughly) its own spread
        obs = sum((m - sum(evidence["huge"][0]) / 30) ** 2 for m in evidence["huge"][0]) / 30 - 0.2
        self.assertAlmostEqual(tau2["huge"] / obs, 1.0, delta=0.25)
        self.assertEqual(bd.map_sensitivity({}), ({}, 0.0, {}))
        # far from a class line -> sure of the class; the flat hero is near 0, far below 1.2
        self.assertGreater(class_p["huge"], 0.95)
        self.assertGreater(class_p["flat"], 0.9)
        self.assertTrue(all(0 <= p <= 1 for p in class_p.values()))


@mock.patch.multiple(config, CURRENT_PERIOD=5, CURRENT_PATCH_MATURE=False,
                     HERO_VALID_FROM_SEASON={}, MAP_VALID_FROM_SEASON={}, FIRST_SEEN={"heroes": {}, "maps": {}})
class BuildScopeTests(unittest.TestCase):
    def build(self, raw):
        return bd.build_scope(raw, config.season_usable, flag_provisional=True)[0]

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

    def test_narrow_filters_borrow_map_sensitivity_from_the_all_view(self):
        raw = synthetic_raw({
            "widowmaker": dict(zip(MAPS, [12, -12, 8, -8, 0, 4, -4, 0])),
            "zenyatta": dict.fromkeys(MAPS, 0.0),
        }, slice_noise=6.0)
        combos = self.build(raw)
        for hero in ("widowmaker", "zenyatta"):
            self.assertEqual(combos["MASTER_EU"]["heroes"][hero]["volatility"], combos["ALL_ALL"]["heroes"][hero]["volatility"])
        narrow = {e["map"]: e for e in combos["MASTER_EU"]["entries"] if e["hero"] == "widowmaker"}
        self.assertGreater(narrow["dorado"]["delta_wr"] - narrow["havana"]["delta_wr"], 15)

    def test_outlier_slices_do_not_hide_real_effects(self):
        # A few wild slices per pair (like Lifeweaver's +43 on King's Row) used
        # to swamp the noise estimate and flatten every map to the same value.
        raw = synthetic_raw({"lifeweaver": dict(zip(MAPS, [5, -5, 3, -3, 0, 2, -2, 0]))},
                            outlier_share=0.1, seed=3)
        combos = self.build(raw)["ALL_ALL"]
        life = {e["map"]: e for e in combos["entries"]}
        self.assertGreater(life["dorado"]["delta_wr"] - life["havana"]["delta_wr"], 7)
        self.assertGreater(combos["heroes"]["lifeweaver"]["volatility"], 2)


if __name__ == "__main__":
    unittest.main()

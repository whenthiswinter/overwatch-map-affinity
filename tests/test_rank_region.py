"""The rank/region test's statistic and its shuffle null."""
import os
import sys
import unittest

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "analysis"))

import check_rank_region as crr  # noqa: E402


class ShuffleTests(unittest.TestCase):
    def test_shuffle_keeps_each_stratums_labels(self):
        rng = np.random.default_rng(0)
        strata = np.array([3, 1, 3, 1, 1, 2, 3, 2])
        labels = np.array([0, 1, 2, 3, 4, 5, 6, 7])
        stable = np.argsort(strata, kind="stable")
        seen = set()
        for _ in range(50):
            out = crr.shuffle_within(labels, strata, stable, rng)
            for s in set(strata.tolist()):
                self.assertEqual(sorted(out[strata == s]), sorted(labels[strata == s]))
            seen.add(tuple(out))
        self.assertGreater(len(seen), 1)  # it does shuffle


class SplitHalfTests(unittest.TestCase):
    def rows(self, gaps_first, gaps_mid):
        """Each pair-half: 2 inside slices at +gap/2 and 2 outside at -gap/2."""
        ph, delta, inside = [], [], []
        for pid, (a, b) in enumerate(zip(gaps_first, gaps_mid)):
            for half, g in ((0, a), (1, b)):
                for side in (True, True, False, False):
                    ph.append(2 * pid + half)
                    delta.append(g / 2 if side else -g / 2)
                    inside.append(side)
        return {"ph": np.array(ph), "delta": np.array(delta, dtype=float), "pairs": len(gaps_first)}, np.array(inside)

    def test_gaps_that_repeat_correlate(self):
        rows, inside = self.rows([1, 2, 3, 4], [1.1, 2.2, 2.9, 4.1])
        r, n = crr.split_half(rows, inside)
        self.assertEqual(n, 4)
        self.assertGreater(r, 0.95)

    def test_pairs_with_too_few_slices_are_skipped(self):
        rows, inside = self.rows([1, 2, 3, 4], [1, 2, 3, 4])
        inside[:2] = False  # pair 0, first half: no inside slices left
        r, n = crr.split_half(rows, inside)
        self.assertEqual(n, 3)


if __name__ == "__main__":
    unittest.main()

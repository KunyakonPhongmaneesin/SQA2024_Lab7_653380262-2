# test_count_clump.py
import unittest
from count_clump import CountClump

class TestCountClump(unittest.TestCase):

    def test_none(self):
        self.assertEqual(CountClump.count_clumps(None), 0)

    def test_empty_list(self):
        self.assertEqual(CountClump.count_clumps([]), 0)

    def test_no_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 4, 5]), 0)

    def test_single_clump_start(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 3, 4, 5]), 1)

    def test_single_clump_middle(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3, 4]), 1)

    def test_consecutive_clump(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 2, 3]), 1)

    def test_long_consecutive_clump(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 2, 2, 3]), 1)

    def test_all_same(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 1, 1, 1]), 1)

    def test_clump_end(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 4, 4]), 1)

    def test_clump_end_with_diff(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 4, 5, 5]), 1)

    def test_multiple_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3, 3, 4, 4, 4, 1]), 3)

if __name__ == '__main__':
    unittest.main()

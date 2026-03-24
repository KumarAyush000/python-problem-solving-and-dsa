import unittest
from leet import Solution

# -------------------------------
# Tests for removeDuplicates
# -------------------------------
"""
class TestRemoveDuplicates(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_case_1(self):
        self.assertEqual(
            self.obj.removeDuplicates([1, 2, 2, 3, 1, 4]),
            [1, 2, 3, 4]
        )

    def test_case_2(self):
        self.assertEqual(
            self.obj.removeDuplicates([5, 5, 5]),
            [5]
        )

    def test_empty(self):
        self.assertEqual(
            self.obj.removeDuplicates([]),
            []
        )
"""

# -------------------------------
# Tests for countFrequency
# -------------------------------
class TestCountFrequency(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_case_1(self):
        self.assertEqual(
            self.obj.countFrequency([1, 2, 2, 3]),
            {1: 1, 2: 2, 3: 1}
        )

    def test_empty(self):
        self.assertEqual(
            self.obj.countFrequency([]),
            {}
        )


if __name__ == "__main__":
    unittest.main()
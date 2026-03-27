import unittest
from leet import Solution

"""
# -------------------------------
# Tests for removeDuplicates
# -------------------------------
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
"""
"""
# -------------------------------
# Test for filterEmails
# -------------------------------
class TestFilterEmails(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_valid_emails(self):
        emails = [
            "test@gmail.com",
            "hello@yahoo.in",
            "user.name@domain.org"
        ]
        expected = [
            "test@gmail.com",
            "hello@yahoo.in",
            "user.name@domain.org"
        ]
        self.assertEqual(self.obj.filterEmails(emails), expected)

    def test_invalid_emails(self):
        emails = [
            "invalid-email",
            "abc@.com",
            "@gmail.com",
            "test@gmail",
            "test@domain.c"   # too short extension
        ]
        self.assertEqual(self.obj.filterEmails(emails), [])

    def test_mixed_emails(self):
        emails = [
            "test@gmail.com",
            "invalid-email",
            "hello@yahoo.in",
            "abc@.com"
        ]
        expected = [
            "test@gmail.com",
            "hello@yahoo.in"
        ]
        self.assertEqual(self.obj.filterEmails(emails), expected)

    def test_empty_list(self):
        self.assertEqual(self.obj.filterEmails([]), [])
"""
# -------------------------------
# Test for maxValueRecord
# -------------------------------
class TestMaxValueRecord(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # Normal case
    def test_normal_case(self):
        records = [
            {"id": 1, "value": 10},
            {"id": 2, "value": 50},
            {"id": 3, "value": 30}
        ]
        self.assertEqual(self.sol.maxValueRecord(records), {"id": 2, "value": 50})

    # Single element
    def test_single_record(self):
        records = [{"id": 1, "value": 100}]
        self.assertEqual(self.sol.maxValueRecord(records), {"id": 1, "value": 100})

    # Empty list
    def test_empty_list(self):
        self.assertEqual(self.sol.maxValueRecord([]), {})

    # Missing 'value' key
    def test_missing_value_key(self):
        records = [
            {"id": 1},
            {"id": 2, "value": 20}
        ]
        self.assertEqual(self.sol.maxValueRecord(records), {"id": 2, "value": 20})

    # Negative values
    def test_negative_values(self):
        records = [
            {"id": 1, "value": -10},
            {"id": 2, "value": -5}
        ]
        self.assertEqual(self.sol.maxValueRecord(records), {"id": 2, "value": -5})

    # Duplicate max values
    def test_duplicate_max(self):
        records = [
            {"id": 1, "value": 50},
            {"id": 2, "value": 50}
        ]
        # max returns first occurrence
        self.assertEqual(self.sol.maxValueRecord(records), {"id": 1, "value": 50})

if __name__ == "__main__":
    unittest.main()
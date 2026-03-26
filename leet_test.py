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

if __name__ == "__main__":
    unittest.main()
import unittest
from part2 import is_nice

class TestFunc(unittest.TestCase):
    def test(self):
        self.assertTrue(is_nice("qjhvhtzxzqqjkmpb"), "expect true but got false")
        self.assertTrue(is_nice("xxyxx"), "expect true but got false")
        self.assertFalse(is_nice("uurcxstgmygtbstg"), "expect false but got true")
        self.assertFalse(is_nice("ieodomkazucvgmuy"), "expect false but got true")

if __name__ == '__main__':
    unittest.main()

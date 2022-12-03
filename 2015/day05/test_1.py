import unittest
from part1 import is_nice

class TestFunc(unittest.TestCase):
    def test(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"), "expect true but got false")

if __name__ == '__main__':
    unittest.main()

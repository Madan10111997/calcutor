# test_calculator.py

import unittest
import cal

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cal.add(2, 3), 5)
        self.assertEqual(cal.add(0, 0), 0)
        self.assertEqual(cal.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(cal.subtract(2, 3), -1)
        self.assertEqual(cal.subtract(0, 0), 0)
        self.assertEqual(cal.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(cal.multiply(2, 3), 6)
        self.assertEqual(cal.multiply(0, 0), 0)
        self.assertEqual(cal.multiply(-1, 1), -1)

if __name__ == '__main__':
    unittest.main()

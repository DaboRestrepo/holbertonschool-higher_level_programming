#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test the function max_integer using unittest"""
    def test_equal(self):
        """Test with assert equal"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_bool(self):
        """Test with assert boolean"""
        self.assertTrue(max_integer([5, 6]), 6)
        self.assertFalse(max_integer([5, 6]), 5)


if __name__ == '__main__':
    unittest.main()

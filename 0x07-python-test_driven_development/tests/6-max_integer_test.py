#!/usr/bin/python3
"""Unittest for the function max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test the function using a regular list"""
        self.assertEqual(max_integer([7, 8, 9, 10]), 10)

    def test_unordered_list(self):
        """Test the function using an unordered list"""
        self.assertEqual(max_integer([12, 2, 100, 1]), 100)

    def test_empty_list(self):
        """Test the function  using an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test function using a list with a single integer"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_elements(self):
        """Test function using negative integers"""
        self.assertEqual(max_integer([-13, -10, -45, -100]), -10)

    def test_mixed_numbers(self):
        """Test function with both pos and neg ints"""
        self.assertEqual(max_integer([-12, 1, -23, 4]), 4)

    def test_duplicate_max(self):
        """Test function with a duplicate max int"""
        self.assertEqual(max_integer([12, -9, 3, 12]), 12)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 0.5, 5.7, 9.9]), 9.9)

    def test_mix_float_and_int(self):
        self.assertEqual(max_integer([1, 2.4, 90, 0.1]), 90)


# Execute the file if it is run directly
if __name__ == '__main__':
    unittest.main()

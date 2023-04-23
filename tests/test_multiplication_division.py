# test_multiplication_division.py

import unittest
import math_functions

# Define class to test the program
class TestMultiplicationDivision(unittest.TestCase):
    # Function to test addition function
    def test_multiplication(self):
        result = math_functions.multiplication(2, 3)
        self.assertEqual(result, 6)

    # Function to test addition function
    def test_division(self):
        result = math_functions.division(4, 2)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()

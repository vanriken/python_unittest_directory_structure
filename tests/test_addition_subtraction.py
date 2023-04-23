# test_addition_subtraction.py

import unittest
import math_functions

# Define class to test the program
class TestAdditionSubtraction(unittest.TestCase):
    # Function to test addition function
    def test_addition(self):
        result = math_functions.addition(2, 2)
        self.assertEqual(result, 4)

    # Function to test addition function
    def test_subtraction(self):
        result = math_functions.subtraction(4, 2)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()

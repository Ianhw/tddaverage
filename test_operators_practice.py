"""
Program: test_operators_practice.py
Author: ian Waddell
Last date modified: 01/27/20

This is a unit test for operators
"""


import unittest

class OperatorsTest(unittest.TestCase):

    def test_equal(self):
        print(1)
        self.assertTrue(5 == 5)

    def test_not_equal(self):
        print(2)
        self.assertTrue(5 == 5)

    def test_greaterthan(self):
        print(3)
        self.assertTrue(6 > 5)

    def test_lessthan(self):
        print(4)
        self.assertTrue(5 < 6)

    def test_greaterequal(self):
        print(5)
        self.assertTrue(6 >= 5)

    def test_lessequal(self):
        print(6)
        self.assertTrue(5 <= 6)


if __name__ == '__main__':
    unittest.main()
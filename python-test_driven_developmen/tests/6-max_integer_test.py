#!/usr/bin/python3
""" Unittests for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_first_max(self):
        test_list = [110, 90, 80, 70, 10]
        self.assertEqual(max_integer(test_list), 110)

    def test_last_max(self):
        test_list = [10, 20, 30, 50, 90]
        self.assertEqual(max_integer(test_list), 90)

    def test_max_all_negative(self):
        test_list = [-1, -5, -7, -9, -11]
        self.assertEqual(max_integer(test_list), -1)

    def test_one_max(self):
        test_list = [100]
        self.assertEqual(max_integer(test_list), 100)
    
    def test_empty_list(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)
    
    def test_middle_max(self):
        test_list = [10, 20, 200, 50, 90]
        self.assertEqual(max_integer(test_list), 200)

#!/usr/bin/python3
'''Advent of Code 2018 Day 1 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day01 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day01part1(self) -> None:
        '''Test part 1'''
        self.assertEqual(day01.runpart1([1, -2, +3, +1]), 3)
        self.assertEqual(day01.runpart1([1, 1, 1]), 3)
        self.assertEqual(day01.runpart1([1, 1, -2]), 0)
        self.assertEqual(day01.runpart1([-1, -2, -3]), -6)

    def test_day01part2(self) -> None:
        '''Test part 2'''
        self.assertEqual(day01.runpart2([1, -1]), 0)
        self.assertEqual(day01.runpart2([3, 3, 4, -2, -4]), 10)
        self.assertEqual(day01.runpart2([-6, 3, 8, 5, -6]), 5)
        self.assertEqual(day01.runpart2([7, 7, -2, -7, -4]), 14)

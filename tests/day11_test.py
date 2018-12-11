#!/usr/bin/python3
'''Advent of Code 2018 Day 11 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day11 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day11helper(self) -> None:
        '''Test cell power function'''
        self.assertEqual(day11.cellpower(122, 79, 57), -5)
        self.assertEqual(day11.cellpower(217, 196, 39), 0)
        self.assertEqual(day11.cellpower(101, 153, 71), 4)

    def test_day11part1(self) -> None:
        '''Test part 1 solution'''
        self.assertEqual(day11.runpart1(18), (33, 45))
        self.assertEqual(day11.runpart1(42), (21, 61))

    def test_day11part2(self) -> None:
        '''Test part 2 solution'''
        self.assertEqual(day11.runpart2(18), (90, 269, 16))
        self.assertEqual(day11.runpart2(42), (232, 251, 12))

    def test_day11run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 11: %s\n" % str(day11.run()))

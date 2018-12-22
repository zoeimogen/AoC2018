#!/usr/bin/python3
'''Advent of Code 2018 Day 22 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day22 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day11part1(self) -> None:
        '''Test part 1 solution'''
        self.assertEqual(day22.runpart1(510, 10, 10), 114)

    def test_day11part2(self) -> None:
        '''Test part 2 solution'''
        self.assertEqual(day22.runpart2(510, 10, 10), 45)

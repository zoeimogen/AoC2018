#!/usr/bin/python3
'''Advent of Code 2018 Day 11 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day12 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day11part1(self) -> None:
        '''Test part 1 solution'''
        with open('tests/day12test.txt', 'r') as f:
            inputs = day12.readinputdata(f)
        self.assertEqual(day12.runpart1(inputs, 20), 325)

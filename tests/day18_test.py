#!/usr/bin/python3
'''Advent of Code 2018 Day 18 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day18 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests'''
    def test_day18part1(self) -> None:
        '''Test part 1'''
        grid = ['.#.#...|#.',
                '.....#|##|',
                '.|..|...#.',
                '..|#.....#',
                '#.#|||#|#|',
                '...#.||...',
                '.|....|...',
                '||...#|.#|',
                '|.||||..|.',
                '...#.|..|.']

        self.assertEqual(day18.runpart1(grid), 1147)

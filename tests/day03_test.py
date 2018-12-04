#!/usr/bin/python3
'''Advent of Code 2018 Day 3 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day03 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day03part1(self) -> None:
        '''Test part 1'''
        testdata = [(1, 1, 3, 4, 4),
                    (2, 3, 1, 4, 4),
                    (3, 5, 5, 2, 2)]
        (result, _) = day03.runpart1(testdata, 8, 8)
        self.assertEqual(result, 4)

    def test_day02part2(self) -> None:
        '''Test part 2'''
        testdata = [(1, 1, 3, 4, 4),
                    (2, 3, 1, 4, 4),
                    (3, 5, 5, 2, 2)]
        (_, fabric) = day03.runpart1(testdata, 8, 8)
        self.assertEqual(day03.runpart2(testdata, fabric), 3)

    def test_day03run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 03: %d, %d\n" % day03.run())

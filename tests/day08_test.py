#!/usr/bin/python3
'''Advent of Code 2018 Day 6 tests'''
from typing import List
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day08 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day08(self) -> None:
        '''Test solution'''
        inputs: List[int] = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

        (part1, part2, _) = day08.runsolution(inputs)
        self.assertEqual(part1, 138)
        self.assertEqual(part2, 66)

    def test_day08run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 08: %d, %d\n" % day08.run())

#!/usr/bin/python3
'''Advent of Code 2018 Day 6 tests'''
from typing import List, Tuple
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day06 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day06(self) -> None:
        '''Test solution'''
        inputs: List[Tuple[int, ...]] = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
        (part1, part2) = day06.runsolution(inputs, 32)
        self.assertEqual(part1, 17)
        self.assertEqual(part2, 16)

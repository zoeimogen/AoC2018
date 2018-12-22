#!/usr/bin/python3
'''Advent of Code 2018 Day 4 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day04 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day04(self) -> None:
        '''Test part 1'''
        with open('inputs/day04test.txt', 'r') as f:
            inputs = day04.readinputdata(f)

        self.assertEqual(day04.runsolution(inputs), (240, 4455))

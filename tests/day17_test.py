#!/usr/bin/python3
'''Advent of Code 2018 Day 17 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day17 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests'''
    def test_day17(self) -> None:
        '''Test part 1 helper function'''
        with open('tests/day17test.txt', 'r') as f:
            inputs = day17.readinputdata(f)

        self.assertEqual(day17.runsolution(inputs), (57, 29))

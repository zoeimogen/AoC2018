#!/usr/bin/python3
'''Advent of Code 2018 Day 23 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day23 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day23part1(self) -> None:
        '''Test part 1'''
        with open('inputs/day23test.txt', 'r') as f:
            inputs = day23.readinputdata(f)

        self.assertEqual(day23.runpart1(inputs), 7)

    def test_day23part2(self) -> None:
        '''Test part 2'''
        with open('inputs/day23test2.txt', 'r') as f:
            inputs = day23.readinputdata(f)

        self.assertEqual(day23.runpart2(inputs), 36)

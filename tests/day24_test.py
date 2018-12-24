#!/usr/bin/python3
'''Advent of Code 2018 Day 24 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day24 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day24part1(self) -> None:
        '''Test part 1'''
        with open('tests/day24test.txt', 'r') as f:
            inputs = day24.readinputdata(f)

        self.assertEqual(day24.runpart1(inputs), 5216)

    def test_day24part2(self) -> None:
        '''Test part 2'''
        with open('tests/day24test.txt', 'r') as f:
            inputs = day24.readinputdata(f)

        self.assertEqual(day24.runpart2(inputs), 51)

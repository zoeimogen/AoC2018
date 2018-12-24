#!/usr/bin/python3
'''Advent of Code 2018 Day 15 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day13 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day13part1(self) -> None:
        '''Test part 1'''
        with open('tests/day13test.txt', 'r') as f:
            inputs = day13.readinputdata(f)
        self.assertEqual(day13.runpart1(inputs), (7, 3))

    def test_day13part2(self) -> None:
        '''Test part 1'''
        with open('tests/day13test2.txt', 'r') as f:
            inputs = day13.readinputdata(f)
        self.assertEqual(day13.runpart2(inputs), (6, 4))

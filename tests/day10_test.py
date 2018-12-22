#!/usr/bin/python3
'''Advent of Code 2018 Day 10 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day10 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day10part1(self) -> None:
        '''Test solution'''
        with open('inputs/day10test.txt', 'r') as f:
            (i, text) = day10.runsolution(day10.readinputdata(f))

        self.assertEqual(i, 3)

        with open('inputs/day10testresult.txt', 'r') as f:
            textresult = f.read()
        self.assertEqual(text, textresult)

#!/usr/bin/python3
'''Advent of Code 2018 Day 25 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day25 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests'''
    def test_day18part1(self) -> None:
        '''Test part 1'''
        results = [('tests/day25test1.txt', 2),
                   ('tests/day25test2.txt', 4),
                   ('tests/day25test3.txt', 3),
                   ('tests/day25test4.txt', 8)]

        for (file, result) in results:
            with open(file, 'r') as f:
                inputs = day25.readinputdata(f)
            self.assertEqual(day25.runpart1(inputs), result)

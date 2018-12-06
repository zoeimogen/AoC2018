#!/usr/bin/python3
'''Advent of Code 2018 Day 5 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day05 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day05part1(self) -> None:
        '''Test part 1'''
        s = 'dabAcCaCBAcCcaDA'
        self.assertEqual(day05.runpart1(s), 10)

    def test_day05part2(self) -> None:
        '''Test part 2'''
        s = 'dabAcCaCBAcCcaDA'
        self.assertEqual(day05.runpart2(s), 4)

    def test_day05run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 05: %d, %d\n" % day05.run())

#!/usr/bin/python3
'''Advent of Code 2018 Day 16 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day16 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests. Day 16 gives us minimal test cases, so coverage is not good.'''
    def test_day16helper(self) -> None:
        '''Test part 1 helper function'''
        inputs = ([3, 2, 1, 1], (9, 2, 1, 2), [3, 2, 2, 1])
        self.assertEqual(day16.testmatch(inputs), 3)

    def test_day16run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 16: %d, %d\n" % day16.run())

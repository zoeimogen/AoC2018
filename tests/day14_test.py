#!/usr/bin/python3
'''Advent of Code 2018 Day 15 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day14 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day14run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 14: %s, %d\n" % day14.run())

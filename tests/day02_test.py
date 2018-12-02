#!/usr/bin/python3
'''Advent of Code 2018 Day 2 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day02 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day02part1(self) -> None:
        '''Test part 1'''
        testdata = ['abcdef', 'bababc', 'abbcde', 'abcccd',
                    'aabcdd', 'abcdee', 'ababab']
        self.assertEqual(day02.runpart1(testdata), 12)

    def test_day02part2(self) -> None:
        '''Test part 2'''
        testdata = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
        self.assertEqual(day02.runpart2(testdata), 'fgij')

    def test_day02run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 02: %d, %s\n" % day02.run())

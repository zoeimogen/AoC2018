#!/usr/bin/python3
'''Advent of Code 2018 Day 4 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day07 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day07part1(self) -> None:
        '''Test part 1'''
        with open('inputs/day07test.txt', 'r') as f:
            inputs = day07.readinputdata(f)

        self.assertEqual(day07.runpart1(inputs), 'CABDFE')

    def test_day07part2(self) -> None:
        '''Test part 2'''
        with open('inputs/day07test.txt', 'r') as f:
            inputs = day07.readinputdata(f)

        self.assertEqual(day07.runpart2(inputs, 0, 2), 15)

    def test_day07run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 07: %s, %d\n" % day07.run())

#!/usr/bin/python3
'''Advent of Code 2018 Day 14 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day14 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day14part1(self) -> None:
        '''Test part 1 helper function'''
        self.assertEqual(day14.runpart1(9), '5158916779')
        self.assertEqual(day14.runpart1(5), '0124515891')
        self.assertEqual(day14.runpart1(18), '9251071085')
        self.assertEqual(day14.runpart1(2018), '5941429882')

    def test_day14part2(self) -> None:
        '''Test part 1 helper function'''
        self.assertEqual(day14.runpart2('51589'), 9)
        self.assertEqual(day14.runpart2('01245'), 5)
        self.assertEqual(day14.runpart2('92510'), 18)
        self.assertEqual(day14.runpart2('59414'), 2018)

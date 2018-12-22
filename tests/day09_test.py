#!/usr/bin/python3
'''Advent of Code 2018 Day 9 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day09 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day09(self) -> None:
        '''Test solution'''
        self.assertEqual(day09.runsolution(9, 25), 32)
        self.assertEqual(day09.runsolution(10, 1618), 8317)
        self.assertEqual(day09.runsolution(13, 7999), 146373)
        self.assertEqual(day09.runsolution(17, 1104), 2764)
        self.assertEqual(day09.runsolution(21, 6111), 54718)
        self.assertEqual(day09.runsolution(30, 5807), 37305)

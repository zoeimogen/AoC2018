#!/usr/bin/python3
'''Advent of Code 2018 Day 20 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day20 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day20(self) -> None:
        '''Test solutions'''
        self.assertEqual(day20.move('WNE')[0], 3)
        self.assertEqual(day20.move('ENWWW(NEEE|SSE(EE|N))')[0], 10)
        self.assertEqual(day20.move('ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN')[0], 18)
        self.assertEqual(day20.move(('WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)'
                                     '|WSWWN(E|WWS(E|SS))))'))[0], 31)

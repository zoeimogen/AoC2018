#!/usr/bin/python3
'''Advent of Code 2018 Day 15 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2018 import day15 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day15part1(self) -> None:
        '''Test part 1 solution'''
        for files in [('inputs/day15test.txt', 27730),
                      ('inputs/day15test1.txt', 36334),
                      ('inputs/day15test2.txt', 39514),
                      ('inputs/day15test3.txt', 27755),
                      ('inputs/day15test4.txt', 28944),
                      ('inputs/day15test5.txt', 18740)]:
            with open(files[0], 'r') as f:
                inputs = day15.readinputdata(f)
                self.assertEqual(day15.runpart1(inputs), files[1])

    def test_day15part2(self) -> None:
        '''Test part 2 solution'''
        for files in [('inputs/day15test.txt', 4988),
                      ('inputs/day15test2.txt', 31284),
                      ('inputs/day15test3.txt', 3478),
                      ('inputs/day15test4.txt', 6474),
                      ('inputs/day15test5.txt', 1140)]:
            with open(files[0], 'r') as f:
                inputs = day15.readinputdata(f)
                self.assertEqual(day15.runpart2(inputs), files[1])

    def test_day15run(self) -> None:
        '''Find the actual solution'''
        _ = self

        with open('results.txt', 'a') as f:
            f.write("Day 15: %d, %d\n" % day15.run())

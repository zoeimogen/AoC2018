#!/usr/bin/python3
'''Advent of Code 2018 Day 19 solution'''
# pylint: disable=wrong-import-position,no-name-in-module,import-error

from typing import Tuple
import pyximport
pyximport.install(language_level=3)
from aoc2018.elfcode import State, Inputs, opcodes, readprogram, runprogram

def spea(state: State, _: Inputs) -> None:
    '''Special function to run solution faster. Register assignments hard coded.'''
    if state[5] > 0 and not state[3] % state[1]:
        state[0] += state[1]

def run() -> Tuple[int, int]:
    '''Main'''
    opcodes['spea'] = spea
    with open('inputs/day19-2.txt', 'r') as f:
        # Input file with some lines replaced with special function.
        inputs = readprogram(f)

    return (runprogram(inputs, 0), runprogram(inputs, 1))

if __name__ == '__main__':
    print(run())

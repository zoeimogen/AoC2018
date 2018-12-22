#!/usr/bin/python3
'''Advent of Code 2018 Day 16 solution'''

from typing import Tuple
from . import elfcode

def spea(state: elfcode.State, _: elfcode.Inputs) -> None:
    '''Special function to run solution faster. Register assignments hard coded.'''
    if state[5] > 0 and not state[3] % state[1]:
        state[0] += state[1]

def run() -> Tuple[int, int]:
    '''Main'''
    elfcode.opcodes['spea'] = spea
    with open('inputs/day19-2.txt', 'r') as f:
        # Input file with some lines replaced with special function.
        inputs = elfcode.readprogram(f)

    return (elfcode.runprogram(inputs, 0), elfcode.runprogram(inputs, 1))

if __name__ == '__main__':
    print(run())

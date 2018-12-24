#!/usr/bin/python3
'''Advent of Code 2018 Day 21 solution'''
# pylint: disable=wrong-import-position,no-name-in-module,import-error

from typing import Generator, Tuple, List
import pyximport
pyximport.install(language_level=3)
from aoc2018.elfcode import readprogram, Program, State
from aoc2018.day21cython import runprogram

def runpart1(program: Program) -> int:
    '''Run program, but break out at instruction 28 and return the value we're trying to
       compare with the input'''
    g: Generator[State, None, None] = runprogram(program)
    result: int = next(g)[program[28][2]]
    return result

def runpart2(program: Program) -> int:
    '''Run program, stopping when the instruction 28 break point repeats'''
    numbers: List[int] = []
    g: Generator[State, None, None] = runprogram(program)

    while True:
        state = next(g)
        if state[program[28][2]] in numbers:
            return numbers[-1]
        numbers.append(state[program[28][2]])

def run() -> Tuple[int, int]:
    '''Main'''
    with open('inputs/day21.txt', 'r') as f:
        inputs = readprogram(f)

    return(runpart1(inputs), runpart2(inputs))

if __name__ == '__main__':
    print(run())

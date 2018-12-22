#!/usr/bin/python3
'''Advent of Code 2018 Day 21 solution'''

from aoc2018.elfcode import readprogram, Program

def runprogram(program: Program) -> int:
    '''Run program, but break out at instruction 28 and return the value we're trying to
       compare with the input'''
    state = [0, 0, 0, 0, 0, 0]
    ip = 0

    while True:
        state[program[ip][1]] = ip
        program[ip][0](state, program[ip][2:])
        ip = state[program[ip][1]] + 1
        if ip == 28:
            return state[program[ip][2]]

def run() -> int:
    '''Main'''
    with open('inputs/day21.txt', 'r') as f:
        inputs = readprogram(f)

    return runprogram(inputs)
    # Part 2 requires manual pattern finding in the program registers.

if __name__ == '__main__':
    print(run())

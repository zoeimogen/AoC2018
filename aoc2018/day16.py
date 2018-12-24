#!/usr/bin/python3
'''Advent of Code 2018 Day 16 solution'''
# pylint: disable=wrong-import-position,no-name-in-module,import-error

import re
import copy
from typing import Tuple, List, Dict, Callable
import pyximport
pyximport.install(language_level=3)
from aoc2018.elfcode import ops, noop

State = List[int]
Inputs = Tuple[int, int, int]
Instruction = Tuple[int, int, int, int]
InputData = List[Tuple[State, Instruction, State]]
Program = List[Instruction]
Op = Callable[[State, Inputs], None]

def testmatch(i: Tuple[State, Instruction, State]) -> int:
    '''Test to see how many matches exist for an opcode'''
    matches = 0
    for o in ops:
        state: State = list(i[0])
        o(state, i[1][1:])
        if state == i[2]:
            matches += 1
    return matches

def runpart1(inputs: InputData) -> int:
    '''Run part 1 solution'''
    return len([i for i in inputs if testmatch(i) >= 3])

def runpart2(inputs: InputData, inputspart2: Program) -> int:
    '''Run part 2 solution'''
    possibilities: List[List[Op]] = [copy.copy(ops) for _ in range(16)]

    for i in inputs:
        # Test an opcode to see if it matches the input/output pair
        p: List[Op] = possibilities[i[1][0]]
        for o in copy.copy(p):
            state: State = list(i[0])
            o(state, i[1][1:])
            if state != i[2]:
                p.remove(o)

    inversep: Dict[Op, List[int]] = dict()
    for o in ops:
        # Create a reverse map of possible opcode->function mappings
        inversep[o] = []
        for poss in enumerate(possibilities):
            if o in poss[1]:
                inversep[o].append(poss[0])

    for _ in range(20):
        # Solve the resulting logic puzzle. (Range 20 is "Good enough")
        for o in inversep:
            if len(inversep[o]) == 1:
                for z in [z for z in inversep if z != o]:
                    try:
                        inversep[z].remove(inversep[o][0])
                    except ValueError:
                        pass

    function: List[Op] = [noop for _ in range(16)]
    for op in inversep:
        # Create a forward mapping of functions for use in the actual program
        function[inversep[op][0]] = op

    # Finally run the program!
    return runprogram(inputspart2, function)

def runprogram(program: Program, function: List[Op]) -> int:
    '''Run an actual program given the opcode->function mappings'''
    state = [0, 0, 0, 0]
    for instruction in program:
        function[instruction[0]](state, instruction[1:])

    return state[0]

def run() -> Tuple[int, int]:
    '''Main'''
    inputs = []
    m1 = re.compile(r'Before: \[(\d+), (\d+), (\d+), (\d+)\]')
    m2 = re.compile(r'(\d+) (\d+) (\d+) (\d+)')
    m3 = re.compile(r'After:  \[(\d+), (\d+), (\d+), (\d+)\]')

    with open('inputs/day16.txt', 'r') as f:
        while True:
            # Read the first half of the input. Exit when the regexps start failing.
            r = m1.match(f.readline())
            if r is not None:
                before: State = [int(r.group(1)), int(r.group(2)), int(r.group(3)), int(r.group(4))]
            else:
                break

            r = m2.match(f.readline())
            if r is not None:
                instruction = (int(r.group(1)), int(r.group(2)), int(r.group(3)), int(r.group(4)))
            else:
                break

            r = m3.match(f.readline())
            if r is not None:
                after: State = [int(r.group(1)), int(r.group(2)), int(r.group(3)), int(r.group(4))]
            else:
                break

            inputs.append((before, instruction, after))
            f.readline()

        f.readline()
        # Read the second part of the input
        inputspart2: Program = []
        while True:
            r = m2.match(f.readline())
            if r is not None:
                inputspart2.append((int(r.group(1)), int(r.group(2)),
                                    int(r.group(3)), int(r.group(4))))
            else:
                break

    return(runpart1(inputs), runpart2(inputs, inputspart2))

if __name__ == '__main__':
    print(run())

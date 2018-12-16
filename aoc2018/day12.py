#!/usr/bin/python3
'''Advent of Code 2018 Day 12 solution'''
import re
from typing import TextIO, Any, Dict
Input = Dict[str, Any]

def runsolution(inputs: Input, generations: int, verbose: bool = False) -> int:
    '''Solve part 1. Part 2 solved by observing pattern in score output'''
    for g in range(generations):
        state = '....' + inputs['state'] + '....'
        output = ''
        for i in range(len(inputs['state'])+4):
            x = state[i:i+5]
            if x in inputs['spread']:
                output += inputs['spread'][x]
            else:
                output += '.'

        inputs['state'] = output

        i = 0-((g+1)*2)
        score = 0
        for l in inputs['state']:
            if l == '#':
                score += i
            i += 1
        if verbose:
            print(g+1, score)

    return score

def readinputdata(f: TextIO) -> Input:
    '''Read input data from the given file handle into inputs'''
    m1 = re.compile(r'initial state: (.+)')
    m2 = re.compile(r'([.#]+) => ([.#])')
    inputs: Input = {'spread': {}}

    for line in f.readlines():
        z = m1.match(line)
        if z is not None:
            inputs['state'] = z.group(1)
        else:
            z = m2.match(line)
            if z is not None:
                inputs['spread'][z.group(1)] = z.group(2)
    return inputs

def run() -> int:
    '''Main'''
    with open('inputs/day12.txt', 'r') as f:
        inputs = readinputdata(f)

    return runsolution(inputs, 20)

if __name__ == '__main__':
    print("%d\n" % (run()))

#!/usr/bin/python3
'''Advent of Code 2018 Day 12 solution'''
import re
import copy
from typing import TextIO, Any, Dict, Tuple, List
from . import sequence

Input = Dict[str, Any]

def rungeneration(inputs: Input) -> None:
    '''Run a single generation'''
    state = '....' + inputs['state'] + '....'
    output = ''
    for i in range(len(inputs['state'])+4):
        x = state[i:i+5]
        if x in inputs['spread']:
            output += inputs['spread'][x]
        else:
            output += '.'

    inputs['state'] = output

def getscore(inputs: Input, g: int) -> int:
    '''Get the current score'''
    # i is the offset needed to calculate the pot position of slot 0 as it expands leftwards
    # each generation.
    i = 0-((g+1)*2)
    score = 0
    for l in inputs['state']:
        if l == '#':
            score += i
        i += 1

    return score

def runpart1(inputs: Input, generations: int) -> int:
    '''Solve part 1'''
    for g in range(generations):
        rungeneration(inputs)

    return getscore(inputs, g)

def runpart2(inputs: Input, generations: int) -> int:
    '''Solve part 2 by spotting the pattern and predicting the result'''
    g = 1
    scorediffs: List[int] = []
    scores = [0]
    while True:
        rungeneration(inputs)
        score = getscore(inputs, g)
        scorediffs.append(score - scores[-1])
        scores.append(score)
        if sequence.checksequence(scorediffs):
            return sequence.predictincrementing(scorediffs, generations)
        g += 1

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

def run() -> Tuple[int, int]:
    '''Main'''
    with open('inputs/day12.txt', 'r') as f:
        inputs = readinputdata(f)

    input2 = copy.copy(inputs)
    return(runpart1(inputs, 20), runpart2(input2, 50000000000))

if __name__ == '__main__':
    print(run())

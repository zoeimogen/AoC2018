#!/usr/bin/python3
'''Advent of Code 2018 Day 10 solution'''
import re
from typing import List, Tuple, TextIO
import numpy
InputData = List[List[int]]

def printgrid(inputs: InputData) -> str:
    '''Print the populated part of our grid'''
    output = ''
    minx = min([p[1] for p in inputs])
    miny = min([p[0] for p in inputs])
    grid = numpy.full((max([p[1] for p in inputs])+1, max(p[0] for p in inputs)+1), ' ')

    for p in inputs:
        grid[p[1]][p[0]] = '#'

    for l in grid[minx:]:
        output += str.join('', l[miny:]) + "\n"

    return output

def runsolution(inputs: InputData) -> Tuple[int, str]:
    '''Solve part 1'''
    i = 0
    lastminx = min([p[1] for p in inputs])
    lastminy = min([p[0] for p in inputs])
    while True:
        for p in inputs:
            p[0] += p[2]
            p[1] += p[3]
        i += 1
        minx = min([p[1] for p in inputs])
        miny = min([p[0] for p in inputs])
        if minx < lastminx or miny < lastminy:
            for p in inputs:
                p[0] -= p[2]
                p[1] -= p[3]
            return (i-1, printgrid(inputs))
        lastminx = minx
        lastminy = miny

def readinputdata(f: TextIO) -> InputData:
    '''Read input data from the given file handle into inputs'''
    m = re.compile(r'position=<([- \d]+), ([- \d]+)> velocity=<([- \d]+), ([- \d]+)>')

    inputs: InputData = []

    for line in f.readlines():
        z = m.match(line)
        if z is not None:
            inputs.append([int(z.group(1)), int(z.group(2)), int(z.group(3)), int(z.group(4))])

    return inputs

def run() -> Tuple[int, str]:
    '''Main'''
    with open('inputs/day10.txt', 'r') as f:
        return runsolution(readinputdata(f))

if __name__ == '__main__':
    print("%d\n%s", run())

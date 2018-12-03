#!/usr/bin/python3
'''Advent of Code 2018 Day 2 solution'''
from typing import Tuple, List
import re
import numpy
InputData = List[Tuple[int, int, int, int, int]]

def runpart1(values: InputData, maxx: int, maxy: int) -> Tuple[int, List[List[int]]]:
    '''Run part one'''
    fabric: List[List[int]] = numpy.zeros((maxx, maxy), dtype=int)
    for v in values:
        for x in range(v[1], v[1]+v[3]):
            for y in range(v[2], v[2]+v[4]):
                fabric[x][y] += 1

    overlaps = 0
    for x in range(0, maxx):
        for y in range(0, maxy):
            if fabric[x][y] > 1:
                overlaps += 1

    return(overlaps, fabric)

def runpart2(values: InputData, fabric: List[List[int]]) -> int:
    '''Run part two'''
    for v in values:
        overlap = False
        for x in range(v[1], v[1]+v[3]):
            for y in range(v[2], v[2]+v[4]):
                if fabric[x][y] > 1:
                    overlap = True
                    continue
        if not overlap:
            return v[0]

    return 0

def run() -> Tuple[int, int]:
    '''Main'''
    m = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    inputs = []
    maxx = 0
    maxy = 0

    with open('inputs/day03.txt', 'r') as f:
        for line in f.readlines():
            z = m.match(line)
            if z is not None:
                inputs.append((int(z.group(1)), int(z.group(2)), int(z.group(3)),
                               int(z.group(4)), int(z.group(5))))
                if int(z.group(2))+int(z.group(4)) > maxx:
                    maxx = int(z.group(2))+int(z.group(4))
                if int(z.group(3))+int(z.group(5)) > maxy:
                    maxy = int(z.group(3))+int(z.group(5))

    (part1, fabric) = runpart1(inputs, maxx, maxy)
    part2 = runpart2(inputs, fabric)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

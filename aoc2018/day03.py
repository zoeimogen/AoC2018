#!/usr/bin/python3
'''Advent of Code 2018 Day 2 solution'''
from typing import Tuple, List
import re
import numpy
InputData = List[Tuple[int, int, int, int, int]]

def runpart1(values: InputData, maxx: int, maxy: int) -> Tuple[int, List[List[int]]]:
    '''Run part one'''

    # Initalise a fabric of all zeros large enough to hold all claims'''
    fabric: List[List[int]] = numpy.zeros((maxx, maxy), dtype=int)
    overlaps = 0

    # Loop through the claims in the input...
    for v in values:
        # ...and increment the fabric counter for every cell it touches
        for x in range(v[1], v[1]+v[3]):
            for y in range(v[2], v[2]+v[4]):
                fabric[x][y] += 1
                # If we've just incremented the counter from 1 to 2, that's a new overlap.
                # Count it.
                if fabric[x][y] == 2:
                    overlaps += 1

    return(overlaps, fabric)

def runpart2(values: InputData, fabric: List[List[int]]) -> int:
    '''Run part two and find which claim didn't overlap with any other claim.
       Uses pre-populated fabric data from part one.'''

    # Loop through the claims in the input...
    for v in values:
        overlap = False
        # ...and check each cell and see if it was marked by two or more claims
        for x in range(v[1], v[1]+v[3]):
            for y in range(v[2], v[2]+v[4]):
                if fabric[x][y] > 1:
                    overlap = True
                    continue
        # If the entire of this claim area only has one claim to it, it's ours so return it.
        if not overlap:
            return v[0]

    return 0

def run() -> Tuple[int, int]:
    '''Main'''
    m = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    inputs = []
    maxx = 0
    maxy = 0

    # Read input data line-by-line and copy into inputs
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

    # Solve the problem
    (part1, fabric) = runpart1(inputs, maxx, maxy)
    part2 = runpart2(inputs, fabric)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

#!/usr/bin/python3
'''Advent of Code 2018 Day 23 solution'''

import re
from statistics import median
from typing import List, Tuple, TextIO

Nanobot = Tuple[int, int, int, int]
Input = List[Nanobot]
Point = Tuple[Nanobot, int]

def taxicabdistance(a: Nanobot, b: Nanobot) -> int:
    '''Calculate Taxi Cab (Manhattan) distance between two pairs of coordinates'''
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def runpart1(inputs: Input) -> int:
    '''Solve part 1'''
    inputs.sort(key=lambda x: x[3], reverse=True)
    strongest = inputs[0]

    inrange = [n for n in inputs if taxicabdistance(n, strongest) <= strongest[3]]
    return len(inrange)

def runpart2(inputs: Input) -> int:
    '''Solve part 2'''
    # This deserves some explanation. Frankly, I'm amazed it worked first time. We take the median
    # of the input coordinates as a starting point, and move towards the best point in terms of
    # Nanobots in range, using distance from the origin (Our location) as tie break. We cast the
    # net very wide (searching current location +/- 10,000 initially) and gradually narrow that
    # down until we find the best point. Large initial net seems to be the key to not getting
    # caught in a a local maximum, but the numbers might neet tweaking for other input data sets.
    x = int(median([a[0] for a in inputs]))
    y = int(median([a[1] for a in inputs]))
    z = int(median([a[2] for a in inputs]))

    # Size of initial scan area
    diff = 100000

    while True:
        box: List[Point] = [] # List of points we've checked

        # Check each point in turn and record nanobots in range.
        for a in [x-diff, x, x+diff]:
            for b in [y-diff, y, y+diff]:
                for c in [z-diff, z, z+diff]:
                    d: Nanobot = (a, b, c, 0)
                    inrange: int = len([n for n in inputs if taxicabdistance(n, d) <= n[3]])
                    box.append((d, inrange))

        # Get the best count of bots in range found during our checks
        box.sort(key=lambda bot: bot[1], reverse=True)
        best: int = box[0][1]

        # Get valid successors (Any point that equals the best count)
        valid: List[Point] = [n for n in box if n[1] == best]

        # Now find the best point (Closest to origin that is also valid)
        valid.sort(key=lambda p: abs(p[0][0] + abs(p[0][1]) + abs(p[0][2])))
        # If the current point is our best point...
        if (valid[0][0][0], valid[0][0][1], valid[0][0][2]) == (x, y, z):
            if diff == 1:
                # ...return the distance from the origin if we're already at minimum net size...
                return abs(x) + abs(y) + abs(z)
            # ...otherwise, shrink the net.
            diff = int(diff / 10)

        # Update the current point
        x = valid[0][0][0]
        y = valid[0][0][1]
        z = valid[0][0][2]

def readinputdata(f: TextIO) -> Input:
    '''Read input data from the given file handle into inputs'''
    inputs: Input = []

    m = re.compile(r'pos=<([-\d]+),([-\d]+),([-\d]+)>, r=([-\d]+)')
    for line in f.readlines():
        result = m.match(line)
        if result is not None:
            inputs.append((int(result.group(1)), int(result.group(2)),
                           int(result.group(3)), int(result.group(4))))

    return inputs

def run() -> Tuple[int, int]:
    '''Main'''
    with open('inputs/day23.txt', 'r') as f:
        inputs = readinputdata(f)

    return(runpart1(inputs), runpart2(inputs))

if __name__ == '__main__':
    print(run())

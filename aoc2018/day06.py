#!/usr/bin/python3
'''Advent of Code 2018 Day 6 solution'''
from typing import Tuple, List
import numpy
Coords = Tuple[int, ...]

def taxicabdistance(a: Coords, b: Coords) -> int:
    ''' Calculate Taxi Cab (Manhattan) distance between two pairs of coordinates'''
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def runsolution(inputs: List[Coords], threshold: int) -> Tuple[int, int]:
    '''Solve both parts'''
    minx = min([z[0] for z in inputs])
    miny = min([z[1] for z in inputs])
    maxx = max([z[0] for z in inputs])
    maxy = max([z[1] for z in inputs])

    total = numpy.zeros(len(inputs), dtype=int)
    totalsafe = 0

    # Loop through the grid
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            # Get distances to all other points
            distances = [taxicabdistance(z, (x, y)) for z in inputs]
            d = sorted(distances)
            # If there isn't a tie for the closest point, add one to the count for the closest
            if d[0] != d[1]:
                total[distances.index(d[0])] += 1
            # Keep track of the number of points satisfying part 2. (Sum of distances below
            # threshold)
            if sum(distances) < threshold:
                totalsafe += 1

    # Go round the edge of the grid, anything closest points we find have infinite coverage
    infinites = set()
    for x in range(minx - 25, maxx + 25):
        distances = [taxicabdistance(z, (x, miny-25)) for z in inputs]
        infinites.add(distances.index(min(distances)))
        distances = [taxicabdistance(z, (x, maxy+25)) for z in inputs]
        infinites.add(distances.index(min(distances)))

    for y in range(miny - 25, maxy + 25):
        distances = [taxicabdistance(z, (minx-25, y)) for z in inputs]
        infinites.add(distances.index(min(distances)))
        distances = [taxicabdistance(z, (maxx+25, y)) for z in inputs]
        infinites.add(distances.index(min(distances)))

    # Strip out the infinite coordinates from the result
    for i in infinites:
        total[i] = 0

    # Return coordinate with highest score, and size of safe area.
    return (max(total), totalsafe)

def run() -> Tuple[int, int]:
    '''Main'''

    # Read input data
    with open('inputs/day06.txt', 'r') as f:
        inputs: List[Coords] = [tuple(map(int, line.rstrip("\n").split(', '))) for line in f]

    # Solve the problem
    return runsolution(inputs, 10000)

if __name__ == '__main__':
    print(run())

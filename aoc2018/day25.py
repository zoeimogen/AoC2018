#!/usr/bin/python3
'''Advent of Code 2018 Day 16 solution'''

from typing import Tuple, List, Dict, TextIO, Optional, Set

Coords = Tuple[int, ...]
Inputs = List[Coords]

def taxicabdistance(a: Coords, b: Coords) -> int:
    '''Calculate Taxi Cab (Manhattan) distance between two pairs of coordinates'''
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3] - b[3])

def collect(group: Dict[int, Set[int]], i: int, seen: Optional[Set[int]] = None) -> None:
    '''Iteratively collect up a constellation, checking both parent and children nodes'''
    if seen is None:
        seen = set([i])
        cleanup = True
    else:
        cleanup = False

    if i not in group:
        return

    for c in group[i]:
        if c in seen:
            continue
        seen.add(c)
        if c in group:
            collect(group, c, seen)

    for d in [j for j in group if i in group[j]]:
        if d in seen:
            continue
        seen.add(d)
        collect(group, d, seen)

    if cleanup:
        for j in [j for j in seen if j != i]:
            group[i].add(j)
            if j in group:
                del group[j]

def runpart1(inputs: Inputs) -> int:
    '''Run part 1 solution'''
    group: Dict[int, Set[int]] = {}
    for i, c in enumerate(inputs):
        group[i] = set()
        for j, d in enumerate(inputs):
            if j <= i:
                continue
            if taxicabdistance(c, d) <= 3:
                group[i].add(j)

    lastlen = 0

    while lastlen != len(group):
        lastlen = len(group)
        for i in range(0, max(group.keys())):
            if i not in group:
                continue
            collect(group, i)

    return lastlen

def readinputdata(f: TextIO) -> Inputs:
    '''Run an actual program given the opcode->function mappings'''
    inputs: Inputs = []
    for line in f:
        result: Coords = tuple(map(int, line.split(',')))
        inputs.append(result)
    return inputs

def run() -> int:
    '''Main'''
    with open('inputs/day25.txt', 'r') as f:
        inputs = readinputdata(f)

    return runpart1(inputs)

if __name__ == '__main__':
    print(run())

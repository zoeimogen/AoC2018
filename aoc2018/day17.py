#!/usr/bin/python3
'''Advent of Code 2018 Day 17 solution'''
 # pylint: disable=too-many-arguments

import re
import sys
from typing import TextIO, Tuple, List, Set
import numpy

sys.setrecursionlimit(10000)

Input = Tuple[Tuple[int, int, int, int], List[List[int]]]

def printmap(inputs: Input, visited: Set[Tuple[int, int]], water: Set[Tuple[int, int]]) -> None:
    '''Display map for debug purposes'''
    for y in range(inputs[0][0], inputs[0][1]+1):
        for x in range(inputs[0][2], inputs[0][2]+1):
            if (y, x) in water:
                print('~', end='')
            elif (y, x) in visited:
                print('|', end='')
            elif inputs[1][y][x]:
                print('#', end='')
            else:
                print('.', end='')
        print('')

def readinputdata(f: TextIO) -> Input:
    '''Read input data from file handle'''
    m = re.compile(r'([xy])=(\d+), [xy]=(\d+)\.\.(\d+)')

    # Find how big a grid we need
    maxx = maxy = 0
    minx = miny = 9999

    for line in f:
        r = m.match(line)
        if r:
            if r.group(1) == 'x':
                x1 = x2 = int(r.group(2))
                y1 = int(r.group(3))
                y2 = int(r.group(4))
            else:
                x1 = int(r.group(3))
                x2 = int(r.group(4))
                y1 = y2 = int(r.group(2))
            minx = min(x1, minx)
            maxx = max(x2, maxx)
            miny = min(y1, miny)
            maxy = max(y2, maxy)

    # Now initalise the grid and read the input
    grid = numpy.full((maxy+1, maxx+1), False, dtype=bool)
    f.seek(0, 0)

    for line in f:
        r = m.match(line)
        if r:
            if r.group(1) == 'x':
                x = int(r.group(2))
                for y in range(int(r.group(3)), int(r.group(4))+1):
                    grid[y][x] = True
            else:
                y = int(r.group(2))
                for x in range(int(r.group(3)), int(r.group(4))+1):
                    grid[y][x] = True

    return ((miny, maxy, minx, maxx), grid)

def flow(y: int, x: int, inputs: Input, visited: Set[Tuple[int, int]],
         water: Set[Tuple[int, int]]) -> bool:
    '''Follow water flow'''
    if y > inputs[0][1] or (y, x) in visited and (y, x) not in water:
        # Free flow from here to the end of the world
        return False
    if inputs[1][y][x] or (y, x) in water:
        # This square is blocked, you cannot go here.
        return True
    visited.add((y, x))
    # Flow down if we can
    if flow(y+1, x, inputs, visited, water):
        # Can't flow down, blocked. Go left/right instead.
        left = flowleft(y, x-1, inputs, visited, water)
        right = flowright(y, x+1, inputs, visited, water)
        if left and right:
            flowleft(y, x-1, inputs, visited, water, blocked=True)
            flowright(y, x+1, inputs, visited, water, blocked=True)
            water.add((y, x))
            return True
        return False
    return False

def flowleft(y: int, x: int, inputs: Input, visited: Set[Tuple[int, int]],
             water: Set[Tuple[int, int]], blocked: bool = False) -> bool:
    '''Follow water flow left, when we've hit bottom'''
    if y > inputs[0][1] and (y, x) not in water:
        # Free flow from here to the end of the world
        return False
    if inputs[1][y][x] or (y, x) in water:
        # This square is blocked, you cannot go here.
        return True
    visited.add((y, x))
    if blocked:
        water.add((y, x))
    # Flow down if we can
    if flow(y+1, x, inputs, visited, water):
        # Can't flow down, blocked. Go left/right instead.
        return flowleft(y, x-1, inputs, visited, water, blocked=blocked)
    return False

def flowright(y: int, x: int, inputs: Input, visited: Set[Tuple[int, int]],
              water: Set[Tuple[int, int]], blocked: bool = False) -> bool:
    '''Follow water flor right, when we've hit bottom'''
    if y > inputs[0][1] and (y, x) not in water:
        # Free flow from here to the end of the world
        return False
    if inputs[1][y][x] or (y, x) in water:
        # This square is blocked, you cannot go here.
        return True
    visited.add((y, x))
    if blocked:
        water.add((y, x))
    # Flow down if we can
    if flow(y+1, x, inputs, visited, water):
        # Can't flow down, blocked. Go left/right instead.
        return flowright(y, x+1, inputs, visited, water, blocked=blocked)
    return False

def runsolution(inputs: Input) -> Tuple[int, int]:
    '''Solve problem'''
    visited: Set[Tuple[int, int]] = set()
    water: Set[Tuple[int, int]] = set()
    flow(0, 500, inputs, visited, water)
    return (len([v for v in visited if v[0] >= inputs[0][0]]), len(water))

def run() -> Tuple[int, int]:
    '''Main'''
    with open('inputs/day17.txt', 'r') as f:
        inputs = readinputdata(f)

    return runsolution(inputs)

if __name__ == '__main__':
    print(run())

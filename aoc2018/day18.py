#!/usr/bin/python3
'''Advent of Code 2018 Day 18 solution'''

from typing import List
import numpy

Grid = List[str]

def getsurrounds(grid: Grid, y: int, x: int) -> str:
    '''Get squares surrounding given coordinates'''
    result = ''
    if y > 0:
        if x > 0:
            result += grid[y-1][x-1]
        result += grid[y-1][x]
        if x < len(grid[y])-1:
            result += grid[y-1][x+1]
    if x > 0:
        result += grid[y][x-1]
    if x < len(grid[y])-1:
        result += grid[y][x+1]
    if y < len(grid)-1:
        if x > 0:
            result += grid[y+1][x-1]
        result += grid[y+1][x]
        if x < len(grid[y])-1:
            result += grid[y+1][x+1]
    return result

def scoregrid(grid: Grid) -> int:
    '''Find the score of the current grid'''
    wood = lumber = 0
    for line in grid:
        for c in line:
            if c == '|':
                wood += 1
            elif c == '#':
                lumber += 1
    return wood * lumber

def runpart1(grid: Grid) -> int:
    '''Solve part 1. Part two solved by looking for repeating patterns in the score output.'''
    for _ in range(10):
        newgrid = numpy.full((len(grid), len(grid[0])), ' ')
        for (y, _) in enumerate(grid):
            for x in range(len(grid[y])):
                if grid[y][x] == '.':
                    if len([c for c in getsurrounds(grid, y, x) if c == '|']) >= 3:
                        newgrid[y][x] = '|'
                    else:
                        newgrid[y][x] = '.'
                elif grid[y][x] == '|':
                    if len([c for c in getsurrounds(grid, y, x) if c == '#']) >= 3:
                        newgrid[y][x] = '#'
                    else:
                        newgrid[y][x] = '|'
                else:
                    surrounds = getsurrounds(grid, y, x)
                    if '|' in surrounds and '#' in surrounds:
                        newgrid[y][x] = '#'
                    else:
                        newgrid[y][x] = '.'
        grid = newgrid

    return scoregrid(grid)

def run() -> int:
    '''Main'''
    grid: Grid = []
    with open('inputs/day18.txt', 'r') as f:
        for line in f:
            grid.append(line.rstrip("\n"))

    return runpart1(grid)

if __name__ == '__main__':
    print(run())

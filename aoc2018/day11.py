#!/usr/bin/python3
'''Advent of Code 2018 Day 10 solution'''
from typing import List, Tuple
import numpy
Grid = List[List[int]]

def cellpower(x: int, y: int, serial: int) -> int:
    '''Calculate the "power" of a cell'''
    if not x or not y:
        return 0
    rack = x + 10
    return (int(((rack * y + serial) * rack) / 100) % 10) - 5

def generategrid(serial: int) -> Grid:
    '''Generate a 300x300 grid for a given serial. (0 is ignored)'''
    grid: Grid = numpy.empty((301, 301), dtype=int)
    for x in range(0, 301):
        for y in range(0, 301):
            grid[x][y] = cellpower(x, y, serial)
    return grid

def generatesat(grid: Grid) -> Grid:
    '''Generate a Summed Area Table for a given grid'''
    satgrid: Grid = numpy.empty((301, 301), dtype=int)
    satgrid[0][0] = grid[0][0]

    for z in range(1, 301):
        satgrid[0][z] = satgrid[0][z-1]+grid[0][z]
        satgrid[z][0] = satgrid[z-1][0]+grid[z][0]

    for x in range(1, 301):
        for y in range(1, 301):
            satgrid[x][y] = satgrid[x-1][y]+satgrid[x][y-1]-satgrid[x-1][y-1]+grid[x][y]

    return satgrid

def squarepower(sat: Grid, x: int, y: int, size: int) -> int:
    '''CAlculate the sum of the square of size size starting at x,y, using a SAT'''
    return sat[x+size-1][y+size-1] - sat[x-1][y+size-1] - sat[x+size-1][y-1] + sat[x-1][y-1]

def runpart1(serial: int) -> Tuple[int, int]:
    '''Solve part 1'''
    grid = generategrid(serial)
    sat = generatesat(grid)

    maxx = 0
    maxy = 0
    maxpower = 0
    for x in range(1, 299):
        for y in range(1, 299):
            sp = squarepower(sat, x, y, 3)
            if sp > maxpower:
                maxx = x
                maxy = y
                maxpower = sp
    return (maxx, maxy)

def runpart2(serial: int) -> Tuple[int, int, int]:
    '''Solve part 2'''
    grid = generategrid(serial)
    sat = generatesat(grid)
    maxsize = 0
    maxpower = 0
    maxx = 0
    maxy = 0

    for size in range(1, 301):
        for x in range(1, 300-size):
            for y in range(1, 300-size):
                sp = squarepower(sat, x, y, size)
                if sp > maxpower:
                    maxx = x
                    maxy = y
                    maxpower = sp
                    maxsize = size
    return (maxx, maxy, maxsize)

def run() -> Tuple[Tuple[int, int], Tuple[int, int, int]]:
    '''Main'''
    return (runpart1(1788), runpart2(1788))

if __name__ == '__main__':
    print(run())

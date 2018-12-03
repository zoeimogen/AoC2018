#!/usr/bin/python3
'''Advent of Code 2018 Day 1 solution'''
from typing import Union, Tuple, List
import functools

def runpart1(sequence: List[int]) -> int:
    '''Run part one
       Just sum the input values'''
    return functools.reduce(lambda x, y: x+y, sequence)

def runpart2(sequence: list, result: int = 0, seen: Union[set, None] = None) -> int:
    '''Run part two'''

    # On first iteration, initialise seen as a set. (Sets are faster than lists for this)
    if seen is None:
        seen = set()

    # Loop through input values and store each result as it's seen.
    for d in sequence:
        seen.add(result)
        result += d
        # If we've seen this value before, return it.
        if result in seen:
            return result

    # We reached the end of the input. Recurse back into this function, but preserving the
    # current result counter and seen values list.
    return runpart2(sequence, result, seen)

def run() -> Tuple[int, int]:
    '''Main'''

    # Read input file and put into values
    values = []
    with open('inputs/day01.txt', 'r') as f:
        for line in f.readlines():
            values.append(int(line))

    # Run the solution
    part1 = runpart1(values)
    part2 = runpart2(values)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

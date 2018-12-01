#!/usr/bin/python3
'''Advent of Code 2018 Day 1 solution'''
from typing import Union, Tuple

def runpart1(sequence: list) -> int:
    '''Run part one'''
    result = 0
    for d in sequence:
        result += d
    return result

def runpart2(sequence: list, result: int = 0, seen: Union[set, None] = None) -> int:
    '''Run part two'''
    if seen is None:
        seen = set()
    for d in sequence:
        seen.add(result)
        result += d
        if result in seen:
            return result
    return runpart2(sequence, result, seen)

def run() -> Tuple[int, int]:
    '''Main'''
    values = []
    with open('inputs/day01.txt', 'r') as f:
        for line in f.readlines():
            values.append(int(line))

    part1 = runpart1(values)
    part2 = runpart2(values)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

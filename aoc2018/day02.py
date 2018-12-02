#!/usr/bin/python3
'''Advent of Code 2018 Day 2 solution'''
from collections import defaultdict
import functools
from typing import List, Tuple, DefaultDict, Set

def runpart1(values: List[str]) -> int:
    '''Run part one'''
    result: DefaultDict[int, int] = defaultdict(int)
    for line in values:
        count: DefaultDict[str, int] = defaultdict(int)
        for letter in line:
            count[letter] += 1
        for i in range(2, max(count.values())+1):
            if i in count.values():
                result[i] += 1

    return functools.reduce(lambda x, y: x*y, result.values())

def runpart2(values: List[str]) -> str:
    '''Run part two'''
    possibles: Set[str] = set()
    for line in values:
        for i in range(0, len(line)):
            p = line[0:i] + line[i+1:len(line)]
            if p in possibles:
                return p
        for i in range(0, len(line)):
            p = line[0:i] + line[i+1:len(line)]
            possibles.add(p)
    return ''

def run() -> Tuple[int, str]:
    '''Main'''
    inputs = []
    with open('inputs/day02.txt', 'r') as f:
        for line in f.readlines():
            inputs.append(line.rstrip('\n'))

    part1 = runpart1(inputs)
    part2 = runpart2(inputs)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

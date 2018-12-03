#!/usr/bin/python3
'''Advent of Code 2018 Day 2 solution'''
from collections import defaultdict
import functools
from typing import List, Tuple, DefaultDict, Set

def runpart1(values: List[str]) -> int:
    '''Run part one'''

    # result counts the number of times we've seen two (result[2]), three (result[3]) or more
    # repeats. (Actual input data turns out never to have more than three repeats of a letter)
    result: DefaultDict[int, int] = defaultdict(int)

    # Go through each line...
    for line in values:
        # ...first, counting the number of times each letter appears...
        count: DefaultDict[str, int] = defaultdict(int)
        for letter in line:
            count[letter] += 1
        # ...then incrementing the result[2] once for each letter than appears twice, result[3]
        # for each letter than appears three times and so on.
        for i in range(2, max(count.values())+1):
            if i in count.values():
                result[i] += 1

    # Get the product of all counters we've gathered.
    return functools.reduce(lambda x, y: x*y, result.values())

def runpart2(values: List[str]) -> str:
    '''Run part two'''

    # A set of all potential matches so far. (Sets are faster than lists for 'x in set')
    possibles: Set[str] = set()

    # For each input line...
    for line in values:
        # ...check for each letter in turn...
        for i in range(0, len(line)):
            p = line[0:i] + line[i+1:len(line)]
            # ...if removing it means it matches something in our possibles list from previous
            # lines. If so, it's our match.
            if p in possibles:
                return p

        # Then add every possible match string to the possibles list, by dropping each letter
        # in turn. We need to do this separately to make sure we don't match on the current string,
        # caused by repeated letters. (E.g. abcddef would match abcdef on removing the second d,
        # because we only just added abcdef by dropping the previous letter)
        for i in range(0, len(line)):
            p = line[0:i] + line[i+1:len(line)]
            possibles.add(p)

    # We should never get here - we didn't find a match.
    return ''

def run() -> Tuple[int, str]:
    '''Main'''

    # Read the input strings into inputs
    inputs = []
    with open('inputs/day02.txt', 'r') as f:
        for line in f.readlines():
            inputs.append(line.rstrip('\n'))

    # Run the solution
    part1 = runpart1(inputs)
    part2 = runpart2(inputs)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

#!/usr/bin/python3
'''Advent of Code 2018 Day 5 solution'''
from string import ascii_lowercase
from typing import Tuple

def runpart1(inputs: str) -> int:
    '''Solve part 1. This isn't the most elegant way, but it's the quickest found so far'''
    i = 0

    # Output
    o = ''
    # Loop is called often enough that precalculating this saves time!
    l = len(inputs)-1

    # Loop across input characters
    while i < l:
        # If the current and next character would react, skip both.
        if inputs[i] != inputs[i+1] and inputs[i].lower() == inputs[i+1].lower():
            i += 2
            try:
                # It's possible the last character on the output buffer reacts with our next
                # character. If so, skip the next character and remove the existing one from
                # the output buffer.
                while inputs[i] != o[-1:] and inputs[i].lower() == o[-1:].lower():
                    i += 1
                    o = o[:-1]
            # We might have gone beyond the end of our input, so catch that.
            except IndexError:
                pass
        else:
            # Nothing reacts, so add to the output and advance to the next input character
            o += inputs[i]
            i += 1

    # We probably have one character left in the input, so add it to the output if so.
    try:
        o += inputs[i]
    except IndexError:
        pass

    return len(o)

def removeletter(inputs: str, l: str) -> str:
    '''Remove all upper and lower case occurances of letter l from s'''
    s = inputs.replace(l, '')
    return s.replace(l.upper(), '')

def runpart2(inputs: str) -> int:
    '''Solve part 2'''
    # Remove every character a-z in turn, and run the part 1 solution. Return best (lowest) score
    return min([runpart1(removeletter(inputs, c)) for c in ascii_lowercase])

def run() -> Tuple[int, int]:
    '''Main'''

    # Read input data
    with open('inputs/day05.txt', 'r') as f:
        inputs = f.read().rstrip("\n")

    # Solve the problem
    part1 = runpart1(inputs)
    part2 = runpart2(inputs)

    return (part1, part2)

if __name__ == '__main__':
    print(run())

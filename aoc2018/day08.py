#!/usr/bin/python3
'''Advent of Code 2018 Day 8 solution'''
from typing import Tuple, List

def runsolution(inputs: List[int], ptr: int = 0) -> Tuple[int, int, int]:
    '''Solve both parts'''
    metadatatotal = 0

    # Read node header
    childcount = inputs[ptr]
    metadatacount = inputs[ptr+1]
    ptr += 2

    # Loop through all the children of this node
    childvalues = []

    while childcount:
        childcount -= 1
        (x, y, ptr) = runsolution(inputs, ptr)
        metadatatotal += x
        childvalues.append(y)

    # Metadata value is just the sum of all the metadata values
    metadatatotal += sum(inputs[ptr:ptr+metadatacount])

    # If we have child nodes, calculate the node value from that.
    if childvalues:
        value = 0
        while metadatacount:
            try:
                value += childvalues[inputs[ptr]-1]
            # Ignore metadata that points at non-existent child nodes.
            except IndexError:
                pass
            ptr += 1
            metadatacount -= 1
    # But if we don't have child notes, node value is the same as metadata value
    else:
        value = metadatatotal
        ptr += metadatacount

    return (metadatatotal, value, ptr)

def run() -> Tuple[int, int]:
    '''Main'''

    # Read input data
    with open('inputs/day08.txt', 'r') as f:
        inputs: List[int] = list(map(int, f.readline().split(' ')))

    # Solve the problem
    (part1, part2, _) = runsolution(inputs)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

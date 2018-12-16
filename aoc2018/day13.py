#!/usr/bin/python3
'''Advent of Code 2018 Day 13 solution'''
from typing import TextIO, Any, Dict, List, Tuple, Set
Input = Dict[str, Any]
Coords = Tuple[int, int]
Cart = Tuple[int, int, int, int]
def up(z: Coords, c: Cart, inputs: Input) -> Cart:
    '''Move cart up'''
    if inputs['map'][z[0]][z[1]] == '|':
        return (z[0], z[1], 0, c[3])
    if inputs['map'][z[0]][z[1]] == chr(92):
        return (z[0], z[1], 3, c[3])
    if inputs['map'][z[0]][z[1]] == r'/':
        return (z[0], z[1], 1, c[3])
    if inputs['map'][z[0]][z[1]] == '+':
        (a, b) = [(3, 1), (0, 2), (1, 0)][c[3]]
        return (z[0], z[1], a, b)
    raise Exception

def right(z: Coords, c: Cart, inputs: Input) -> Cart:
    '''Move cart right'''
    if inputs['map'][z[0]][z[1]] == '-':
        return (z[0], z[1], 1, c[3])
    if inputs['map'][z[0]][z[1]] == chr(92):
        return (z[0], z[1], 2, c[3])
    if inputs['map'][z[0]][z[1]] == r'/':
        return (z[0], z[1], 0, c[3])
    if inputs['map'][z[0]][z[1]] == '+':
        (a, b) = [(0, 1), (1, 2), (2, 0)][c[3]]
        return (z[0], z[1], a, b)
    raise Exception

def down(z: Coords, c: Cart, inputs: Input) -> Cart:
    '''Move cart down'''
    if inputs['map'][z[0]][z[1]] == '|':
        return (z[0], z[1], 2, c[3])
    if inputs['map'][z[0]][z[1]] == chr(92):
        return (z[0], z[1], 1, c[3])
    if inputs['map'][z[0]][z[1]] == r'/':
        return (z[0], z[1], 3, c[3])
    if inputs['map'][z[0]][z[1]] == '+':
        (a, b) = [(1, 1), (2, 2), (3, 0)][c[3]]
        return (z[0], z[1], a, b)
    raise Exception

def left(z: Coords, c: Cart, inputs: Input) -> Cart:
    '''Move cart left'''
    if inputs['map'][z[0]][z[1]] == '-':
        return (z[0], z[1], 3, c[3])
    if inputs['map'][z[0]][z[1]] == chr(92):
        return (z[0], z[1], 0, c[3])
    if inputs['map'][z[0]][z[1]] == r'/':
        return (z[0], z[1], 2, c[3])
    if inputs['map'][z[0]][z[1]] == '+':
        (a, b) = [(2, 1), (3, 2), (0, 0)][c[3]]
        return (z[0], z[1], a, b)
    raise Exception

def tick(inputs: Input) -> List[Tuple[Any, Any, int, Any]]:
    '''Process one time tick'''
    carts = inputs['carts']
    carts.sort()
    newcarts = []
    cartlocations: Set[Coords] = set()
    crashlocations: Set[Coords] = set()
    for c in carts:
        z = (c[0], c[1])
        cartlocations.add(z)
    for c in carts:
        if (c[0], c[1]) not in crashlocations:
            z = [((c[0]-1, c[1]), up),
                 ((c[0], c[1]+1), right),
                 ((c[0]+1, c[1]), down),
                 ((c[0], c[1]-1), left)][c[2]]
            if z[0] in cartlocations:
                crashlocations.add(z[0])
            else:
                newcarts.append(z[1](z[0], c, inputs))
        cartlocations.remove((c[0], c[1]))
    return newcarts

def runpart1(inputs: Input) -> Coords:
    '''Solve part one'''
    while True:
        newcarts = tick(inputs)
        cartlocations: Set[Coords] = set()
        for c in newcarts:
            z = (c[0], c[1])
            if z in cartlocations:
                return (z[1], z[0])
            cartlocations.add(z)
        inputs['carts'] = newcarts

def runpart2(inputs: Input) -> Coords:
    '''Solve part two'''
    while True:
        newcarts = tick(inputs)
        newcarts2 = []
        cartlocations: Set[Coords] = set()
        crash = set()
        for c in newcarts:
            z = (c[0], c[1])
            if z in cartlocations:
                crash.add(z)
            else:
                cartlocations.add(z)
        for c in newcarts:
            z = (c[0], c[1])
            if z not in crash:
                newcarts2.append(c)
        inputs['carts'] = newcarts2
        if len(newcarts2) == 1:
            return(newcarts2[0][1], newcarts2[0][0])
        if not newcarts2:
            raise Exception("Ran out of carts")

def readinputdata(f: TextIO) -> Input:
    '''Read input data from the given file handle into inputs'''
    inputs: Input = {'map': [], 'carts': []}

    x = y = 0
    for line in f.readlines():
        lineout = ''
        x = 0
        for c in line:
            if c in r' /\-|+':
                lineout += c
            elif c == '^':
                inputs['carts'].append((y, x, 0, 0))
                lineout += '|'
            elif c == '>':
                inputs['carts'].append((y, x, 1, 0))
                lineout += '-'
            elif c == 'v':
                inputs['carts'].append((y, x, 2, 0))
                lineout += '|'
            elif c == '<':
                inputs['carts'].append((y, x, 3, 0))
                lineout += '-'
            x += 1
        inputs['map'].append(lineout)
        y += 1

    return inputs

def run() -> Tuple[Coords, Coords]:
    '''Main'''
    with open('inputs/day13.txt', 'r') as f:
        inputs = readinputdata(f)

    return(runpart1(inputs), runpart2(inputs))

if __name__ == '__main__':
    print(run())

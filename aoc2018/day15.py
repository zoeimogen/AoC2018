#!/usr/bin/python3
'''Advent of Code 2018 Day 15 solution'''
import copy
from typing import TextIO, Tuple, Union, List, Set
Unit = List[int]
Input = Tuple[List[Unit], List[str]]
Coords = Tuple[int, int]

# def printgrid(inputs):
#     for y in range(len(inputs['map'])):
#         end = []
#         for x in range(len(inputs['map'][y])):
#             unit = [z for z in inputs['units'] if (z[0], z[1]) == (y, x)]
#             if unit:
#                 print(unit[0][2], end='')
#                 end.append("%s(%d)" % (unit[0][2], unit[0][4]))
#             else:
#                 print(inputs['map'][y][x], end='')
#         print("   %s" %(', '.join(end)))

def findmove(unit: Unit, inputs: Input) -> Union[None, Tuple[int, int]]:
    '''Find and make available moves for a unit'''
    q = []
    locations = set((z[0], z[1]) for z in inputs[0] if z[2] != unit[2])
    blocked = set((z[0], z[1]) for z in inputs[0] if z[2] == unit[2])
    for z in [(unit[0]+1, unit[1]), (unit[0]-1, unit[1]),
              (unit[0], unit[1]+1), (unit[0], unit[1]-1)]:
        if inputs[1][z[0]][z[1]] != '.' or z in blocked:
            continue # Blocked by wall or Elf.
        elif z in locations:
            return None # Already adjacent to a unit we can attack
        else:
            q.append((z[0], z[1], z[0], z[1]))
    result = []
    p: Set[Coords] = set([(unit[0], unit[1])]) # Locations we visited last move
    while q:
        q.sort()
        r = [] # Next set of moves to add to the queue
        for c in q:
            for z in [(c[0]+1, c[1]), (c[0]-1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1)]:
                if inputs[1][z[0]][z[1]] != '.' or z in blocked or z in p:
                    continue # Blocked by wall or Elf or we already went here.
                elif z in locations:
                    result.append((c[0], c[1], z[0], z[1], c[2], c[3]))
                else:
                    r.append((z[0], z[1], c[2], c[3]))
                p.add((z[0], z[1]))

        if result:
            result.sort()
            return (result[0][4], result[0][5])
        q = r
    return None

def attack(unit: Unit, inputs: Input) -> None:
    '''Find and attack a unit'''
    targets: List[Unit] = []
    for z in [(unit[0]+1, unit[1]), (unit[0]-1, unit[1]),
              (unit[0], unit[1]+1), (unit[0], unit[1]-1)]:
        for t in [t for t in inputs[0] if t[2] != unit[2]]:
            if (t[0], t[1]) == (z[0], z[1]):
                targets.append(t)
    if targets:
        targets.sort(key=lambda x: (x[4], x[0], x[1]))
        t = targets[0]
        t[4] -= unit[3]
        if t[4] <= 0:
            inputs[0].remove(t)
        return

def runpart1(inputs: Input) -> int:
    '''Solve part one'''
    r = 0
    inputcopy = copy.deepcopy(inputs)
    while True:
        inputcopy[0].sort()
        unitcopy = copy.copy(inputcopy[0])
        for u in unitcopy:
            if u[4] <= 0:
                continue
            move = findmove(u, inputcopy)
            if move:
                u[0] = move[0]
                u[1] = move[1]
            attack(u, inputcopy)
            if (not [(z[0], z[1])
                     for z in inputcopy[0]
                     if z[2]] or
                    not [(z[0], z[1])
                         for z in inputcopy[0]
                         if not z[2]]):
                if unitcopy.index(u) == len(unitcopy)-1:
                    # We actually finished the last move of the turn before ending
                    r += 1
                return r * sum([z[4] for z in inputcopy[0]])
        r += 1

def runpart2rounds(inputs: Input) -> int:
    '''Attempt to solve part 2, if elf power is sufficient'''
    elfcount = len([z for z in inputs[0] if z[2]])
    r = 0
    while True:
        inputs[0].sort()
        unitcopy = copy.copy(inputs[0])
        for u in unitcopy:
            if u[4] <= 0:
                continue
            move = findmove(u, inputs)
            if move:
                u[0] = move[0]
                u[1] = move[1]
            attack(u, inputs)
            if len([z for z in inputs[0] if z[2]]) < elfcount:
                return 0
            if not [z for z in inputs[0] if not z[2]]:
                if unitcopy.index(u) == len(unitcopy)-1:
                    # We actually finished the last move of the turn before ending
                    r += 1
                return r * sum([z[4] for z in inputs[0]])
        r += 1

def runpart2(inputs: Input) -> int:
    '''Soove part two'''
    power = 3
    while True:
        inputcopy = copy.deepcopy(inputs)
        for z in [z for z in inputcopy[0] if z[2]]:
            z[3] = power
        result = runpart2rounds(inputcopy)
        if result:
            return result
        power += 1

def readinputdata(f: TextIO) -> Input:
    '''Read input data from the given file handle into inputs'''
    inputs: Input = ([], [])

    x = y = 0
    for line in f.readlines():
        out = ''
        x = 0
        for c in line:
            if c in r'#.':
                out += c
            elif c in 'EG':
                inputs[0].append([y, x, int(c == 'E'), 3, 200])
                out += '.'
            x += 1
        inputs[1].append(out)
        y += 1

    return inputs

def run() -> Tuple[int, int]:
    '''Main'''
    with open('inputs/day15.txt', 'r') as f:
        inputs = readinputdata(f)

    return(runpart1(inputs), runpart2(inputs))

if __name__ == '__main__':
    print(run())

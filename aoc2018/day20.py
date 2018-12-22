#!/usr/bin/python3
'''Advent of Code 2018 Day 20 solution'''
from typing import Dict, Tuple, Union

Grid = Dict[Tuple[int, int], int]

move_map = {'E': (1, 0),
            'W': (-1, 0),
            'N': (0, -1),
            'S': (0, 1)}

def move(string: str, x: int = 0, y: int = 0, dist: int = 0,
         grid: Union[Grid, None] = None) -> Tuple[int, int]:
    '''Try moves from a substring'''
    if grid is None:
        grid = {}
    ptr = 0
    (curr_x, curr_y, curr_dist) = (x, y, dist)
    while ptr < len(string):
        if string[ptr] == '(':
            optr = ptr
            ptr += 1
            nest = 0
            while True:
                if string[ptr] == ')':
                    if not nest:
                        substring = string[optr+1:ptr]
                        move(substring, curr_x, curr_y, curr_dist, grid)
                        break
                    else:
                        nest -= 1
                elif string[ptr] == '(':
                    nest += 1
                ptr += 1
        elif string[ptr] == '|':
            (curr_x, curr_y, curr_dist) = (x, y, dist)
        else:
            m = move_map[string[ptr]]
            (curr_x, curr_y, curr_dist) = (curr_x + m[0], curr_y + m[1], curr_dist + 1)
            if (curr_x, curr_y) not in grid or curr_dist < grid[(curr_x, curr_y)]:
                grid[(curr_x, curr_y)] = curr_dist

        ptr += 1

    max_dist = max(grid[z] for z in grid)
    long_way = len([z for z in grid if grid[z] >= 1000])

    return (max_dist, long_way)

def run() -> Tuple[int, int]:
    '''Main'''
    with open('inputs/day20.txt', 'r') as f:
        inputs = f.read().rstrip("$\n").lstrip("^")

    return move(inputs)

if __name__ == '__main__':
    print(run())

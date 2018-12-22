#!/usr/bin/python3
'''Advent of Code 2018 Day 18 solution'''
from typing import Tuple, List, Dict
import numpy
Squares = List[List[int]]
Visited = List[Dict[Tuple[int, int], int]]
Move = Tuple[int, int, int, int]
Queue = List[Move]

def print_erosion(erosion: Squares) -> None:
    '''Print function for debugging'''
    for y in erosion:
        for x in y:
            if x % 3 == 0:
                print('.', end='')
            elif x % 3 == 1:
                print('=', end='')
            else:
                print('|', end='')
        print()

def print_visited(visited: Visited, erosion: Squares) -> None:
    '''Print function for debugging'''
    for y in range(len(erosion)):
        for x in range(len(erosion[0])):
            for eq in [0, 1, 2]:
                if (y, x) in visited[eq]:
                    z = str(visited[eq][(y, x)])
                else:
                    z = '---'
                print('%3s ' % (z), end='')
            print('|', end='')
        print()

def square_type(depth: int, y: int, x: int, erosion: Squares) -> int:
    '''Return the type of a square'''
    if not y:
        geologic = x * 16807
    elif not x:
        geologic = y * 48271
    else:
        geologic = int(erosion[y-1][x]) * int(erosion[y][x-1])
    erosion[y][x] = (geologic + depth) % 20183
    return erosion[y][x] % 3

def runpart1(depth: int, target_y: int, target_x: int) -> int:
    '''Solve part 1'''
    erosion = numpy.empty((target_y+1, target_x+1), dtype=int)
    score = 0
    for y in range(0, target_y+1):
        for x in range(0, target_x+1):
            if y == target_y and x == target_x:
                score += square_type(depth, 0, 0, erosion)
            else:
                score += square_type(depth, y, x, erosion)
    return score

def queue_move(move: Move, visited: Visited, queue: Queue, new_equip: List[int]) -> None:
    '''Queue up moves for given equipment type'''
    for eq in new_equip:
        if eq == move[3]:
            d = move[2] + 1
        else:
            d = move[2] + 8
        coords = (move[0], move[1])
        if coords in visited[eq] and visited[eq][coords] <= d:
            continue
        visited[eq][coords] = d
        queue.append((move[0], move[1], d, eq))

def consider_move(move: Move, visited: Visited, squares: Squares, queue: Queue) -> None:
    '''Consider a move to given coordinates'''
    if move[0] < 0 or move[1] < 0 or move[0] >= len(squares) or move[1] >= len(squares[1]):
        return

    st = squares[move[0]][move[1]]
    if st == 0: # Rocky
        if move[3] != 0: # Need to use something
            queue_move(move, visited, queue, [1, 2])
    elif st == 1: # Wet
        if move[3] != 1: # Need to use climing or nothing
            queue_move(move, visited, queue, [0, 2])
    else: # Narrow
        if move[3] != 2: # Need to use torch or nothing
            queue_move(move, visited, queue, [0, 1])

def runpart2(depth: int, target_y: int, target_x: int) -> int:
    '''Solve part 2'''
    # Queue of moves to test
    queue: Queue = [(0, 0, 0, 1), (0, 0, 7, 2)]
    # Where we've been for each equipment type, and best distance found
    visited: Visited = [{}, {(0, 0): 0}, {(0, 0): 7}]
    overage = 25 # How far to look beyond the target for possible solutions

    erosion = numpy.empty((target_y+overage, target_x+overage), dtype=int)
    squares = numpy.empty((target_y+overage, target_x+overage), dtype=int)
    for y in range(0, target_y+overage):
        for x in range(0, target_x+overage):
            if y == target_y and x == target_x:
                squares[y][x] = square_type(depth, 0, 0, erosion)
            else:
                squares[y][x] = square_type(depth, y, x, erosion)

    while queue:
        queue.sort(key=lambda x: x[2], reverse=True)
        q = queue.pop()
        x = q[1]
        y = q[0]
        for coords in [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]:
            consider_move((coords[0], coords[1], q[2], q[3]), visited, squares, queue)

    return visited[1][(target_y, target_x)]

def run() -> Tuple[int, int]:
    '''Main'''
    return(runpart1(10647, 770, 7), runpart2(10647, 770, 7))

if __name__ == '__main__':
    print(run())

#!/usr/bin/python3
'''Advent of Code 2018 Day 9 solution'''
from typing import Tuple
from blist import blist # pylint: disable=no-name-in-module

def runsolution(players: int, lastmarble: int) -> int:
    '''Solve problem'''
    # This is the key to the speed required to solve part 2 - blist is several orders of magnitude
    # faster when doing an insert on the list, which is the bottleneck of this algorithm.
    circle = blist([0])
    marble = 1
    ptr = 0
    player = 0
    scores = [0 for _ in range(0, players)]

    # Play the game
    while marble <= lastmarble:
        if marble % 23:
            # Normal move
            ptr = (ptr + 2) % len(circle)
            if ptr:
                circle.insert(ptr, marble)
            else:
                # If current marble pointer is zero, we insert at the end - not the beginning
                circle.append(marble)
                ptr = len(circle)-1
        else:
            # Every 23rd move we do the scoring and remove a marble
            scores[player] += marble
            r = ptr - 7
            if r < 0:
                r += len(circle)
            scores[player] += circle.pop(r)
            ptr = r

        # Standard end-of-move postambl common to move turn types.
        marble += 1
        player = (player+1)%players

    # Result is the highest scoring elf.
    return max(scores)

def run() -> Tuple[int, int]:
    '''Main'''
    part1 = runsolution(411, 71170)
    part2 = runsolution(411, 7117000)
    return (part1, part2)

if __name__ == '__main__':
    print(run())

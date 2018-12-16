#!/usr/bin/python3
'''Advent of Code 2018 Day 14 solution'''
from typing import Tuple

def runpart1(improve: int) -> str:
    '''Solve part one'''
    recipelist = [3, 7]
    elfA = 0
    elfB = 1
    while len(recipelist) < (improve + 10):
        newrecipes = str(recipelist[elfA] + recipelist[elfB])
        recipelist += [int(r) for r in newrecipes]
        elfA = (elfA + 1 + recipelist[elfA]) % len(recipelist)
        elfB = (elfB + 1 + recipelist[elfB]) % len(recipelist)
    return ''.join([str(r) for r in recipelist[improve:improve+10]])

def runpart2(finds: str) -> int:
    '''Solve part two'''
    recipelist = '37'
    elfA = 0
    elfB = 1
    while True:
        recipelist += str(int(recipelist[elfA]) + int(recipelist[elfB]))
        elfA = (elfA + 1 + int(recipelist[elfA])) % len(recipelist)
        elfB = (elfB + 1 + int(recipelist[elfB])) % len(recipelist)
        if recipelist[-10:].find(finds) > -1:
            return recipelist.find(finds)

def run() -> Tuple[str, int]:
    '''Main'''
    return(runpart1(635041), runpart2('635041'))

if __name__ == '__main__':
    print(run())

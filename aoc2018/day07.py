#!/usr/bin/python3
'''Advent of Code 2018 Day 4 solution'''
from typing import Tuple, List, DefaultDict, TextIO, Dict, Any
import re
from collections import defaultdict
InputData = Dict[str, DefaultDict[str, List[str]]]

def runpart1(values: InputData) -> str:
    '''Run solution - both parts drop out of the same loop'''
    queue = [a for a in values['forward'].keys() if a not in values['back']]
    output = ''
    while queue:
        q = [a for a in queue if all([b in output for b in values['back'][a]])]
        q.sort()
        item = q.pop(0)
        queue.remove(item)
        output += item
        queue = queue + [i for i in values['forward'][item] if i not in queue]
    return output

def runpart2(values: InputData, addtime: int, workercount: int) -> int:
    '''Run solution - both parts drop out of the same loop'''
    queue = [a for a in values['forward'].keys() if a not in values['back']]
    workers: List[List[Any]] = [['', 0] for i in range(0, workercount)]
    time = 0
    output = ''

    def getnextitem() -> str:
        nonlocal queue, output
        q = [a for a in queue if all([b in output for b in values['back'][a]])]
        q.sort()
        if not q:
            return ''
        item = q.pop(0)
        queue.remove(item)
        queue = queue + [i for i in values['forward'][item] if i not in queue]
        return item

    while queue or any([w[1] > 0 for w in workers]):
        for w in workers:
            w[1] -= 1
            if w[1] == 0 and w[0] != '':
                output += w[0]

        # This is undoucmented in the puzzle - you can't grab a new item to work on in the same
        # cycle as someone else puts it down, so need a separate loop.
        for w in workers:
            if w[1] < 1:
                w[0] = getnextitem()
                if w[0] != '':
                    w[1] = addtime + 1 + ord(w[0]) - ord('A')

        time += 1

    return time-1

def readinputdata(f: TextIO) -> InputData:
    '''Read input data from the given file handle into inputs'''
    m = re.compile(r'Step (.) must be finished before step (.) can begin\.')
    inputs: InputData = {'forward': defaultdict(list),
                         'back': defaultdict(list)}

    for line in f.readlines():
        z = m.match(line)
        if z is not None:
            inputs['forward'][z.group(1)].append(z.group(2))
            inputs['back'][z.group(2)].append(z.group(1))
    return inputs

def run() -> Tuple[str, int]:
    '''Main'''
    with open('inputs/day07.txt', 'r') as f:
        inputs = readinputdata(f)
    part1 = runpart1(inputs)

    with open('inputs/day07.txt', 'r') as f:
        inputs = readinputdata(f)
    part2 = runpart2(inputs, 60, 5)

    return(part1, part2)

if __name__ == '__main__':
    print(run())

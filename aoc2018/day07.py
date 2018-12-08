#!/usr/bin/python3
'''Advent of Code 2018 Day 4 solution'''
from typing import Tuple, List, DefaultDict, TextIO, Dict, Any
import re
from collections import defaultdict
InputData = Dict[str, DefaultDict[str, List[str]]]

def runpart1(values: InputData) -> str:
    '''Solve part 1'''
    # Initial queue is all nodes that have child references but no parents
    queue = [a for a in values['forward'].keys() if a not in values['back']]
    output = ''
    # Keep going until the queue is exhausted
    while queue:
        # Short queue is nodes that also have all parents completed (i.e. are in output)
        q = [a for a in queue
             if a not in values['back'] or all([b in output for b in values['back'][a]])]
        # Get alphabetically first node in shortened queue, remove from main queue and
        # add it to output
        q.sort()
        item = q.pop(0)
        queue.remove(item)
        output += item
        # Add children of this completed node to queue
        queue = queue + [i for i in values['forward'][item] if i not in queue]
    return output

def runpart2(values: InputData, addtime: int, workercount: int) -> int:
    '''Solve part 2'''
    # Initial queue is all nodes that have child references but no parents
    queue = [a for a in values['forward'].keys() if a not in values['back']]

    # List to keep track of what our workers are doing. (Node and time countdown)
    workers: List[List[Any]] = [['', 0] for i in range(0, workercount)]
    time = 0
    output = ''

    def getnextitem() -> str:
        '''Gets the next item to work on from the queue'''
        nonlocal queue, output
        # Short queue is nodes that also have all parents completed (i.e. are in output)
        q = [a for a in queue if all([b in output for b in values['back'][a]])]
        # Get alphabetically first node in shortened queue
        q.sort()
        # Entirely possible there's nothing to work on available yet...
        if not q:
            return ''
        # ...but in this case we do have something. First alphabetically first node,
        # remove from main queue
        item = q.pop(0)
        queue.remove(item)
        # Add children of this node to queue
        queue = queue + [i for i in values['forward'][item] if i not in queue]
        return item

    # Run while we still have things in the queue, or any worker is working
    while queue or any([w[1] > 0 for w in workers]):
        # Decrement the timer for all workers, add to output anything that has been completed.
        # (I.e. timer has reached zero)
        for w in workers:
            w[1] -= 1
            if w[1] == 0 and w[0] != '':
                output += w[0]

        # Now find new work for any idle workers, and set their countdown timer
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

    # We keep track of both parents and children of nodes (back and forward)
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
    part2 = runpart2(inputs, 60, 5)

    return(part1, part2)

if __name__ == '__main__':
    print(run())

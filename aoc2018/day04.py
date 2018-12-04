#!/usr/bin/python3
'''Advent of Code 2018 Day 4 solution'''
from typing import Tuple, List, DefaultDict, TextIO
import re
import datetime
import operator
from collections import defaultdict
InputData = List[Tuple[datetime.datetime, str]]

def runsolution(values: InputData) -> Tuple[int, int]:
    '''Run solution - both parts drop out of the same loop'''
    # Current guard on shift
    guard = 0

    # When the guard went to sleep (Initialise using dt object to keep the type checker happy)
    sleepsat = datetime.datetime(1, 1, 1)

    # For each guard, a dict of minutes in which they were asleep and how often
    guardsleeptimes: DefaultDict[int, DefaultDict[int, int]] = defaultdict(lambda: defaultdict(int))

    # Total amount of time each guard spent asleep
    guardsleeptotals: DefaultDict[int, int] = defaultdict(int)

    m = re.compile(r'Guard #(\d+) begins shift')

    # Loop through each input line...
    for v in values:
        # Changing of the Guard
        z = m.match(v[1])
        if z is not None:
            guard = int(z.group(1))
        # Note if a guard fell asleep
        elif v[1] == 'falls asleep':
            sleepsat = v[0]
        # If a guard wakes up...
        elif v[1] == 'wakes up':
            # ...record how long they were asleep...
            guardsleeptotals[guard] += int((v[0] - sleepsat) / datetime.timedelta(minutes=1))
            # ...and increment the counter for each minute slot in which they were asleep
            t = sleepsat
            while t < v[0]:
                guardsleeptimes[guard][t.minute] += 1
                t += datetime.timedelta(minutes=1)

    # The most slept guard is the one with the maximum value in the guardsleeptotals dict.
    mostsleptguard = max(guardsleeptotals.items(), key=operator.itemgetter(1))[0]
    # And now get the most slept minute of that guard.
    mostsleptminute = max(guardsleeptimes[mostsleptguard].items(), key=operator.itemgetter(1))[0]

    # Now solve part 2, using the same output.
    mg = 0
    part2 = 0
    # Loop through each guard...
    for g in guardsleeptimes:
        # ...finding the minute they slept most in...
        mx = max(guardsleeptimes[g].items(), key=operator.itemgetter(1))[0]
        # ...and if that beats the previous record (tracked in mg), update the record and put the
        # answer to part 2 (minute times guard number) into part2.
        if guardsleeptimes[g][mx] > mg:
            mg = guardsleeptimes[g][mx]
            part2 = g * mx

    return(mostsleptguard * mostsleptminute, part2)

def readinputdata(f: TextIO) -> InputData:
    '''Read input data from the given file handle into inputs'''
    m = re.compile(r'\[(1518-\d\d-\d\d \d\d:\d\d)\] (.*)')
    inputs: InputData = []

    for line in f.readlines():
        z = m.match(line)
        if z is not None:
            dt = datetime.datetime.strptime(z.group(1), '%Y-%m-%d %H:%M')
            inputs.append((dt, z.group(2)))

    # Sort the input data chronologically
    inputs.sort(key=lambda x: x[0])

    return inputs

def run() -> Tuple[int, int]:
    '''Main'''

    # Read input data
    with open('inputs/day04.txt', 'r') as f:
        inputs = readinputdata(f)

    # Solve the problem
    return runsolution(inputs)

if __name__ == '__main__':
    print(run())

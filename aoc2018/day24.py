#!/usr/bin/python3
'''Advent of Code 2018 Day 24 solution'''
import re
import math
import copy
from typing import Tuple, TextIO, List, Callable

class Unit: # pylint: disable=too-many-instance-attributes
    '''Represents a unit group'''
    count = 0
    hp = 0
    attack = 0
    attacktype = ''
    initiative = 0
    army = ''
    immune: List[str] = []
    weak: List[str] = []
    armycount = 0

    def effectivepower(self) -> int:
        '''Returns effective attack power of a unit group'''
        return self.attack * self.count

    def __str__(self) -> str:
        '''Cast to str'''
        return "Group %d contains %d units" % (self.armycount, self.count)

Units = List[Unit]

def targetsort(units: Units, u: int) -> Callable[[int], Tuple[int, int, int]]:
    '''Return curried sort order function for targets'''
    return(lambda t: (calculatedamage(units[u], units[t]),
                      units[t].effectivepower(),
                      units[t].initiative))

def calculatedamage(unit: Unit, target: Unit) -> int:
    '''Camculate damage that unit would do to target'''
    if unit.attacktype in target.immune:
        return 0
    if unit.attacktype in target.weak:
        return unit.count * unit.attack * 2
    return unit.count * unit.attack

def calculateattacks(units: Units) -> List[Tuple[int, int]]:
    '''Perform the attack selection stage of a fight'''
    unitlist = list(range(0, len(units)))
    unitlist.sort(key=lambda x: (units[x].effectivepower(), units[x].initiative),
                  reverse=True)
    chosen: List[int] = []
    results = []
    for unit in unitlist:
        if units[unit].count == 0:
            continue
        targets = [t
                   for t in list(range(0, len(units)))
                   if (units[t].army != units[unit].army and
                       t not in chosen and
                       units[t].count != 0)]
        targets.sort(key=targetsort(units, unit), reverse=True)
        if targets and calculatedamage(units[unit], units[targets[0]]) > 0:
            chosen.append(targets[0])
            if calculatedamage(units[unit], units[targets[0]]) >= units[targets[0]].hp:
                # We've attacked the group but only add it to the list if we actually capable of
                # killing some units. This is needed for stalemate detection in part 2.
                results.append((unit, targets[0]))
    return results

def runattacks(attacks: List[Tuple[int, int]], units: Units) -> None:
    '''Run the previously selected attacks'''
    attacks.sort(key=lambda x: units[x[0]].initiative, reverse=True)
    for attack in attacks:
        if units[attack[0]].count == 0:
            continue
        hp = units[attack[1]].hp * units[attack[1]].count
        damage = calculatedamage(units[attack[0]], units[attack[1]])
        remaining = math.ceil((hp - damage) / units[attack[1]].hp)
        if remaining < 0:
            remaining = 0
        units[attack[1]].count = remaining

def readinputdata(f: TextIO) -> Units:
    '''Load input data'''
    units = []
    m1 = re.compile((r'^(\d+) units each with (\d+) hit points (\([^)]+\))? ?'
                     r'with an attack that does (\d+) ([^ ]+) damage at initiative (\d+)$'))
    m2 = re.compile(r'^([A-Za-z ]+):$')
    m3 = re.compile(r'^\((((immune)|(weak)) to ([a-z, ]+); )?(((immune)|(weak)) to ([a-z, ]+)\))?$')

    army = ''
    armycount = 0 # This is the unit number within the army group - used only for debugging.

    for line in f:
        result = m2.match(line)
        if result is not None:
            army = result.group(1)
            armycount = 1
            continue
        result = m1.match(line)
        if result is not None:
            weak: List[str] = []
            immune: List[str] = []

            if result.group(3) is not None:
                defence = m3.match(result.group(3))
                if defence is not None:
                    if defence.group(2) is not None and defence.group(2) == 'immune':
                        immune = defence.group(5).split(', ')
                    if defence.group(7) is not None and defence.group(7) == 'immune':
                        immune = defence.group(10).split(', ')

                    if defence.group(2) is not None and defence.group(2) == 'weak':
                        weak = defence.group(5).split(', ')
                    if defence.group(7) is not None and defence.group(7) == 'weak':
                        weak = defence.group(10).split(', ')

            unit = Unit()
            unit.count = int(result.group(1))
            unit.hp = int(result.group(2))
            unit.attack = int(result.group(4))
            unit.attacktype = result.group(5)
            unit.initiative = int(result.group(6))
            unit.army = army
            unit.immune = immune
            unit.weak = weak
            unit.armycount = armycount
            armycount += 1
            units.append(unit)

    return units

def runfight(inputs: Units) -> Tuple[str, int]:
    '''Run a series of fights'''
    while True:
        attacks = calculateattacks(inputs)
        if not attacks:
            return('Stalemate', 0)
        runattacks(attacks, inputs)
        if not [u for u in inputs if u.army == 'Immune System' and u.count > 0]:
            return ('Infection',
                    sum([u.count
                         for u in inputs
                         if u.army == 'Infection' and u.count > 0]))
        if not [u for u in inputs if u.army == 'Infection' and u.count > 0]:
            return ('Immune',
                    sum([u.count
                         for u in inputs
                         if u.army == 'Immune System' and u.count > 0]))

def runpart1(inputs: Units) -> int:
    '''Solve part 1'''
    inputcopy = copy.deepcopy(inputs)
    return runfight(inputcopy)[1]

def runpart2(inputs: Units) -> int:
    '''Solve part 2'''
    boost = 1
    while True:
        inputcopy = copy.deepcopy(inputs)
        for u in [u for u in inputcopy if u.army == 'Immune System']:
            u.attack += boost
        result = runfight(inputcopy)
        if result[0] == 'Immune':
            return result[1]
        boost += 1

def run() -> Tuple[int, int]:
    '''Main'''
    with open('inputs/day24.txt', 'r') as f:
        inputs = readinputdata(f)

    return(runpart1(inputs), runpart2(inputs))

if __name__ == '__main__':
    print(run())

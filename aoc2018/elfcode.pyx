#!/usr/bin/python3
'''Advent of Code 2018's elf code functions'''

from typing import List, Tuple, Callable, TextIO
import re

State = List[int]
Inputs = Tuple[int, int, int]
Op = Callable[[State, Inputs], None]
DecodedInstruction = Tuple[Op, int, int, int, int]
Program = List[DecodedInstruction]

def noop(_state: State, _inputs: Inputs) -> None:
    '''Dummy placeholder'''

def addr(state: State, inputs: Inputs) -> None:
    '''addr (add register) stores into register C the result of adding register A and register B.'''
    state[inputs[2]] = state[inputs[0]] + state[inputs[1]]

def addi(state: State, inputs: Inputs) -> None:
    '''addi (add immediate) stores into register C the result of adding register A and value B.'''
    state[inputs[2]] = state[inputs[0]] + inputs[1]

def mulr(state: State, inputs: Inputs) -> None:
    ''''mulr (multiply register) stores into register C the result of multiplying register A and
        register B.'''
    state[inputs[2]] = state[inputs[0]] * state[inputs[1]]

def muli(state: State, inputs: Inputs) -> None:
    '''muli (multiply immediate) stores into register C the result of multiplying register A and
       value B.'''
    state[inputs[2]] = state[inputs[0]] * inputs[1]

def banr(state: State, inputs: Inputs) -> None:
    '''banr (bitwise AND register) stores into register C the result of the bitwise AND of register
       A and register B.'''
    state[inputs[2]] = state[inputs[0]] & state[inputs[1]]

def bani(state: State, inputs: Inputs) -> None:
    '''bani (bitwise AND immediate) stores into register C the result of the bitwise AND of
       register A and value B.'''
    state[inputs[2]] = state[inputs[0]] & inputs[1]

def borr(state: State, inputs: Inputs) -> None:
    '''borr (bitwise OR register) stores into register C the result of the bitwise OR of register
       A and register B.'''
    state[inputs[2]] = state[inputs[0]] | state[inputs[1]]

def bori(state: State, inputs: Inputs) -> None:
    '''bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register
       A and value B.'''
    state[inputs[2]] = state[inputs[0]] | inputs[1]

def setr(state: State, inputs: Inputs) -> None:
    '''setr (set register) copies the contents of register A into register C.
       (Input B is ignored.)'''
    state[inputs[2]] = state[inputs[0]]

def seti(state: State, inputs: Inputs) -> None:
    '''seti (set immediate) stores value A into register C. (Input B is ignored.)'''
    state[inputs[2]] = inputs[0]

def gtir(state: State, inputs: Inputs) -> None:
    '''gtir (greater-than immediate/register) sets register C to 1 if value A is greater than
       register B. Otherwise, register C is set to 0.'''
    state[inputs[2]] = int(inputs[0] > state[inputs[1]])

def gtri(state: State, inputs: Inputs) -> None:
    '''gtri (greater-than register/immediate) sets register C to 1 if register A is greater than
       value B. Otherwise, register C is set to 0.'''
    state[inputs[2]] = int(state[inputs[0]] > inputs[1])

def gtrr(state: State, inputs: Inputs) -> None:
    '''gtrr (greater-than register/register) sets register C to 1 if register A is greater than
       register B. Otherwise, register C is set to 0.'''
    state[inputs[2]] = int(state[inputs[0]] > state[inputs[1]])

def eqir(state: State, inputs: Inputs) -> None:
    '''eqir (equal immediate/register) sets register C to 1 if value A is equal to register B.
       Otherwise, register C is set to 0.'''
    state[inputs[2]] = int(inputs[0] == state[inputs[1]])

def eqri(state: State, inputs: Inputs) -> None:
    '''eqri (equal register/immediate) sets register C to 1 if register A is equal to value B.
       Otherwise, register C is set to 0.'''
    state[inputs[2]] = int(state[inputs[0]] == inputs[1])

def eqrr(state: State, inputs: Inputs) -> None:
    '''eqrr (equal register/register) sets register C to 1 if register A is equal to register B.
       Otherwise, register C is set to 0.'''
    state[inputs[2]] = int(state[inputs[0]] == state[inputs[1]])


opcodes = {'noop': noop,
           'addr': addr, 'addi': addi, 'mulr': mulr, 'muli': muli,
           'banr': banr, 'bani': bani, 'borr': borr, 'bori': bori,
           'setr': setr, 'seti': seti, 'gtir': gtir, 'gtri': gtri,
           'gtrr': gtrr, 'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr}

ops: List[Op] = [addr, addi, mulr, muli, banr, bani, borr, bori,
                 setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def readprogram(f: TextIO) -> Program:
    '''Read a program from file'''
    inputs: Program = []
    m1 = re.compile(r'([a-z]+) (\d+) (\d+) (\d+)')
    m2 = re.compile(r'#ip (\d+)')
    ip = 0

    for line in f:
        r = m1.match(line)
        if r is not None:
            inputs.append((opcodes[r.group(1)], ip, int(r.group(2)),
                           int(r.group(3)), int(r.group(4))))
        else:
            r = m2.match(line)
            if r is not None:
                ip = int(r.group(1))

    return inputs

def runprogram(program: Program, reg0: int = 0) -> int:
    '''Run program'''
    state = [reg0, 0, 0, 0, 0, 0]
    ip = 0
    while True:
        state[program[ip][1]] = ip
        program[ip][0](state, program[ip][2:])
        ip = state[program[ip][1]] + 1
        if ip < 0 or ip >= len(program):
            break
    return state[0]

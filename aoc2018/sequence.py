#!/usr/bin/python3
'''Sequence finder code'''

from typing import List, Optional, Tuple

def checksequence(numbers: List[int]) -> Optional[Tuple[int, int]]:
    '''Check to see if a sequence has started repeating.
       Simple check - does not actually verify contents of loop'''
    if len([n for n in numbers if n == numbers[-1]]) >= 3:
        indices = [i for i, n in enumerate(numbers) if n == numbers[-1]][-3:]
        sequence1 = numbers[indices[0]:indices[1]]
        sequence2 = numbers[indices[1]:indices[2]]
        if sequence1 == sequence2:
            return (indices[1], indices[2])

    return None

def predict(numbers: List[int], target: int) -> int:
    '''Predict what a repeating sequence will be at a target index'''
    result = checksequence(numbers)
    if not result:
        raise Exception('Asked to predict with no sequence detected')
    (start, end) = result
    sequence = numbers[start:end]
    offset = (target - start - 1) % len(sequence)
    return sequence[offset]

def predictincrementing(numbers: List[int], target: int) -> int:
    '''Predict what a repeating incrementing sequence will be at a target index'''
    result = checksequence(numbers)
    if not result:
        raise Exception('Asked to predict with no sequence detected')
    (start, end) = result
    sequence = numbers[start:end]
    preamble = sum(numbers[:start])
    cycles = (target - start)
    offset = (target - start) % len(sequence)
    return preamble + ((cycles+2) * sum(sequence)) + sum(sequence[:offset])

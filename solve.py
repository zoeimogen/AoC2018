#!/usr/bin/python3
'''Advent of Code 2018 run all solutions'''

from timeit import timeit

for i in range(1, 10):
    print(' in %.2fs' % (timeit('print("Day %d: ", aoc2018.day%02d.run(), end="")' % (i, i),
                                'import aoc2018.day%02d' % (i),
                                number=1)))

print(' in %.2fs' % (timeit(r'print("Day 10: %d\n%s" % aoc2018.day10.run(), end="")',
                            'import aoc2018.day10',
                            number=1)))

for i in range(11, 24):
    print(' in %.2fs' % (timeit('print("Day %d: ", aoc2018.day%02d.run(), end="")' % (i, i),
                                'import aoc2018.day%02d' % (i),
                                number=1)))

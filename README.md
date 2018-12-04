# Advent of Code 2018 Solutions

Solutions to 2018 problems found at [AdventOfCode.com](https://adventofcode.com/)

To solve a problem with the input data in inputs/dayXX.txt, simply run python aoc2018/dayXX.py.

Tests can be run with unittest:
```
$ python3 -m unittest tests/day01_test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.025s

OK
```

Tests also include the calculation on the full input data, so that it can be profiled. Output is
written to results.txt, which is reset by the day 1 solution.

To run a full test, coverage check (htmlcov/index.html) lint, profile (prof/) and type check use
tox.
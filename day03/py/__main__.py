import os
import re
import functools
from typing import Tuple

_dir = os.path.dirname(__file__)


def read_input(filename):
  inputfile = os.path.join(_dir, '../' + filename)
  with open(inputfile) as f:
    return f.read().splitlines()




def day2(filename, invalid_id_fn):
  print('day 2 part 1: ' + filename)
  ranges = read_input(filename)
  # print(ranges)
  invalid_id_sum = 0
  for start, end in ranges:
    for id in range(int(start), int(end) + 1):
      if invalid_id_fn(id):
        # print(f'invalid id: {id}')
        invalid_id_sum += id
  print(f'Sum of invalid IDs: {invalid_id_sum}')


def day3part1(filename):
  sum = 0
  inputlines = read_input(filename)
  # print(inputlines)
  for line in inputlines:
    digits = [int(x) for x in list(line)]
    print(digits)
    # find max first digit (exclude last digit)
    max1 = max(digits[:-1])
    pos1 = digits[:-1].index(max1)
    print(f'{max1=} {pos1=}')
    max2 = max(digits[pos1+1:])
    pos2 = pos1 + digits[pos1:].index(max2)
    print(f'{max2=} {pos2=}')
    max_joltage = max1 * 10 + max2
    print(f'{max_joltage=}')
    sum += max_joltage
  print(f'{sum=}')


if __name__ == '__main__':
  # day3part1('example.txt')
  day3part1('input.txt')
  # day3part2('input.txt')

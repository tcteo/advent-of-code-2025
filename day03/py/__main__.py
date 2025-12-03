import os
import re
import functools
from typing import Tuple
import numpy as np

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
    # print(digits)
    # find max first digit (exclude last digit)
    max1 = max(digits[:-1])
    pos1 = digits[:-1].index(max1)
    # print(f'{max1=} {pos1=}')
    max2 = max(digits[pos1+1:])
    pos2 = pos1 + digits[pos1:].index(max2)
    # print(f'{max2=} {pos2=}')
    bank_max_joltage = max1 * 10 + max2
    # print(f'{max_joltage=}')
    sum += bank_max_joltage
  print(f'{sum=}')

def day3part2(filename):
  sum = 0
  inputlines = read_input(filename)
  # print(inputlines)
  for line in inputlines:
    # print(line)
    digits = [int(x) for x in list(line)]
    maxvalue = day3part2_max(digits, 12)
    # print(f'line {maxvalue=}')
    sum += maxvalue
  print(f'{sum=}')

# def sum_digits(digits):
#   tens = [10**n for n in range(0,len(digits))][::-1]
#   return sum([x[0]*x[1] for x in zip(digits,tens)])

def day3part2_max(digits, length):
  # print(f'day3part2_max({digits}, {length}):')
  if len(digits)<=0:
    raise RuntimeError("too short")
  if len(digits)<length:
    raise RuntimeError("too short")
  
  range_max = len(digits)
  while True:
    max_idx = np.argmax(digits[:range_max])
    max_val = digits[max_idx]
    if length==1:
      return max_val * (10**(length-1))
    try:
      r = day3part2_max(digits[max_idx+1:], length-1)
      return max_val * (10**(length-1)) + r
    except RuntimeError:
      range_max = max_idx

  # return sum_digits(digits) # TODO


if __name__ == '__main__':
  # day3part1('example.txt')
  # day3part1('input.txt')
  # day3part2('example.txt')
  day3part2('input.txt')

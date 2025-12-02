import os
import re
import functools
from typing import Tuple

_dir = os.path.dirname(__file__)


def read_input(filename):
  # returns a list of 2-tuples
  inputfile = os.path.join(_dir, '../' + filename)
  with open(inputfile) as f:
    input = f.read().strip()
    ranges = input.split(',')
    r = [tuple(a.split('-')) for a in ranges]
  return r


re_invalid_id = re.compile(r'(\d+)\1$')


def invalid_id_part1(id: int) -> bool:
  digits = str(id)
  if re_invalid_id.match(digits):
    return True
  return False


@functools.cache
def generate_regexes(n):
  res = []
  for i in range(1, n + 1):
    re_str = r'(\d+)' + r'\1' * i + r'$'
    res.append(re.compile(re_str))
  return res


def invalid_id_part2(id: int) -> bool:
  digits = str(id)
  regexes = generate_regexes(len(digits))
  for r in regexes:
    if r.match(digits):
      return True
  return False


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


def day2part1(filename):
  return day2(filename, invalid_id_part1)


def day2part2(filename):
  return day2(filename, invalid_id_part2)


if __name__ == '__main__':
  # day2part1('example.txt')
  day2part1('input.txt')
  day2part2('input.txt')

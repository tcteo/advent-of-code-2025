import os
import re
from typing import Tuple

_dir = os.path.dirname(__file__)


def read_input(filename):
  # returns a list of 2-tuples
  inputfile = os.path.join(_dir, '../'+filename)
  with open(inputfile) as f:
    input = f.read().strip()
    ranges = input.split(',')
    r = [tuple(a.split('-')) for a in ranges]
  return r


re_invalid_id = re.compile(r'(\d+)\1$')
def invalid_id(id: int) -> bool:
  digits = str(id)
  if re_invalid_id.match(digits):
    return True
  return False
  


def day2part1(filename):
  print('day 2 part 1: '+filename)
  ranges = read_input(filename)
  # print(ranges)
  invalid_id_sum = 0
  for start, end in ranges:
    for id in range(int(start), int(end)+1):
      if invalid_id(id):
        # print(f'Invalid ID: {id}')
        invalid_id_sum += id
  print(f'Sum of invalid IDs: {invalid_id_sum}')




if __name__ == '__main__':
  day2part1('example.txt')
  day2part1('input.txt')
  # day2part2()

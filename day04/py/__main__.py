import os
import re
import functools
from typing import Tuple
import numpy as np
import pprint
import scipy.signal

_dir = os.path.dirname(__file__)

def read_input(filename):
  inputfile = os.path.join(_dir, '../' + filename)
  with open(inputfile) as f:
    chararr = [list(x.strip()) for x in f.read().splitlines()]
  
  lookup = {'.': 0, '@': 1}
  binarray = [[
    lookup[elem] for elem in row
  ] for row in chararr]
  
  return np.array(binarray, dtype=np.int8)
  


def day4part1(filename):
  print(f'day 4 part 1: {filename}')
  matrix = read_input(filename)
  # pprint.pprint(matrix)
  k = np.array([[1,1,1],[1,0,1],[1,1,1]], dtype=np.int8)
  # pprint.pprint(k)
  c = scipy.signal.convolve2d(matrix, k, mode='same')
  # pprint.pprint(c)

  c_lt4 = c < 4
  yes = np.multiply(c_lt4, matrix)
  # pprint.pprint(yes)
  lt4_count = np.sum(yes)
  # pprint.pprint(np.reshape(matrix, (-1)))

  # pprint.pprint(roll_neighbour_counts)
  # lt4 = sum([(x<4) for r in roll_neighbour_counts for x in r])
  print(f'rolls with less than 4 neighbours: {lt4_count}')



if __name__ == '__main__':
  day4part1('example.txt')
  day4part1('input.txt')
  # day4part2('example.txt')
  # day4part2('input.txt')

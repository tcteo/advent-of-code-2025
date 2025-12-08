import os
import re
import numpy as np
import functools

_dir = os.path.dirname(__file__)


def read_input(filename):
  inputfile = os.path.join(_dir, '../' + filename)
  with open(inputfile, 'rt') as f:
    lines = f.readlines()
    lines = [re.sub(r' +', ' ', l.strip()) for l in lines]
  operators = lines[-1].split(' ')

  digits = [ [int(x) for x in l.split(' ')] for l in lines[:-1]]

  digits = np.array(digits).T
  return digits, operators

opfns = {
  # operator_char: (fn, reduce_init_value)
  '*': (lambda x,y: x*y, 1),
  '+': (lambda x,y: x+y, 0),
}
def op(digits, operator):
  fn, initvalue = opfns[operator]
  return functools.reduce(fn, digits, initvalue)
  

def day6part1(filename):
  print(f'day 6 part 1: {filename}')
  digits, operators = read_input(filename)

  d_o = zip(digits, operators)
  res = [op(*c) for c in d_o]
  print(f'ans {np.sum(res)}')
  # print(res)

def day6part2(filename):
  print(f'day 6 part 2: {filename}')


if __name__ == '__main__':
  # day6part1('example.txt')
  day6part1('input.txt')
  # print('--')
  # day6part2('example.txt')
  # day6part2('input.txt')

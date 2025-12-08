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

def remove_newline(s):
  if s.endswith('\n'):
    return s[:-1]
  return s

def digits_to_int(dlist):
  n = ''.join(dlist).strip()
  if not n:
    return None
  return int(n)


def read_input2(filename):
  inputfile = os.path.join(_dir, '../' + filename)
  with open(inputfile, 'rt') as f:
    lines = f.readlines()
    lines = [remove_newline(s) for s in lines]

  m = [list(l) for l in lines]
  mt = np.array(m).T
  # return mt.tolist()
  numbers = [digits_to_int(x) for x in mt[:,:-1]]
  numbers.append(None)
  operators = re.sub(r' +', ' ', ''.join(mt[:,-1]).strip()).split(' ')
  # print('numbers:', numbers)
  # print('operators:', operators)
  return numbers, operators
  
def day6part2(filename):
  print(f'day 6 part 2: {filename}')
  numbers, operators = read_input2(filename)
  oi = 0
  a = []
  res = []
  for i in numbers:
    if i is None:
      # do math
      opchar = operators[oi]
      fn, initvalue = opfns[opchar]
      res.append(
        functools.reduce(fn, a, initvalue)
      )
      # then clear
      a = []
      oi += 1
    else:
      # append
      a.append(i)
  # print(res)

  print(f'ans {np.sum(res)}')
  


if __name__ == '__main__':
  # day6part1('example.txt')
  day6part1('input.txt')
  # print('--')
  # day6part2('example.txt')
  day6part2('input.txt')

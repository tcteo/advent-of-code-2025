import os
from typing import Tuple

_dir = os.path.dirname(__file__)


def read_input():
  input = os.path.join(_dir, '../input.txt')

  with open(input) as f:
    lines = [l.strip() for l in f.read().splitlines() if l]

  rotations: Tuple[int, int] = []
  for l in lines:
    direction = {'L': -1, 'R': 1}[l[0]]
    distance = int(l[1:])
    rotations.append((direction, distance))

  return rotations
  
def day1part1():
  print('day 1 part 1')
  rotations = read_input()
  password = 0
  pos = 50
  for direction, distance in rotations:
    pos += (direction * distance)
    pos = pos % 100
    if pos == 0:
      password += 1
  print(f'{password=}')

def day1part2():
  print('day 1 part 1')
  rotations = read_input()
  password = 0
  pos = 50
  for direction, distance in rotations:
    for _ in range(distance):
      pos += direction
      pos = pos % 100
      if pos == 0:
        password += 1
  print(f'{password=}')


if __name__ == '__main__':
  day1part1()
  day1part2() 
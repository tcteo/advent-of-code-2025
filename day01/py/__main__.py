import os
from typing import Tuple

_dir = os.path.dirname(__file__)


def main():
  print('in main')
  input = os.path.join(_dir, '../input.txt')
  print(input)

  with open(input) as f:
    lines = [l.strip() for l in f.read().splitlines() if l]

  print(lines)

  rotations: Tuple[int, int] = []
  for l in lines:
    direction = {'L': -1, 'R': 1}[l[0]]
    distance = int(l[1:])
    rotations.append((direction, distance))

  password = 0
  pos = 50
  for direction, distance in rotations:
    pos += (direction * distance)
    pos = pos % 100
    if pos == 0:
      password += 1
  print(f'{password=}')


if __name__ == '__main__':
  main()

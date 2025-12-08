import os


_dir = os.path.dirname(__file__)


def read_input(filename):
  inputfile = os.path.join(_dir, '../' + filename)


def day6part1(filename):
  print(f'day 6 part 1: {filename}')


def day6part2(filename):
  print(f'day 6 part 2: {filename}')


if __name__ == '__main__':
  day6part1('example.txt')
  # day6part1('input.txt')
  # print('--')
  day6part2('example.txt')
  # day6part2('input.txt')

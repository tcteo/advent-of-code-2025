import os

_dir = os.path.dirname(__file__)

def read_input(filename):
  inputfile = os.path.join(_dir, '../' + filename)
  fresh_ranges = []
  avail_ids = []
  f = True
  with open(inputfile) as f:
    for l in f.readlines():
      l = l.strip()
      if not l: # blank line
        f = False
        continue
      if f:  # fresh ranges
        r = tuple([int(s) for s in l.split('-')])
        fresh_ranges.append(r)
      else:  # avail ids
        a = int(l)
        avail_ids.append(a)
  
  return fresh_ranges, avail_ids


def day5part1(filename):
  print(f'day 5 part 1: {filename}')
  fresh_ranges, avail_ids = read_input(filename)
  # print(f'{fresh_ranges}')
  # print(f'{avail_ids}')

  def in_ranges(ranges, aid):
    for r in ranges:
      if aid>=r[0] and aid <=r[1]:
        return True
    return False

  fresh = [in_ranges(fresh_ranges, a) for a in avail_ids]
  n_fresh = sum(fresh)

  print(f'avail fresh {n_fresh}')

def day5part2(filename):
  print(f'day 5 part 2: {filename}')
  matrix = read_input(filename)


if __name__ == '__main__':
  # day5part1('example.txt')
  day5part1('input.txt')
  # print('--')
  # day5part2('example.txt')
  # day5part2('input.txt')

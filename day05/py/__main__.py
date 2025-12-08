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
      if not l:  # blank line
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
      if aid >= r[0] and aid <= r[1]:
        return True
    return False

  fresh = [in_ranges(fresh_ranges, a) for a in avail_ids]
  n_fresh = sum(fresh)

  print(f'avail fresh {n_fresh}')


def day5part2_bruteforce(filename):
  print(f'day 5 part 2 brute force: {filename}')
  fresh_ranges, _ = read_input(filename)

  freshids = set()
  for r in fresh_ranges:
    for i in range(r[0], r[1] + 1):
      freshids.add(i)
  print(sorted(freshids))
  print(f'{len(freshids)=}')


class Range:
  def __init__(self, min, max):
    assert min <= max
    self.min = min
    self.max = max

  def union(self, other):  # non-overlapping
    if (self.max < other.min) or (other.max < self.min):  # non-overlapping
      ret = [self, other]
    # overlap
    elif self.min <= other.min and other.max <= self.max:
      ret = [self]
    elif other.min <= self.min and self.max <= other.max:
      ret = [other]
    elif other.min <= self.min and other.max <= self.max:
      ret = [Range(other.min, self.max)]
    elif self.min <= other.min and self.max <= other.max:
      ret = [Range(self.min, other.max)]
    else:
      raise RuntimeError(f'{self} + {other} = ???!??!')

    print(f'{self} + {other} => {ret}')
    return ret

  def overlap(self, other):
    if (self.max < other.min) or (other.max < self.min):  # non-overlapping
      return False
    return True

  def size(self):
    return self.max - self.min + 1

  def __str__(self):
    return f'Range({self.min},{self.max})'

  def __repr__(self):
    return str(self)

  def __hash__(self):
    return self.min * int(1e20) + self.max

  def __lt__(self, other):
    if self.min < other.min:
      return True
    if self.min > other.min:
      return False
    if self.max < other.max:
      return True
    if self.max > other.max:
      return False
    return False


def day5part2(filename):
  print(f'day 5 part 2: {filename}')
  fresh_ranges, _ = read_input(filename)
  ranges = [Range(*r) for r in fresh_ranges]

  last_t = None
  ranges = sorted(ranges)
  # print(ranges)

  rr = []
  cr = None
  for i in range(0, len(ranges)):
    r = ranges[i]
    if cr == None:
      cr = r
      continue
    if r.overlap(cr):
      cr = Range(min(r.min, cr.min), max(r.max, cr.max))
      continue
    rr.append(cr)
    cr = r
  rr.append(cr)

  for r in sorted(rr):
    print(f'{r}: {r.size()}')
  t = sum([s.size() for s in rr])
  print(t)


if __name__ == '__main__':
  # day5part1('example.txt')
  # day5part1('input.txt')
  # print('--')
  # day5part2_bruteforce('example.txt')
  # day5part2('example.txt')
  day5part2('input.txt')

import os


_dir = os.path.dirname(__file__)


def read_input(filename):
  inputfile = os.path.join(_dir, '../' + filename)
  with open(inputfile, 'rt') as f:
    lines = [l.strip() for l in f.readlines()]
    lines = [l.replace('.', ' ') for l in lines]
  return lines

def positions(s, c):
  return [i for (i,x) in enumerate(list(s)) if x==c]

def transform_input(lines):
  source_loc = None
  splitter_locs = [] # list of lists [layer][positions]
  for li, l in enumerate(lines):
    if li==0:
      source_loc = l.index('S')
    else:
      if not l.strip():
        continue
      splitter_locs.append(positions(l, '^'))
  return source_loc, splitter_locs

def eval_beams(source_loc, splitter_locs):
  # returns (beam_locs, num_splits)
  num_splits = 0
  beam_locs = set([source_loc])

  for si, splitters in enumerate(splitter_locs):
    # update beam_locs
    # find beams that match splitter locs
    sb = [n for n in beam_locs if n in splitters]
    # remove split beams
    for sbi in sb:
      beam_locs.remove(sbi)
    # new beam locations
    nb = set()
    for sbi in sb:
      nb.add(sbi-1)
      nb.add(sbi+1)
      num_splits += 1
    for b in beam_locs:
      nb.add(b)
    beam_locs = nb
    
    print(f'after layer {si}: beam_locs: {beam_locs}')
    print(f'{num_splits=}')


def day7part1(filename):
  print(f'day 7 part 1: {filename}')
  lines = read_input(filename)
  source_loc, splitter_locs = transform_input(lines)
  print(f'{source_loc=}')
  print(f'{splitter_locs=}')

  eval_beams(source_loc, splitter_locs)


def day7part2(filename):
  print(f'day 7 part 2: {filename}')


if __name__ == '__main__':
  # day7part1('example.txt')
  day7part1('input.txt')
  # print('--')
  # day7part2('example.txt')
  # day7part2('input.txt')

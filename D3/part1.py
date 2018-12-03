import re

puzzleInput = open('input.txt', 'r').read().split('\n')

overlaps = {} 

for row in puzzleInput:
  id, left, top, width, height = map(lambda x: int(x), re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', row).groups())
  for w in range(width):
    for h in range(height):
      coords = (left + w, top + h)
      if coords not in overlaps:
        overlaps[coords] = 0
      
      overlaps[coords] += 1

result = len(filter(lambda x: x >= 2, overlaps.itervalues()))

print 'Result: %s' % result
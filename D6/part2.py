import re
import numpy as np

puzzleInput = open('input.txt', 'r').read().split('\n')

coords = map(lambda x: re.match(r'(\d+), (\d+)', x).groups(), puzzleInput)
coords = map(lambda (x, y): (int(x), int(y)), coords)
bounds = (max(map(lambda c: c[0], coords)), max(map(lambda c: c[1], coords)))

def distance(p):
  xp, yp = p
  return sum(map(lambda (x, y): abs(xp - x) + abs(yp - y), coords))

bx, by = bounds
limit = 10000
areaSize = 0
for y in range(by+1):
  for x in range(bx+1):
    if distance((x, y)) < limit:
      areaSize+=1

result = areaSize

print 'Result: %s' % result
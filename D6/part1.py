import re
import numpy as np

puzzleInput = open('input.txt', 'r').read().split('\n')

coords = map(lambda x: re.match(r'(\d+), (\d+)', x).groups(), puzzleInput)
coords = map(lambda (x, y): (int(x), int(y)), coords)
bounds = (max(map(lambda c: c[0], coords)), max(map(lambda c: c[1], coords)))

def getDistance(a, b):
  ax, ay = a
  bx, by = b
  return abs(ax - bx) + abs(ay - by)

def getMinPoint(refPoint):
  distList = map(lambda p: getDistance(p, refPoint), coords)
  minDist = min(distList)
  if len(filter(lambda d: d == minDist, distList)) > 1:
    return -1
  else:
    return np.argmin(distList)

bx, by = bounds
areas = {}
infiniteAreas = set()
for y in range(by+1):
  for x in range(bx+1):
    minPoint = getMinPoint((x, y))
    if minPoint != -1:
      if x == 0 or x == bx-1 or y == 0 or y == by-1:
        infiniteAreas.add(minPoint)
      if minPoint not in areas:
        areas[minPoint] = 0
      areas[minPoint]+=1

result = max([v for k, v in areas.iteritems() if k not in infiniteAreas])

print 'Result: %s' % result
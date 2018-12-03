import re

puzzleInput = open('input.txt', 'r').read().split('\n')

overlaps = {} 

mapClaim = lambda claim: map(lambda x: int(x), re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim).groups())

def iterClaim(left, top, width, height): 
  for w in range(width):
    for h in range(height):
      yield (left + w, top + h)

for row in puzzleInput:
  id, left, top, width, height = mapClaim(row)
  for coords in iterClaim(left, top, width, height):
    if coords not in overlaps:
      overlaps[coords] = 0
    overlaps[coords] += 1 

for row in puzzleInput:
  id, left, top, width, height = mapClaim(row)
  if all(map(lambda coords: overlaps[coords] == 1, iterClaim(left, top, width, height))):
    result = id

print 'Result: %s' % result

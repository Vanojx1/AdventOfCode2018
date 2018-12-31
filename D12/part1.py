import re

puzzleInput = open('input.txt', 'r').read()

pots = re.match(r'initial state: ([#\.]+)', puzzleInput).group(1)
pots = { i:v for i, v in enumerate(pots) }

notes = re.findall(r'([#\.]+) => ([#\.])', puzzleInput)
notes = { k:v for k, v in notes }

def getPotState(potIndex):
  def getChar():
    for i in range(-2, 3, 1):
      if potIndex+i in pots:
        yield pots[potIndex+i]
  return ''.join(getChar())

total = 0
for gen in range(20):
  # print 'P:', ''.join(map(lambda x: pots[x], sorted(pots.keys())))
  minPotIndex = min(pots.keys())
  maxPotIndex = max(pots.keys())
  for i in range(minPotIndex-1,  minPotIndex-6, -1):
    pots[i] = '.'
  for i in range(maxPotIndex+1,  maxPotIndex+6):
    pots[i] = '.'
  nextPots = {}
  for i in sorted(pots.keys()):
    pState = getPotState(i)
    if pState in notes:
      nextPots[i]=notes[pState]
    else:
      nextPots[i]='.'
  clearPots = dict(nextPots)
  for i in sorted(nextPots.keys()):
    if nextPots[i] == '.':
      del clearPots[i]
    else:
      break
  for i in reversed(sorted(nextPots.keys())):
    if nextPots[i] == '.':
      del clearPots[i]
    else:
      break
  # print 'N: '+''.join(map(lambda x: clearPots[x], sorted(clearPots.keys())))
  pots = clearPots
  total=sum([k for k, v in pots.iteritems() if v == '#'])
  # print '--------------------------------'

result = total

print 'Result: %s' % result
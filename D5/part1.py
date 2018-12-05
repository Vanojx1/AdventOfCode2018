import re
from cStringIO import StringIO

puzzleInput = open('input.txt', 'r').read()

fattyRegex = []
for index in range(26):
  l = chr(97 + index)
  fattyRegex.append('%s%s|%s%s' % (l, l.upper(), l.upper(), l))
fattyRegex = '|'.join(fattyRegex)

def react(polymer):
  newPolymer = re.sub(fattyRegex, '', polymer)
  if len(newPolymer) != len(polymer):
    return react(newPolymer)
  else:
    return newPolymer

result = len(react(puzzleInput))

print 'Result: %s' % result
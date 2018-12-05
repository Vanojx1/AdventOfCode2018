import re, sys

sys.setrecursionlimit(10000)

puzzleInput = open('input.txt', 'r').read()

fattyRegex = []
for index in range(26):
  l = chr(97 + index)
  fattyRegex.append('%s%s|%s%s' % (l, l.upper(), l.upper(), l))
fattyRegex = '|'.join(fattyRegex)

def react(polymer):
  newPolymer = re.sub(fattyRegex, '', polymer)
  if newPolymer != polymer:
    return react(newPolymer)
  else:
    return newPolymer

result = min(map(lambda i: len(react(re.sub(chr(97 + i), '', puzzleInput, 0, re.IGNORECASE))), range(26)))

print 'Result: %s' % result
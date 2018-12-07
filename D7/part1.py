import re
import numpy as np

puzzleInput = open('input.txt', 'r').read().split('\n')

instructions = map(lambda i: re.findall(r' (\w) ', i), puzzleInput)

priors = {}
for (A, B) in instructions:
  if A not in priors:
    priors[A] = 0
  if B not in priors:
    priors[B] = 0
  priors[A]+=1
  priors[B]-=1

def comparator((ka, va), (kb, vb)):
  if va == vb:
    if kb > ka:
      return -1
    else:
      return 1 
  else:
    return vb - va

print instructions
print ''.join(map(lambda (k, v): k, sorted(priors.iteritems(), cmp=comparator)))


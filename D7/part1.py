import re

puzzleInput = open('input.txt', 'r').read().split('\n')

instructions = map(lambda i: re.findall(r' (\w) ', i), puzzleInput)

steps = {}
for a, b in instructions:
  if b not in steps:
    steps[b] = set()
  steps[b].add(a)

def todo(currSteps):
  t = set()
  if isinstance(currSteps, dict):
    for k, v in currSteps.iteritems():
      if len(v) == 0:
        t.add(k)
      else:
        t = t | todo(list(v))
  else:
    for k in currSteps:
      if k not in steps:
        t.add(k)
  return t

result  = ''
curr = todo(steps)
while len(curr) > 0:
  ck = sorted(curr).pop(0)
  result += ck
  steps = { k: v for k, v in steps.iteritems() if len(v) > 0 }
  for k, v in steps.iteritems():
    steps[k] = steps[k].difference(set(ck))
  curr = todo(steps)

print 'Result: %s' % result
import re

NUM_WORKERS = 5
ACTION_TIME = 60
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

started = set()

def removeSteps(step):
  global steps
  global started
  started = started.difference(set(step))
  steps = { k: v for k, v in steps.iteritems() if len(v) > 0 }
  for k, v in steps.iteritems():
    steps[k] = steps[k].difference(set(step))

workers = map(lambda x: None, range(NUM_WORKERS))
result = 0
while any(map(lambda w: w is not None, workers)) or steps != {}:
  idle = True
  for i, _ in enumerate(workers):

    if workers[i] is not None:
      workers[i]['t'] -= 1
      idle = False

    nextSteps = sorted(todo(steps).difference(started))
    if len(nextSteps) > 0:
      ck = nextSteps.pop(0)
    else:
      ck = None

    if workers[i] is None and ck is not None:
      workers[i] = { 't': ord(ck) - 64 + ACTION_TIME, 'l': ck }
      started.add(ck)
    elif workers[i] and workers[i]['t'] == 0:
      removeSteps(workers[i]['l'])
      workers[i] = None
      nextSteps = sorted(todo(steps).difference(started))
      if len(nextSteps) > 0:
        nextStep = nextSteps.pop(0)
        workers[i] = { 't': ord(nextStep) - 64 + ACTION_TIME, 'l': nextStep }
        started.add(nextStep)
      else:
        workers[i] = None

  if not idle:
    result += 1

print 'Result: %s' % result
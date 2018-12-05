import re
import json
from datetime import datetime
from collections import Counter

puzzleInput = open('input.txt', 'r').read().split('\n')


def mapper(row):
    m = re.search(
        r'\[(?P<time>[0-9\- :]+)\]\s+(Guard #(?P<guard>\d+))?(?P<wakeup>wakes up)?(?P<asleep>falls asleep)?', row)
    if m.group('wakeup'):
        action = 'WAKEUP'
    elif m.group('asleep'):
        action = 'ASLEEP'
    else:
        action = 'SHIFT'
    return {
        'time': datetime.strptime(m.group('time'), '%Y-%m-%d %H:%M'),
        'action': action,
        'guard': m.group('guard')
    }


mappedInput = map(mapper, puzzleInput)
sortedInput = sorted(mappedInput, key=lambda x: x['time'])

currGuard = None
start = None
whoSleep = {}

for row in sortedInput:
    currMinute = row['time'].minute
    if row['action'] == 'SHIFT':
        currGuard = row['guard']
    elif row['action'] == 'ASLEEP':
        start = currMinute
    elif row['action'] == 'WAKEUP':
        for m in range(currMinute - start):
            if (start + m) not in whoSleep:
                whoSleep[start + m] = []
            whoSleep[start + m].append(currGuard)

arrayfied = [dict(minute=key, who=[dict(guard=k, times=v) for k, v in Counter(
    value).iteritems()]) for key, value in whoSleep.iteritems()]

maxMinuteSleeping = 0
sleepyGuard = None
for minute in arrayfied:
  currMaxTimes = max(minute['who'], key=lambda x: x['times'])
  if currMaxTimes['times'] > maxMinuteSleeping:
    maxMinuteSleeping = currMaxTimes['times']
    maxMinute = { 'guard': currMaxTimes['guard'], 'minute': minute['minute'] }

result = int(maxMinute['guard']) * int(maxMinute['minute'])

print 'Result: %s' % result
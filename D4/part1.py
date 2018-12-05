import re
import json
from datetime import datetime

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
sleepTimes = {}
for row in sortedInput:
    currMinute = row['time'].minute
    if row['action'] == 'SHIFT':
        currGuard = row['guard']
    elif row['action'] == 'ASLEEP':
        if currGuard not in sleepTimes:
            sleepTimes[currGuard] = 0
        sleepTimes[currGuard] -= currMinute
        start = currMinute
    elif row['action'] == 'WAKEUP':
        sleepTimes[currGuard] += currMinute
        for m in range(currMinute - start):
            if (start + m) not in whoSleep:
                whoSleep[start + m] = []
            whoSleep[start + m].append(currGuard)

arrayfied = [dict(guard=key, slept=value)
             for key, value in sleepTimes.iteritems()]

mostSleepy = max(arrayfied, key=lambda x: x['slept'])

maxTimes = 0
maxMinute = None
for minute, who in whoSleep.iteritems():
    l = len(filter(lambda x: x == mostSleepy['guard'], who))
    if l > maxTimes:
        maxTimes = l
        maxMinute = minute

result = int(mostSleepy['guard']) * int(maxMinute)

print 'Result: %s' % result

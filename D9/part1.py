import re
from collections import deque, defaultdict

puzzleInput = open('input.txt', 'r').read()

playersNum, score = map(lambda x: int(x), re.match(r'(\d+)[^\d]*(\d+)', puzzleInput).groups())

players = defaultdict(int)
circle = deque([0])
for marble in range(1, score+1):
  if marble % 23 == 0:
    circle.rotate(7)
    players[marble % playersNum] += marble + circle.pop()
    circle.rotate(-1)
  else:
    circle.rotate(-1)
    circle.append(marble)

result = max(players.values())

print 'Result: %s' % result
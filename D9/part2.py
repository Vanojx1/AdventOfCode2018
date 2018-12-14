import re

puzzleInput = open('input.txt', 'r').read()

playersNum, score = map(lambda x: int(x), re.match(r'(\d+)[^\d]*(\d+)', puzzleInput).groups())

def printC(player, circle, index):
  print ('[%s] ' % (player+1)) + ' '.join(map(lambda (i, x): '(%s)' % x if i == index else str(x), enumerate(circle))), index

circle = [0]
currMarbleIndex = 0
players = map(lambda x: 0, range(playersNum))
for i in range(score):
  oneAfter = (currMarbleIndex+1) % len(circle)
  twoAfter = (currMarbleIndex+2) % len(circle)
  nextMarble = i+1
  playerIndex = i % playersNum
  if nextMarble % 23 == 0:
    currMarbleIndex = (currMarbleIndex-7) % len(circle)
    rM = circle.pop(currMarbleIndex)
    players[playerIndex] += rM + nextMarble
    # printC(playerIndex, circle, currMarbleIndex)
    continue
  elif oneAfter >= twoAfter:
    circle.append(nextMarble)
  else:
    circle.insert(twoAfter, nextMarble)
  currMarbleIndex = circle.index(nextMarble)
  # printC(playerIndex, circle, currMarbleIndex)

result =  max(players)

print 'Result: %s' % result
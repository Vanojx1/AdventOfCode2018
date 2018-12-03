puzzleInput = open('input.txt', 'r').read().split('\n')

found = False
i = 0
currFreq = 0
freqs = set()
while not found:
  el = puzzleInput[i % len(puzzleInput)]
  currFreq += int(el)
  if currFreq in freqs:
    found = currFreq
  else:
    freqs.add(currFreq)
  i+=1

print 'Result: %s' % found

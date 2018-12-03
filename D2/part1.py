from collections import Counter

puzzleInput = open('input.txt', 'r').read().split('\n')

found2 = found3 = 0

for row in puzzleInput:
  c = Counter(row)
  found2 += 1 if 2 in c.values() else 0
  found3 += 1 if 3 in c.values() else 0

checksum = found2 * found3

print 'Result: %s' % checksum

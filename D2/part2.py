puzzleInput = open('input.txt', 'r').read().split('\n')

def diff(str1, str2):
  return map(lambda (k, l): l, filter(lambda (i, v): str1[i] != str2[i], enumerate(min(str1, str2))))

def equals(str1, str2):
  return map(lambda (k, l): l, filter(lambda (i, v): str1[i] == str2[i], enumerate(min(str1, str2))))

for str1 in puzzleInput:
  for str2 in puzzleInput:
    if len(diff(str1, str2)) == 1:
      result = ''.join(equals(str1, str2))

print 'Result: %s' % result
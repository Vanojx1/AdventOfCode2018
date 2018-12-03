puzzleInput = open('input.txt', 'r').read().split('\n')

result = sum(map(lambda x: int(x), puzzleInput))

print 'Result: %s' % result
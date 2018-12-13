import re

puzzleInput = open('input.txt', 'r').read()

rawTree = map(lambda n: int(n), re.findall(r'\d+', puzzleInput))

class Tree():
  cursor = -1
  metaSum = 0

  class Node():
    def __init__(self, id=0):
      self.id = id
      self.tree = Tree
      self.startIndex = self.tree.next()
      self.metaIndex = self.tree.next()
      self.childs = self.getChilds()
      self.meta = self.getMeta()
      self.tree.metaSum += reduce(lambda c, v: c+v, self.meta, 0)
    
    def getChilds(self):
      childNum = rawTree[self.startIndex]
      return map(lambda c: self.tree.Node(self.id+c+1), range(childNum))

    def getMeta(self):
      metaNum = rawTree[self.metaIndex]
      return map(lambda c: rawTree[self.tree.next()], range(metaNum))

  def __init__(self):
    self.root = self.Node()
  
  @classmethod
  def next(self):
    self.cursor+=1
    return self.cursor

tree = Tree()

result = tree.metaSum

print 'Result: %s' % result
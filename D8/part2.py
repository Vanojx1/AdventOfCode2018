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
    
    @property
    def value(self):
      return reduce(lambda c, v: c+v, self.meta, 0)

    def getChilds(self):
      childNum = rawTree[self.startIndex]
      return map(lambda c: self.tree.Node(self.id+c+1), range(childNum))

    def getMeta(self):
      metaNum = rawTree[self.metaIndex]
      return map(lambda c: rawTree[self.tree.next()], range(metaNum))

    def processMeta(self):

      def processChild(metaIndex):
        if metaIndex in range(len(self.childs)):
          return self.childs[metaIndex].processMeta()
        else:
          return 0

      if len(self.childs) == 0:
        return self.value
      else:
        return reduce(lambda c, v: c+v, map(lambda c: processChild(c-1), self.meta), 0)

  def __init__(self):
    self.root = self.Node()
  
  @classmethod
  def next(self):
    self.cursor+=1
    return self.cursor

tree = Tree()

result = tree.root.processMeta()

print 'Result: %s' % result
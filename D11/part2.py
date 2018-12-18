import numpy as np
import os, json

class FuelCell():
  def __init__(self, serial, x, y):
    self.serial = serial
    self.x = x
    self.y = y
  
  @property
  def value(self):
    rackID = self.x+10
    power = rackID*self.y
    power+=self.serial
    power*=rackID
    try:
      return int(str(power)[-3])-5
    except:
      return -5

class FuelGrid():
  def __init__(self, serial):
    self.grid = {}
    for y in range(1, 301):
      self.grid[y] = {}
      for x in range(1, 301):
        self.grid[y][x] = FuelCell(serial, x, y).value
  def __getitem__(self, key):
    return self.grid[key]

  def maxCell(self):
    matrix = np.matrix(map(lambda x: map(lambda y: y, x.values()), self.grid.values()))
    maxPower = 0
    maxpowerCell = None
    for y in range(300): 
      for x in range(300):
        for n in range(1, 301):
          if y+n < 300 and x+n < 300:
            cMax = matrix[y:y+n, x:x+n].sum()
            if cMax > maxPower:
              maxPower = cMax
              maxpowerCell = (x+1, y+1, n)
    return maxpowerCell

grid = FuelGrid(5719)
result = '%s,%s,%s' % grid.maxCell()

print 'Result: %s' % result
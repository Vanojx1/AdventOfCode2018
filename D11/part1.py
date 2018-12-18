import numpy as np

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
  
  def get3x3Power(self, x, y):
    power = 0
    for yy in range(3):
      for xx in range(3):
        if y+yy <= 300 and x+xx <= 300:
          power+=self.grid[y+yy][x+xx]
    return power

  def maxCell(self):
    maxPower = 0
    maxpowerCell = None
    for y in range(1, 301):
      for x in range(1, 301):
        power = self.get3x3Power(x, y)
        if power > maxPower:
          maxPower = power
          maxpowerCell = (x, y)
    return maxpowerCell

grid = FuelGrid(5719)
result = '%s,%s' % grid.maxCell()

print 'Result: %s' % result
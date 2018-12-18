import re, os
from time import sleep

class Point():
  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
  
  def move(self):
    self.x+=self.vx
    self.y+=self.vy
  
  @property
  def position(self):
    return (self.x, self.y)
  
  def __repr__(self):
    return '(%s,%s)' % (self.x, self.y)

class Sky():
  def __init__(self):
    self.sky_limit = 800
    puzzleInput = open('input.txt', 'r').read().split('\n')
    self.points = map(lambda (x, y, vx, vy): Point(x, y, vx, vy), \
      map(lambda r: map(lambda i: int(i), re.findall(r'-?\d+', r)), puzzleInput))

  def render(self):
    os.system('cls')
    pMatrix = ''
    mx, my = min(map(lambda p: p.x, self.points)), \
      min(map(lambda p: p.y, self.points))
    Mx, My = max(map(lambda p: p.x, self.points)), \
      max(map(lambda p: p.y, self.points))

    for y in reversed(range(My, my-1, -1)):
      for x in reversed(range(Mx, mx-1, -1)):
        if (x, y) in self:
          pMatrix += '#'
        else:
          pMatrix += '.'
      pMatrix += '\n'
    print pMatrix
  
  def move(self):
    for point in self.points:
      point.move()

  @property
  def size(self):
    mx, my = min(map(lambda p: p.x, self.points)), \
      min(map(lambda p: p.y, self.points))
    Mx, My = max(map(lambda p: p.x, self.points)), \
      max(map(lambda p: p.y, self.points))
    
    return (Mx - mx) * (My - my)

  def __contains__(self, key):
    for p in self.points:
      if (p.x, p.y) == key:
        return True
    return False 


sky = Sky()

lastSize = None
while lastSize is None or lastSize > sky.size:
  lastSize = sky.size
  sky.move()
  if sky.size < 3000:
    sky.render()
    sleep(1)
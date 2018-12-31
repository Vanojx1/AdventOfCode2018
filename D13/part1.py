import pygame
import numpy as np
from collections import deque

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GRAY = (221,221,221)

puzzleInput = open('input.txt', 'r').read().split('\n')
mineGrid = map(lambda x: list(x), puzzleInput)

def getTrackSize(x, y):
  width = 1
  height = 1
  i = 0
  while mineGrid[y][x+i] != '\\':
    width+=1
    i+=1
  j=0
  while mineGrid[y+j][x+i] != '/':
    height+=1
    j+=1
  return (width, height)

def drawTrack(track, screen, wratio, hratio):
  origin = track['origin']
  size  = track['size']

  coords = [
    [origin[0], origin[1]],
    [origin[0]+size[0]-1, origin[1]],
    [origin[0]+size[0]-1, origin[1]+size[1]-1],
    [origin[0], origin[1]+size[1]-1]
  ]

  pygame.draw.polygon(
    screen, 
    GRAY, 
    np.multiply(coords, (wratio, hratio)),
    3)

tracks = []
for y, row in enumerate(mineGrid):
  for x, col in enumerate(row):
    cell = mineGrid[y][x]
    if cell == '/' and \
      x+1 < len(mineGrid[y]) and mineGrid[y][x+1] in ['+', '-', '<', '>'] and \
      y+1 < len(mineGrid) and mineGrid[y+1][x] in ['+', '|', '^', 'v']:
      tracks.append({
        'origin': (x, y),
        'size': getTrackSize(x, y)
      })

maxW = 0
maxH = 0
for track in tracks:
  cw, ch = (track['origin'][0]+track['size'][0], track['origin'][1]+track['size'][1])
  if cw > maxW:
    maxW = cw
  if ch > maxH:
    maxH = ch

pygame.init()

screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("AOC2018 DAY 13")

carts = {}
for y, row in enumerate(mineGrid):
  for x, col in enumerate(row):
    if col in ['<', '>', '^', 'v']:
      orderedDir = list(reversed([(0, -1), (1, 0), (0, 1), (-1, 0)]))
      if col == '<':
        cartDir = (-1, 0)
      elif col == '>':
        cartDir = (1, 0)
      elif col == '^':
        cartDir = (0, -1)
      elif col == 'v':
        cartDir = (0, 1)
      carts[(x, y)] = (deque(map(lambda x: orderedDir[orderedDir.index(cartDir)-x], range(4))), deque('LFR'))

FPS=60
done=False
crashed=False
clock = pygame.time.Clock()
while not done:

  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done=True

  screen.fill(WHITE)

  sw, sh = pygame.display.get_surface().get_size()
  wratio, hratio = sw/float(maxW), sh/float(maxH)

  for track in tracks:
    drawTrack(track, screen, wratio, hratio)

  for (x, y), (dirs, interDir) in sorted(carts.iteritems(), key=lambda (k, v): k):
    
    if (x, y) not in carts:
      continue
    
    del carts[(x, y)]

    if not crashed:
      dx, dy = dirs[0]
      currCell = mineGrid[y][x]
      if currCell == '\\':
        if dx != 0:
          dirs.rotate(-1)
        else:
          dirs.rotate(1)
      elif currCell == '/':
        if dx != 0:
          dirs.rotate(1)
        else:
          dirs.rotate(-1)
      elif currCell == '+':
        nextInterDir = interDir[0]
        if nextInterDir == 'L':
          dirs.rotate(1)
        elif nextInterDir == 'R':
          dirs.rotate(-1)
        interDir.rotate(-1)
      dx, dy = dirs[0]

      nextPos = (x+dx, y+dy)

      if nextPos in carts:
        crashed = nextPos
        result = nextPos
        del carts[nextPos]
        continue
    else:
      nextPos = (x, y)

    coords = [
      nextPos[0]*wratio-1.5,
      nextPos[1]*hratio-1.5,
      3,
      3
    ]
    pygame.draw.rect(
      screen,
      BLACK,
      coords)
  
    carts[nextPos] = (dirs, interDir)

  if crashed:
    coords = [
      crashed[0]*wratio-1.5,
      crashed[1]*hratio-1.5,
      3,
      3
    ]
    pygame.draw.rect(
      screen,
      RED,
      coords)

  pygame.display.flip()
    

print 'Result: %s,%s' % result
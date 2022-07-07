from operator import ge
import sys

import pygame
from pygame.locals import *
from Generator import Generator
from GameManager import GameManager
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
  
# Game loop.
gen = Generator(screen,True)
gM = GameManager(gen)
while True:
  screen.fill((0, 0, 0))
  events = pygame.event.get()
  for event in events:
    if event.type == QUIT:
      if(len(gM.savedStates) > 0):
        with open('states.txt', 'w') as f:
          f.write(str(gM.savedStates))
      pygame.quit()
      sys.exit()
  
  # Update.
  gM.update(events)
  # Draw.
  gM.draw()
  pygame.display.flip()
  fpsClock.tick(fps)
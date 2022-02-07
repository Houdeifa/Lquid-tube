import sys
import random

import pygame
from pygame.locals import *
from Tube import Tube
from Selector import Selector
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
widthBoxes = (width * 5) / 9
tube_boxes = []
ColorMatrix = []
Sel = []
def getRandomIndex():
    return int(random.random() * 12)
def generateRandomMatrix():
    ColorMat = []
    for i in range(12):
        l = []
        for j in range(4):
            l.append(0)
        ColorMat.append(l)
    choosedColors = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(12):
        for j in range(4):
            n = getRandomIndex()
            m = 0
            while choosedColors[n] >= 4:
                n = getRandomIndex()
                m = m + 1
                if(m > 100):
                    break
            choosedColors[n] = choosedColors[n] + 1
            ColorMat[i][j] = n;
            #print("n : " + str(n))
            #print("m : " + str(m))
            #print("choosedColors : " + str(choosedColors))
            #print("ColorMat : " + str(ColorMat))
    return ColorMat
def assignColors(ColorMatrix_s, tube_boxes_s):
    for i in range(12):
        tube_boxes_s[i].colors = ColorMatrix_s[i]

def init():
    w = widthBoxes / 8
    h = height/ 5
    x = 0
    y = 0
    for i in range(7*2):
        if(i < 7):
            x = w * i + (w / 7) * i + w / 14 + (width - widthBoxes) /2
            y = h * 1.5
        else:
            x = w * (i - 8) + (w / 7) * i + w / 14 + (width - widthBoxes) /2
            y = h * 3
        tube_boxes.append(Tube(i,w,h,x,y))
    ColorMatrix = generateRandomMatrix()
    assignColors(ColorMatrix, tube_boxes)
    Sel.append(Selector(tube_boxes[0].width/2,tube_boxes[0].height/6, tube_boxes[0].x + tube_boxes[0].width/4 , tube_boxes[0].y - tube_boxes[0].height/3))
    
def eventListner(events):
    pos = pygame.mouse.get_pos()
    for i in range(7*2):
        if tube_boxes[i].isHover(pos) and Sel[0].selected == []:
            Sel[0].setPos(tube_boxes[i].x,tube_boxes[i].y)
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            print("clicked")
            print("--------------------------------------------")
            Unselect_bool = False
            for i in range(7*2):
                if tube_boxes[i].isHover(pos):
                    tube_boxes[i].sel()
                    print("str(tube_boxes[i].selected) = " + str(tube_boxes[i].selected))
                    print("str(Sel[0].selected) = " + str(Sel[0].selected))
                    if(tube_boxes[i].selected != -1):
                        Sel[0].setPos(tube_boxes[i].x,tube_boxes[i].y)
                        Unselect_bool = True
                    played = False
                    if(Sel[0].selected == []):
                        Sel[0].select((tube_boxes[i].selected,tube_boxes[i]))
                    else:
                        print("putColor test")
                        if tube_boxes[i].putColor(Sel[0].selected[0][0]):
                            print("str(Sel[0].selected[0][1].index) = " + str(Sel[0].selected[0][1].index))
                            print("i = " + str(i))
                            tube_boxes[Sel[0].selected[0][1].index].removeColor()
                            Unselect_bool = False
                            tube_boxes[i].unsel()
                            tube_boxes[Sel[0].selected[0][1].index].unsel()
                            Sel[0].unselect()
                            played = True
                    if(played == False):
                        Sel[0].select((tube_boxes[i].selected,tube_boxes[i]))
            if not Unselect_bool:
                Sel[0].unselect()
                tube_boxes[i].unsel()
                print("unselected")
            print("str(tube_boxes[i].selected) = " + str(tube_boxes[i].selected))
            print("str(Sel[0].selected) = " + str(Sel[0].selected))
def update(events):
    for i in range(7*2):
        tube_boxes[i].check()
    eventListner(events)
 
def draw():
    for i in range(7*2):
        tube_boxes[i].draw(screen)
    Sel[0].draw(screen)
 
# Game loop.
init()
while True:
  screen.fill((0, 0, 0))
  events = pygame.event.get()
  for event in events:
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  update(events)
  # Draw.
  draw()
  pygame.display.flip()
  fpsClock.tick(fps)
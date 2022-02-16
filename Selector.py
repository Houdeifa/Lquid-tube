
from asyncio.windows_events import NULL
import pygame
class Selector:
  def __init__(self,w,h,x,y):
    self.width = w
    self.height = h
    self.x = x
    self.y = y
    self.isSelected = False
    self.selectedColor = -1
    self.selectedTube = NULL
  def draw(self,surface):
    coord = [(self.x,self.y), (self.x+self.width,self.y),(self.x+self.width/2,self.y+self.height)]
    pygame.draw.polygon(surface, (255,255,255), coord)
  def setPos(self,x,y):
    self.x = x + self.width/2 
    self.y = y - self.height * 2
  def select(self,selection_pair_C_T):
    selected_tube_class_str = str(type(selection_pair_C_T[1]))
    if(selection_pair_C_T[0] >=0 and selection_pair_C_T[0] < 14 and selected_tube_class_str == "<class 'Tube.Tube'>"):
        self.isSelected = True
        self.selectedColor, self.selectedTube = selection_pair_C_T
  def unselect(self):
    self.isSelected = False
    self.selectedColor, self.selectedTube = (-1, NULL)

import pygame
class Selector:
  def __init__(self,w,h,x,y):
    self.width = w
    self.height = h
    self.x = x
    self.y = y
    self.selected = []
  def draw(self,surface):
    coord = [(self.x,self.y), (self.x+self.width,self.y),(self.x+self.width/2,self.y+self.height)]
    pygame.draw.polygon(surface, (255,255,255), coord)
  def setPos(self,x,y):
    self.x = x + self.width/2 
    self.y = y - self.height * 2
  def select(self,selection):
    str_sel = str(type(selection[1]))
    if(selection[0] >=0 and selection[0] < 14 and str_sel == "<class 'Tube.Tube'>"):
        self.selected = []
        self.selected.append(selection)
  def unselect(self):
    self.selected = []
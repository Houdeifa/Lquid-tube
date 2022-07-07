
import pygame
class Tube:
  
  def __init__(self,i,w,h,x,y):
    self.index = i
    self.width = w
    self.height = h
    self.x = x
    self.y = y
    self.colors = [-1,-1,-1,-1]
    self.NBlockToPlay = 0
    self.NBlockSelected = 0
    self.outer = w/10
    self.bg = (x+self.outer,y,w-(self.outer*2),h-(self.outer))
    self.colorsX = (self.bg[0] + self.outer/2,self.bg[1],self.bg[2] - self.outer,(self.bg[3] - self.outer*2)/4)
    #      0      1     2      3        4          5          6      7     8     9     10          11
    # violet, jaune, gris, orange, marron, bleu ciel, vert bleu, rouge, bleu, vert , rose, vert claire
    self.ColorsArray = ((83, 0, 150),(251, 255, 0), (150, 150, 150),(255, 123, 0),(92, 44, 0),(0, 194, 224),(0, 255, 191),(255, 47, 0),(13, 0, 255),(0, 82, 18),(255, 0, 157), (112, 255, 105))
    self.canPlay = -2 #-2 = cant play , -1 can play any color, other = color that can play
    self.selectedColor = -1 #-1 = not selected, other = color that is selected
  
  
  def playingCheck(self):
        if(self.colors[0] != -1):
            self.canPlay = -2
            self.blockNumberToPlay = 0
            return
        if(self.colors[1] != -1):
            self.canPlay = self.colors[1]
            self.blockNumberToPlay = 1
            return
        if(self.colors[2] != -1):
            self.canPlay = self.colors[2]
            self.blockNumberToPlay = 2
            return
        if(self.colors[3] != -1):
            self.canPlay = self.colors[3]
            self.blockNumberToPlay = 3
            return
        self.canPlay = -1
        self.NBlockToPlay = 4
        
  def sel(self):
    if(self.colors[3] == -1):
        self.selectedColor = -1
        self.NBlockSelected = 0
        return
    if(self.colors[2] == -1):
        self.selectedColor = self.colors[3]
        self.NBlockSelected = 1
        return
    if(self.colors[1] == -1):
        if(self.colors[2] == self.colors[3]):
            self.NBlockSelected = 2
        else :
            self.NBlockSelected = 1
        self.selectedColor = self.colors[2]
        return
    if(self.colors[0] == -1):
        if(self.colors[1] == self.colors[2] and self.colors[2] == self.colors[3]):
            self.NBlockSelected = 3
        elif (self.colors[1] == self.colors[2]):
            self.NBlockSelected = 2
        else:
            self.NBlockSelected = 1
        self.selectedColor = self.colors[1]
        return
    if(self.colors[0] == self.colors[1] and self.colors[1] == self.colors[2] and self.colors[2] == self.colors[3]):
        self.NBlockSelected = 4
    elif (self.colors[0] == self.colors[1] and self.colors[1] == self.colors[3]):
        self.NBlockSelected = 3
    elif (self.colors[0] == self.colors[1]):
        self.NBlockSelected = 2
    else:
        self.NBlockSelected = 1
    self.selectedColor = self.colors[0]
  def unsel(self):
    self.selectedColor = -1
    self.NBlockSelected = 0
  def setColors(self,C1,C2,C3,C4):
    self.colors = [C1,C2,C3,C4]
    
  def removeColors(self,n):
        if(self.colors[3] == -1):
            return
        if(self.colors[2] == -1):
            self.colors[3] = -1
            return
        if(self.colors[1] == -1):
            m = min(2,n)
            for i in range(m):
                self.colors[2+i] = -1
            return
        if(self.colors[0] == -1):
            m = min(3,n)
            for i in range(m):
                self.colors[1+i] = -1  
            return
        m = min(4,n)
        for i in range(m):
            self.colors[i] = -1  
  def canPutColors(self,C,n):
        if(self.colors[0] != -1):
            return False
        if(self.colors[1] == C and n == 1):
            return True
        if(self.colors[1] != -1):
            return False
        if(self.colors[2] == C and n <= 2):
            return True
        if(self.colors[2] != -1):
            return False
        if(self.colors[3] == C  and n <= 3):
            return True
            
        if(self.colors[3] != -1):
            return False
        if( n <= 4):
            return True

  def putColors(self,C,n):
        if(self.colors[0] != -1):
            return False
        if(self.colors[1] == C and n == 1):
            self.colors[0] = C
            return True
        if(self.colors[1] != -1):
            return False
        if(self.colors[2] == C and n <= 2):
            for i in range(n):
                self.colors[1-i] = C
            return True
        if(self.colors[2] != -1):
            return False
        if(self.colors[3] == C  and n <= 3):
            for i in range(n):
                self.colors[2-i] = C
            return True
            
        if(self.colors[3] != -1):
            return False
        if( n <= 4):
            for i in range(n):
                self.colors[3-i] = C
            return True
        return True
  def draw(self,screen):
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x, self.y, self.width, self.height))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.bg[0], self.bg[1], self.bg[2], self.bg[3]))
    for i in range(4):
        if(self.colors[i] >= 0):
            pygame.draw.rect(screen, self.ColorsArray[self.colors[i]], pygame.Rect(self.colorsX[0], self.colorsX[1] + self.colorsX[3]*i + (self.outer/2)*i, self.colorsX[2], self.colorsX[3]))
            
  def isHover(self,mousePos):
        if(mousePos[0] > self.x and mousePos[1] > self.y and mousePos[0] < (self.x + self.width) and mousePos[1] < (self.y + self.height)):
            return True
        else:
            return False
        

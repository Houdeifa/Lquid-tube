
import pygame
import os
class UI:
    def __init__(self,screen,gen) -> None:
        self.screen = screen
        self.gen = gen
        self.backButtonImg = pygame.image.load('images/back-svg.png')
    def createBackButton(self):
        width, height =  self.screen.get_size()
        scale = 1.5
        w = width / 21.33333333333333 * scale
        h = height / 16  * scale
        pos = (int(width-w-(width / 22)),int((height / 16)))
        self.backButtonRect = [pos,w,h]
        self.backButtonImg = pygame.transform.scale(self.backButtonImg, (w,h))
    def drawBackButton(self):
         self.screen.blit(self.backButtonImg, self.backButtonRect[0])
    def isBackBHovred(self,mousePos : tuple):
        if(mousePos[0] < self.backButtonRect[0][0]) :
            return False
        if(mousePos[1] < self.backButtonRect[0][1]) :
            return False
        if(mousePos[0] > (self.backButtonRect[0][0] + self.backButtonRect[1])) :
            return False
        if(mousePos[1] > (self.backButtonRect[0][1] + self.backButtonRect[2])) :
            return False
        return True
    def draw(self):
        self.drawBackButton()
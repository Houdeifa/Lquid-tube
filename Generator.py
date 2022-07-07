from Tube import Tube
from Selector import Selector
from pygame.locals import *
import random
import csv


class Generator:
    Sel = []
    def __init__(self,screen,getConfigFile=False):
        width, height = screen.get_size()
        self.screen = screen
        self.widthBoxes = (width * 5) / 9
        self.tube_boxes = []
        self.ColorMatrix = []
        w = self.widthBoxes / 8
        h = height/ 5
        x = 0
        y = 0
        for i in range(7*2):
            if(i < 7):
                x = w * i + (w / 7) * i + w / 14 + (width - self.widthBoxes) /2
                y = h * 1.5
            else:
                x = w * (i - 8) + (w / 7) * i + w / 14 + (width - self.widthBoxes) /2
                y = h * 3
            self.tube_boxes.append(Tube(i,w,h,x,y))
            if(getConfigFile == True):
                file = open('colors.csv')
                csvreader = csv.reader(file)
                row_counter = 0
                ColorMatrix = []
                for row in csvreader:
                    row = row[0].split(';')
                    for col_index in range(12):
                        ColorMatrix.append([])
                        ColorMatrix[col_index].append(int(row[col_index]))
                    row_counter +=1
                file.close()
                ColorMatrix = ColorMatrix[0:12]
            else:
                ColorMatrix = self.generateRandomMatrix()
        self.assignColors(ColorMatrix)
        self.ColorMatrix = ColorMatrix
        self.SelectionHat = Selector(self.tube_boxes[0].width/2,self.tube_boxes[0].height/6, self.tube_boxes[0].x + self.tube_boxes[0].width/4 , self.tube_boxes[0].y - self.tube_boxes[0].height/3)
        
        
    def getRandomIndex(self):
        return int(random.random() * 12)
    def generateRandomMatrix(self):
        ColorMat = []
        N = 12
        for i in range(12):
            l = []
            for j in range(4):
                l.append(0)
            ColorMat.append(l)
        choosedColors = [0]*N
        for i in range(N):
            for j in range(4):
                n = self.getRandomIndex()
                m = 0
                while choosedColors[n] >= 4:
                    n = self.getRandomIndex()
                    m = m + 1
                    if(m > 100):
                        break
                choosedColors[n] = choosedColors[n] + 1
                ColorMat[i][j] = n
                #print("n : " + str(n))
                #print("m : " + str(m))
                #print("choosedColors : " + str(choosedColors))
                #print("ColorMat : " + str(ColorMat))
        return ColorMat
    def assignColors(self,ColorMatrix_s):
        for i in range(12):
            for j in range(4):
                self.tube_boxes[i].colors[j] = ColorMatrix_s[i][j]
    def assignColorsToAll(self,fullMatrix):
        for i in range(14):
            for j in range(4):
                self.tube_boxes[i].colors[j] = fullMatrix[i][j]
    def getColors(self) -> list:
        fullStateMatrix = []
        for i in range(14):
            currentTub = []
            for j in range(4):
                currentTub.append(self.tube_boxes[i].colors[j])
            fullStateMatrix.append(currentTub)
        return fullStateMatrix

from Generator import Generator
import pygame


class GameManager:
    def __init__(self,gen):
        self.gen = gen

    def eventListner(self,events):
        pos = pygame.mouse.get_pos()
        for i in range(7*2):
            if self.gen.tube_boxes[i].isHover(pos) and self.gen.SelectionHat.isSelected == False:
                self.gen.SelectionHat.setPos(self.gen.tube_boxes[i].x,self.gen.tube_boxes[i].y)
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                print("clicked")
                print("--------------------------------------------")
                Unselect_bool = False
                for i in range(7*2):
                    if self.gen.tube_boxes[i].isHover(pos):
                        self.gen.tube_boxes[i].sel()
                        print("str(tube_boxes[i].selected) = " + str(self.gen.tube_boxes[i].selectedColor))
                        print("str(Sel[0].selected) = " + str(self.gen.SelectionHat.isSelected))
                        if(self.gen.tube_boxes[i].selectedColor != -1):
                            self.gen.SelectionHat.setPos(self.gen.tube_boxes[i].x,self.gen.tube_boxes[i].y)
                            Unselect_bool = True
                        played = False
                        if(self.gen.SelectionHat.isSelected == False):
                            self.gen.SelectionHat.select((self.gen.tube_boxes[i].selectedColor,self.gen.tube_boxes[i]))
                        else:
                            print("putColor test")
                            if self.gen.tube_boxes[i].putColor(self.gen.SelectionHat.selectedColor):
                                print("str(Sel[0].selected[0][1].index) = " + str(self.gen.SelectionHat.selectedTube.index))
                                print("i = " + str(i))
                                self.gen.tube_boxes[self.gen.SelectionHat.selectedTube.index].removeColor()
                                Unselect_bool = False
                                self.gen.tube_boxes[i].unsel()
                                self.gen.tube_boxes[self.gen.SelectionHat.selectedTube.index].unsel()
                                self.gen.SelectionHat.unselect()
                                played = True
                        if(played == False):
                            self.gen.SelectionHat.select((self.gen.tube_boxes[i].selectedColor,self.gen.tube_boxes[i]))
                if not Unselect_bool:
                    self.gen.SelectionHat.unselect()
                    self.gen.tube_boxes[i].unsel()
                    print("unselected")
                print("str(tube_boxes[i].selected) = " + str(self.gen.tube_boxes[i].selectedColor))
                print("str(Sel[0].selected) = " + str(self.gen.SelectionHat.isSelected))
    def update(self,events):
        for i in range(7*2):
            self.gen.tube_boxes[i].check()
        self.eventListner(events)
    def Play(self,source,destination_index):
        pass
    def draw(self):
        for i in range(7*2):
            self.gen.tube_boxes[i].draw(self.gen.screen)
        self.gen.SelectionHat.draw(self.gen.screen)
    


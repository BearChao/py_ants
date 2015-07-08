import pygame
from pygame.locals import Color
from com.nickzy.pyants.model.ant import Ant

__author__ = 'zynick'
class Simulator(object):#ants motion simulate
    def __init__(self,antNum):#the number of ant
        self.ants = []
        for i in range(1,antNum):
            self.ants.append(Ant(20+i,20+i,'run'))

    def simulate(self):
        for ant in self.ants:
            ant.move()
        pass
    def paint(self,screen):
        for ant in self.ants:
            start = (ant.x,ant.y)
            end = (ant.x,ant.y)
            pygame.draw.line(screen, Color('black'), start, end)
        pass

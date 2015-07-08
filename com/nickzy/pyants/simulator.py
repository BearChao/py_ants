import random

__author__ = 'zynick'
import pygame
from pygame.locals import Color
from com.nickzy.pyants.model.ant import Ant

class Simulator(object):#ants motion simulate
    #the number of ant,the border of the screen
    def __init__(self,antNum,border):
        self.ants = []
        self.X = border[0]
        self.Y = border[1]
        self.location = []
        for i in range(0,antNum):
            self.ants.append(Ant(200,200,'run',random.choice([1,2,3,4])))
            self.location.append((20,20))
        pass
    def simulate(self):
        for ant in self.ants:
            self.avoidBorder(ant)
            self.Move(ant)

        pass
    def paint(self,screen):
        for ant in self.ants:
            point = (ant.x,ant.y)
            pygame.draw.circle(screen, Color('black'), point,2)
        pass


    def Move(self,ant):
        if not ant.moved:
            l = [1,4,2,3]#1:up,4:down,2:left,3:right
            l.remove(5-ant.lm)#ant can't move back,5-a=b
            d=random.choice(l)
            if  (d==1):
                ant.moveU()
            elif(d==4):
                ant.moveD()
            elif(d==2):
                ant.moveL()
            elif(d==3):
                ant.moveR()
            ant.lm = d
        ant.moved = False
    def avoidBorder(self,ant):
        if ant.x >= self.X-1:
            ant.lm = 2
        if ant.x <= 1:
            ant.lm = 3
        if ant.y >= self.Y-1:
            ant.lm = 1
        if ant.y <= 1:
            ant.lm = 4
        touch = (ant.x,ant.y) in self.location#目前没有实现接触距离
        if touch:
            ant.moveBack()
            self.location=[]

    def dist(p1,p2):#distance of to points
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[2]) ** 2) ** 0.5

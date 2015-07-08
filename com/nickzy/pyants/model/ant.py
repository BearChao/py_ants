__author__ = 'zynick'
import random
import pygame
from pygame.locals import *
import os
from sys import exit

class Ant(object):#ant entity
    #location:x,y,
    #status:pass
    #lm:last move status
    __slots__=['x','y','status','lm']
    def __init__(self,x,y,status):
        self.x = x
        self.y = y
        self.status = status
        self.lm = 1
    #1:up,4:down,2:lift,3:right
    def moveU(self):self.y+=1
    def moveD(self):self.y-=1
    def moveL(self):self.x-=1
    def moveR(self):self.x+=1
    def move(self):
        l = [1,4,2,3]
        l.remove(5-self.lm)#ant can't move back,5-a=b
        d=random.choice(l)
        if  (d==1):
            self.moveU()
        elif(d==4):
            self.moveD()
        elif(d==2):
            self.moveL()
        elif(d==3):
            self.moveR()
        self.lm = d




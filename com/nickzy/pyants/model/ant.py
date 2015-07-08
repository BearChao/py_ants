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
    __slots__=['x','y','status','lm','touch','see','moved']
    def __init__(self,x,y,status,lm):
        self.x = x
        self.y = y
        self.status = status
        self.lm = lm #从上一次地点指向现在地点的方向
        self.touch = 4 #circle.d
        self.see = 10
        self.moved = False
    #1:up,4:down,2:lift,3:right
    def moveU(self):self.y-=1
    def moveD(self):self.y+=1
    def moveL(self):self.x-=1
    def moveR(self):self.x+=1
    def moveBack(self):
        m = 5-self.lm
        if(m==1):self.moveU()
        if(m==4):self.moveD()
        if(m==2):self.moveL()
        if(m==3):self.moveR()
        self.moved = True





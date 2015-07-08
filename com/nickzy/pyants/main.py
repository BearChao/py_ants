from com.nickzy.pyants.simulator import Simulator

__author__ = 'zynick'
import pygame
from pygame.locals import *
import os
from sys import exit

class Visual(object):#set visual window
    def __init__(self, screenSize, simulator):
        self.simulator = simulator
        self.screen = pygame.display.set_mode(screenSize)
        self.clock = pygame.time.Clock()

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.screen.fill(Color('white'))
            self.simulator.simulate()
            self.simulator.paint(self.screen)

            pygame.display.update()
            pygame.display.set_caption('fps: %d' % self.clock.get_fps())

            self.clock.tick(30)
def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    simulator = Simulator(400,(400,400))
    visual = Visual((400, 400), simulator)
    visual.run()

if __name__ == '__main__':
    main()

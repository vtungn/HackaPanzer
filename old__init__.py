# -*- coding: utf-8 -*-
import os, sys
import pygame
from pygame.locals import *
from track import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PanzerMain:

    "This class initialization the main game"
    rect1 = pygame.Rect(0, 0, 10, 10)
    def __init__(self, width=1080, depth=720):
        "init the screen window"
        pygame.init()
        self.width = width
        self.depth = depth
        self.screen = pygame.display.set_mode((self.width,self.depth))

    def MainLoop(self):
        "the main loop of the game"
        self.MainLoad()
        xM = 0
        yM = 0
        "key input event"
        while 1:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        xM, yM = self.track.move(event.key)

            "background"
            self.MainDraw()
            pygame.display.flip()

    def MainLoad(self):
        "load all module, sprite, shit..."
        self.track = Track(self.rect1)


    def MainDraw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.line(self.screen, (0, 0, 255), (210, 0), (200, 100))
        pygame.draw.aaline(self.screen, (0, 0, 255), (200, 0), (200, 100))
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect1)




if __name__ == "__main__":
    MainWindow = PanzerMain()
    MainWindow.MainLoop()
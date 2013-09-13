# -*- coding: utf-8 -*-
import os, sys
import pygame
from pygame.locals import *
from Tank import *
from TankAI import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PanzerMain:
    "This class initialization the main game"

    #rect1 = pygame.Rect(0, 0, 10, 10)

    gameObjects = []

    def __init__(self, width=1080, depth=720):

        #init the screen window
        pygame.init()
        self.width = width
        self.depth = depth
        self.screen = pygame.display.set_mode((self.width,self.depth))

	self.LoadContent()
        #xM = 0
        #yM = 0

    def LoadContent(self):
	"load all module, sprite, shit..."
	#self.track = Track(self.rect1)

	# TODO: Add game objects here
        self.tank = Tank()
        self.tank2 = TankAI()
        self.gameObjects.append(self.tank)
        self.gameObjects.append(self.tank2)
	for gameObject in self.gameObjects:
		gameObject.LoadContent()

    def MainLoop(self):

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
		    for gameObject in self.gameObjects:
			gameObject.UpdateKeyPress(event)

                #elif event.type == KEYDOWN:
                    #if ((event.key == K_RIGHT)
                    #or (event.key == K_LEFT)
                    #or (event.key == K_UP)
                    #or (event.key == K_DOWN)):
                        #xM, yM = self.track.move(event.key)
            for gameObject in self.gameObjects:
			gameObject.Update()
            self.MainDraw()
            pygame.display.flip()

    def MainDraw(self):

        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 0, 255), (210, 0), (200, 100))
        pygame.draw.aaline(self.screen, (0, 0, 255), (200, 0), (200, 100))

        for gameObject in self.gameObjects:
            gameObject.Draw(self.screen)

        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect1)

if __name__ == "__main__":
    MainWindow = PanzerMain()
    MainWindow.MainLoop()

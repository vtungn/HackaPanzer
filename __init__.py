# -*- coding: utf-8 -*-

import os, sys

import pygame
from pygame.locals import *

from Tank import *
from TankAI import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PanzerMain:
    "The main game"

    def __init__(self, width=1080, depth=720):
    
        # List of all the game's objects
        self.gameObjects = []
        
        # Init engine
        pygame.init()
                
        # Create the screen window
        self.width = width
        self.depth = depth
        self.screen = pygame.display.set_mode((self.width,self.depth))

        # Load game resources
        self.LoadContent()            

    def LoadContent(self):
	"Load all resources, sprite, shit..."
	
	    # TODO: Create game objects here
        self.tank = Tank()
        self.tank2 = TankAI()
        
        # TODO: Add game objects to the game here
        self.gameObjects.append(self.tank)
        self.gameObjects.append(self.tank2)
        
        # Load resources
        for gameObject in self.gameObjects:
		    gameObject.LoadContent()

    def MainLoop(self):
        while 1:
        
            # Handle pygame's events
            for event in pygame.event.get():
            
                # Quit game
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                # Handle input
                elif event.type == KEYDOWN:                
                    for gameObject in self.gameObjects:
			            gameObject.UpdateKeyPress(event)
               
            # Update game logic
            for gameObject in self.gameObjects:
			    gameObject.Update()
            
            # Draw graphics to back buffer
            self.MainDraw()
            
            # Swap screen buffer
            pygame.display.flip()

    def MainDraw(self):
    
        # Draw background
        self.screen.fill((255, 255, 255))
        
        # Draw graphics
        for gameObject in self.gameObjects:
            gameObject.Draw(self.screen)

if __name__ == "__main__":
    MainWindow = PanzerMain()
    MainWindow.MainLoop()

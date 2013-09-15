import pygame
from pygame.locals import *

from GameObject import *

class Shell(GameObject):

    def __init__(self, game, position):
        GameObject.__init__(self, game, position)  
        
        self.sprite = pygame.image.load("shell.png").convert()

    def go(self, direction):    
        self.direction = direction
        self.is_going = True
        
    def Update(self, event):
        if (self.is_going):
            if (self.direction == 'right'):
                #self.sprite.move(1,0)
                pass
            elif (self.direction == 'left'):
                #self.sprite.move(-1,0)
                pass
            elif (self.direction == 'up'):
                #self.sprite.move(0,1)
                pass
            elif (self.direction == 'down'):
                #self.sprite.move(0,-1)
                pass
        
    def Draw(self, screen):
        screen.blit(self.sprite, self.position)

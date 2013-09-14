# -*- coding: utf-8 -*-

import pygame

from GameObject import *
from track import *
from TankSprite import *
from Shell import *

class Tank(GameObject):

    def __init__(self, game, position):
        #pygame.sprite.Sprite.__init__(self)
        #self.TankRect = pygame.Rect(0, 0, 10, 10)
        
        GameObject.__init__(self, game, position)  
        
        # Replaced by self.position (common for all game objects)
        #self.position = (0, 0)
        
        self.direction = "right"
        self.barrel_position = self.get_barrel_position()
               
        self.rect = 0
        self.image = 0

    def LoadContent(self):
        #self.image, self.rect = self.load_image("snake.png", -1)
        tempSprite = TankSprite()
        self.Sprite = pygame.sprite.RenderPlain((tempSprite))
        self.track = Track(tempSprite)
        self.image = tempSprite.getImg()
        self.rect = tempSprite.getRect()

    def UpdateKeyPress(self,event):
    
        # Rotation
        if (event.key == K_RIGHT):
            self.rotate('right')
        elif (event.key == K_LEFT):
            self.rotate('left')
        elif (event.key == K_UP):
            self.rotate('up')
        elif (event.key == K_DOWN):
            self.rotate('down')
    
        # REVIEW
        # This is redundant, you will check for the key pressed again in Track.move()
        # A better solution is
        #
        # if ((event.key == K_RIGHT):
        #     self.moveTank("right")
        # elif (event.key == K_LEFT):
        #     self.moveTank("left")
        # elif (event.key == K_UP):
        #     self.moveTank("up")
        # elif (event.key == K_DOWN)):
        #     self.moveTank("down")
        #
        # def moveTank(direction)
        #     self.track.move(direction)
        if ((event.key == K_RIGHT)
        or (event.key == K_LEFT)
        or (event.key == K_UP)
        or (event.key == K_DOWN)):
            self.moveTank(event.key)       
                          
        # REVIEW
        # The position of the sprite should depends on the Tank's abstract position, not this way
        self.position = self.rect.center
        
    def rotate(self, direction):
        self.direction = direction    
        self.barrel_position = self.get_barrel_position()
        
    def get_barrel_position(self):
        if self.direction == 'up':   
            return self.position #+ self.length/2
        elif self.direction == 'down':   
            return self.position #- self.length/2
        elif self.direction == 'left':   
            return self.position #- self.width/2
        elif self.direction == 'right':   
            return self.position #+ self.width/2
        
    def shoot(self):
        shell = Shell(self.game, self.barrel_position)
        shell.go(self.direction)
    
    def Update(self, event):
        if (event.type == MOUSEBUTTONDOWN):   
            if (event.button == 1):
                self.shoot()
        
    def Draw(self,screen):
        self.Sprite.draw(screen)
        #pygame.draw.rect(screen, (0, 0, 0), self.TankRect)
        pass

    def moveTank(self, key):
        self.track.move(key)
        #self.image = pygame.transform.rotate(self.image, 90)


# -*- coding: utf-8 -*-
import pygame
from track import *
from TankSprite import *
from GameObject import *

class Tank(GameObject):


    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.TankRect = pygame.Rect(0, 0, 10, 10)
        self.pos = (0, 0)
        self.angle = 0
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
        if ((event.key == K_RIGHT)
        or (event.key == K_LEFT)
        or (event.key == K_UP)
        or (event.key == K_DOWN)):
            self.moveTank(event.key)
        self.pos = self.rect.center

    def Update(self):
        pass

        pass
    def Draw(self,screen):
        self.Sprite.draw(screen)
        #pygame.draw.rect(screen, (0, 0, 0), self.TankRect)
        pass

    def moveTank(self, key):
        self.track.move(key)
        #self.image = pygame.transform.rotate(self.image, 90)


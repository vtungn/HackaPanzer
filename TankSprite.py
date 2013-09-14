# -*- coding: utf-8 -*-
from Sprite import *

class TankSprite(Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image, self.rect = self.load_image(self.Name, -1)
        ss = spritesheet('tank10.png')
        self.images = []
        self.rects = []
        self.image, self.rect = ss.image_at((0, 0, 190, 190))
        self.images.append(self.image)
        self.rects.append(self.rect)
        self.image, self.rect = ss.image_at((0, 180, 190, 170))
        self.images.append(self.image)
        self.rects.append(self.rect)
        self.image, self.rect = ss.image_at((0, 340, 190, 170))
        self.images.append(self.image)
        self.rects.append(self.rect)
        self.image, self.rect = ss.image_at((0, 500, 190, 190))
        self.images.append(self.image)
        self.rects.append(self.rect)

        #self.images[1], self.rects[1] = ss.image_at((0, 18, 19, 17))
        #self.images[2], self.rects[2] = ss.image_at((0, 34, 19, 17))
        #self.images[3], self.rects[3] = ss.image_at((0, 50, 19, 19))

        #self.images[0], self.rects[0] = ss.image_at((0, 0, 19, 19))
        #self.images[1], self.rects[1] = ss.image_at((0, 18, 19, 17))
        #self.images[2], self.rects[2] = ss.image_at((0, 34, 19, 17))
        #self.images[3], self.rects[3] = ss.image_at((0, 50, 19, 19))

        #self.images, self.rects = ss.images_at([(0, 0, 19, 19),(0, 18, 19, 17),(0, 34, 19, 17),(0, 50, 19, 19)])
        self.image = self.images[1]
        self.rect = self.rects[1]

    # REVIEW
    # This is ROTATE sprite, NOT move
    def MoveSprite(self,frame):
        self.image = self.images[frame]
        #self.rect = self.rects[frame]
        #pass

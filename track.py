from pygame.locals import *
from TankSprite import *

class Track():
    "this for movement of the tank"
    def __init__(self,TankSprite):
        self.x_dif = 30
        self.y_dif = 30
        self.Sprite = TankSprite

    def move(self,key):
        xMove = 0
        yMove = 0
        if (key == K_RIGHT):
            xMove = self.x_dif
            self.Sprite.MoveSprite(1)
        elif (key == K_LEFT):
            xMove = -self.x_dif
            self.Sprite.MoveSprite(2)
        elif (key == K_UP):
            yMove = -self.y_dif
            self.Sprite.MoveSprite(0)
        elif (key == K_DOWN):
            yMove = self.y_dif
            self.Sprite.MoveSprite(3)

        self.Sprite.rect.move_ip(xMove, yMove)

        #self.Pan = PanzerMain
        #self.Pan.rect1.move_ip(xMove, yMove)
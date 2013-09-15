# -*- coding: utf-8 -*-

from Tank import *

class TankAI(Tank):

    def __init__(self, game, position):
        GameObject.__init__(self, game, position)  

    def UpdateKeyPress(self,event):
        pass

    def Update(self, event):
        self.moveTank(K_RIGHT)

# -*- coding: utf-8 -*-

from NormalShell import *

class Gun:

    angle = 0
    shell_type = NormalShell

    def __init__(self):
        pass

    def load(self, shell_type):
        self.shell_type = shell_type

    def shoot(self):
        return self.shell_type()

    def rotate(angle):
        self.angle = angle

    def auto_rotate():
        self.angle = 0

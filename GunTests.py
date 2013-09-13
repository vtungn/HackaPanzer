# -*- coding: utf-8 -*-

import unittest
from Gun import *
from Shell import *
from NormalShell import *

class GunTests(unittest.TestCase):

    def setUp(self):
        self.gun = Gun()

    def test_shoot(self):
        shell = self.gun.shoot()
        self.assertIsInstance(shell, Shell)

    def test_load_shell(self):
        self.gun.load(NormalShell)
        shell = self.gun.shoot()
        self.assertIsInstance(shell, NormalShell)

    #def test_rotate(self):
        #self.gun.rotate(180)
        #assertEqual(self.gun.angle, 180)


if __name__ == '__main__':
    unittest.main()

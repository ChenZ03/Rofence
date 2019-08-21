# imports
import pygame
import os
from .Enemies import Enemy


# create an empty list for Orge3
images = []


# add image for the Orge3
for x in range(4):
    string = str(x)
    images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ORG/3_ORK/RUN", "RUN_00" + string + ".png")), (50, 50)))


# create a class for orge while inherit properties from Enemy File
class Orge3(Enemy):

    def __init__(self):
        super().__init__()
        self.maxHP = 5
        self.health = self.maxHP
        self.money = 16
        self.imgs = images[:]
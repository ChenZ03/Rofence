#imports
import pygame
import os
from .Enemies import Enemy

# create a an empty list for Orge2
Images = []


# add image for the Orge2
for x in range(3):
    string = str(x)
    Images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ORG/2_ORK/WALK", "WALK_00" + string + ".png")), (50, 50)))


# create a class for orge while inherit properties from Enemy File
class Orge2(Enemy):

    # define the details of the orge
    def __init__(self):
        super().__init__()
        self.maxHP = 3
        self.health = self.maxHP
        self.money = 5
        self.imgs = Images[:]
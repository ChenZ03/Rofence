# imports
import pygame
import os
from .Enemies import Enemy

# create an empty list for Orge.images
Orge_images = []


# add image for Orge
for x in range(4):
    string = str(x)
    Orge_images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ORG/1_ORK/WALK", "WALK_00" + string + ".png")), (50, 50)))


# to create class for orge and inherit properties from Enemy file
class Orge(Enemy):

    def __init__(self):
        super().__init__()
        self.maxHP = 2
        self.health = self.maxHP
        self.money = 4
        self.imgs = Orge_images[:]
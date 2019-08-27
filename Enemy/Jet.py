# imports
import pygame
import os
from .Enemies import Enemy


# create an empty list for jet.images
Jet_images = []


# add image for Jet
Jet_images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ROFENCE/Robot", "jet right.png")), (50, 50)))


# to create class for Jet and inherit properties from Enemy file
class Jet(Enemy):

    def __init__(self):
        super().__init__()
        self.maxHP = 5
        self.health = self.maxHP
        self.money = 4
        self.imgs = Jet_images[:]
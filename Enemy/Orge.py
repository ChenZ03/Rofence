import pygame
import os
from .Enemies import Enemy


Orge_images = []

for x in range(7):
    string = str(x)
    Orge_images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ORG/1_ORK/WALK", "WALK_00" + string + ".png")), (50, 50)))


class Orge(Enemy):

    def __init__(self):
        super().__init__()
        self.maxHP = 1
        self.health = self.maxHP
        self.money = 10
        self.imgs = Orge_images[:]
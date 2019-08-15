import pygame
import os
from .Enemies import Enemy


class Orge3(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []
        self.maxHP = 10
        self.health = self.maxHP

        for x in range(7):
            string = str(x)
            self.imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("Assets/ORG/3_ORK/WALK", "WALK_00" + string + ".png")), (70, 70)))

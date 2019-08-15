import pygame
import os
from .Enemies import Enemy


class Orge(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []

        for x in range(7):
            string = str(x)
            self.imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("Assets/ORG/1_ORK/WALK", "WALK_00" + string + ".png")), (50, 50)))

# Imports and inheritances
import pygame
from pygame import *
from Shop.Shop import Menu
import math
import os

# Shop's background
bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Rec.png")), (120, 70))


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.menu = Menu(self, self.x, self.y, bg, [2000, "MAX"])
        self.tower_imgs = []
        self.damage = 1

        self.place_color = (0, 0, 255, 100)

    def draw(self, window):
        img = self.tower_imgs[self.level - 1]
        window.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

    def draw_placement(self, win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50, 50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self, X, Y):
        if  X <= self.x + self.width and X >= self.x:
            if Y <= self.y and Y >= self.y:
                return False

    def move(self, x, y):
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, other_towers):
        x2 = other_towers.x
        y2 = other_towers.y

        dis = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        if dis >= 100:
            return False
        else:
            return True



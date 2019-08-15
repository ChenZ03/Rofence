import pygame
from pygame import *
import math


class Enemy:

    def __init__(self):
        self.width = 32
        self.height = 32
        self.img = None
        self.path = [(79, 383), (188, 384), (193, 269), (198, 180), (314, 176), (437, 176), (436, 288), (442, 376), (442, 449), (530, 454), (613, 452), (706, 454), (760, 454), (757, 395), (756, 325), (856, 317), (945, 320), (1047, 317), (1155, 316), (-10, 316)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.animation_count = 0
        self.health = 1
        self.path_pos = 0
        self.move_count = 0
        self.move_distance = 0
        self.distance = 0
        self.imgs = []
        self.flipped = False

    def draw(self, window):
        # window = surface
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        window.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        if  X <= self.x + self.width and X >= self.x:
            if Y <= self.y and Y >= self.y:
                return False

    def move(self):
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 316)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        direction = ((x2 - x1) * 2, (y2 - y1) * 2)
        length = math.sqrt((direction[0]) ** 2 + (direction[1]) ** 2)
        direction = (direction[0] / length, direction[1] / length)

        if direction[0] < 0:
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + direction[0]), (self.y + direction[1]))

        self.x = move_x
        self.y = move_y

        # Go to next point
        if direction[0] >= 0:  # moving right
            if direction[1] >= 0:  # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:  # moving left
            if direction[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1





    def hit(self):
        # True if enemy is destroyed
        self.health -= 1
        if self.health <= 0:
            return True



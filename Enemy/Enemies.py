# Imports
import pygame
from pygame import *
import math
import time


class Enemy:

    def __init__(self):
        self.width = 32
        self.height = 32
        self.img = None
        # Path for enemies to walk on
        self.path = [(-10, 353), (14, 353), (182, 354), (185, 591), (582, 583), (598, 581), (598, 528), (598, 442), (598, 393), (598, 302), (598, 115), (1167, 121), (1198, 116), (1300, 116)]

        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.animation_count = 0
        self.health = 1
        self.path_pos = 0
        self.move_count = 0
        self.move_distance = 0
        self.distance = 0
        self.imgs = []
        self.maxHP = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    # Draw enemies animations
    def draw(self, window):
        # window = surface

        self.img = self.imgs[self.animation_count]
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        window.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2))
        self.hpBar(window)

    # Enemy Health Bar
    def hpBar(self, window):
        hpLen = 40
        hpMove = round(hpLen) / self.maxHP
        healthBar = hpMove * self.health

        pygame.draw.rect(window, (255, 0, 0), (self.x - 17, self.y - 35, hpLen, 8), 0)
        pygame.draw.rect(window, (0, 255, 0), (self.x - 17, self.y - 35, healthBar, 8), 0)

    def collide(self, X, Y):
        if  X <= self.x + self.width and X >= self.x:
            if Y <= self.y and Y >= self.y:
                return False

    # Enemy move towards the path from one to another
    def move(self):
        start_frame = time.time()
        noi = 16
        frames_per_second = 10
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

        '''if direction[0] < 0:
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)'''

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
             """if direction[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1"""

        return self.up, self.right, self.down

    # Check enemy is dead or na
    def hit(self, damage):
        # True if enemy is destroyed
        self.health -= damage
        if self.health <= 0:
            return True
        return False


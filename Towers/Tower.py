import pygame
from pygame import *
import sys
import os

class Heroes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.img = []
        self.path = []
        self.damage = 50

    def hero(self):
        # hero class

    def draw(self, window):
        # window = surface
        pass

    def attack(self, x, y):
        # hero attack
        # x = skill
        # y = dmg

    def hit(self, x, y):
        # Enemy get hits

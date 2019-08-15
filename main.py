import pygame
from pygame import *
import os
from Enemy.Orge import Orge
from Enemy.Orge_2 import Orge2
from Enemy.Orge_3 import Orge3
import time
import random

class Game:
    def __init__(self):
        pygame.init()
        self.height = 700
        self.width = 1200
        self.window = pygame.display.set_mode((self.width, self.height))
        self.towers = []
        self.enemies = [Orge()]
        self.lives = 20
        self.money = 200
        self.bg = pygame.image.load(os.path.join("Assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.timer = time.time()

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            if time.time() - self.timer >= 2:
                self.timer = time.time()
                # self.enemies.append(random.choice([Orge(), Orge2(), Orge3()]))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            # Loop Through Enemies:
            delete = []
            for Enemy in self.enemies:
                if Enemy.x > 1200:
                    delete.append(Enemy)

            # Delete off_Screen Enemies
            for delete in delete:
                self.enemies.remove(delete)

            # Drawing Circles (path)
            '''pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks.append(pos)
                print(self.clicks)'''

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.blit(self.bg, (0, 0))
        # Draw Enemy
        for enemies in self.enemies:
            enemies.draw(self.window)
        '''for p in self.clicks:
            pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 5, 0)'''
        pygame.display.update()


game = Game()
game.run()




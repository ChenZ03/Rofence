import pygame
from pygame import *
import os
from Enemy.Orge import Orge
from Enemy.Orge_2 import Orge2
from Enemy.Orge_3 import Orge3


class Game:
    def __init__(self):
        pygame.init()
        self.height = 700
        self.width = 1200
        self.window = pygame.display.set_mode((self.width, self.height))
        self.towers = []
        self.enemies = [Orge(), Orge2(), Orge3()]
        self.lives = 20
        self.money = 200
        self.bg = pygame.image.load(os.path.join("Assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            # Loop Through Enemies:
            delete = []
            for Enemy in self.enemies:
                if Enemy.x < -5:
                    delete.append(Enemy)

            # Delete off_Screen Enemies
            for delete in delete:
                self.enemies.remove(delete)

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.blit(self.bg, (0, 0))
        # Draw Enemy
        for enemies in self.enemies:
            enemies.draw(self.window)
        pygame.display.update()


game = Game()
game.run()




import pygame
from pygame import *
import os
from Enemy.Orge import Orge
from Enemy.Orge_2 import Orge2
from Enemy.Orge_3 import Orge3
from Towers.canonTower import LongTower, ShortTower
import time
import random
pygame.font.init()
pygame.init()

lives_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "lives.png")), (25, 25))
coin_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "coin.png")), (25, 25))


class Game:
    def __init__(self):
        pygame.init()
        self.height = 700
        self.width = 1200
        self.window = pygame.display.set_mode((self.width, self.height))
        self.towers = [ShortTower(320, 200), LongTower(510, 500)]
        self.enemies = [Orge()]
        self.life = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("Assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("comicsans", 65)

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            if time.time() - self.timer > 5:
                self.timer = time.time()
                self.enemies.append(random.choice([Orge(), Orge2(), Orge3()]))
            clock.tick(200)
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
                self.life -= 1
                self.enemies.remove(delete)

            # Loop through Towers
            for towers in self.towers:
                towers.attack(self.enemies)

            # Game Over
            if self.life <= 0:
                print("GAME OVER" + "\n" + "YOU LOSE")
                run = False

            # Drawing Circles (path)
            '''pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks.append(pos)
                print(self.clicks)'''

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.blit(self.bg, (0, 0))

        # Draw Clicks
        '''for p in self.clicks:
            pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 5, 0)'''

        # Draw Enemy
        for enemies in self.enemies:
            enemies.draw(self.window)

        # Draw Towers
        for tower in self.towers:
            tower.draw(self.window)

        # Draw Lives
        text = self.life_font.render(str(self.life), 1, (255, 255, 255))
        life = pygame.transform.scale(lives_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.window.blit(text, (start_x - text.get_width() - 10, 13))
        self.window.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (0, 0, 0))
        money = pygame.transform.scale(coin_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.window.blit(text, (start_x - text.get_width() - 10, 75))
        self.window.blit(money, (start_x, 65))

        pygame.display.update()


game = Game()
game.run()




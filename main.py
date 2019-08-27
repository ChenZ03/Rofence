# IMPORTS
import pygame
from pygame import *
import os
import time
import random

# Import enemy from other files (Easier for lookup and editing)
from Enemy.Jet import Jet
from Enemy.Robot import Robot
from Enemy.Tanker import Tanker

# Import Tower from other files
from Towers.LongTower import LongTower
from Towers.ShortTower import ShortTower

# Import Shop from other files
from Shop.Shop import Shop, Play

# Load Images and Scale them
lives_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE", "heart.png")), (25, 25))
coin_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE", "Energy.png")), (25, 25))
Shop_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE", "shop_menu.png")), (450, 70))
Shop_icon1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE", "Shop_001.png")), (50, 50))
Shop_icon2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE", "Shop_002.png")), (50, 50))
play = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Play.png")), (60, 60))
pause = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Pause.png")), (60, 60))
wave_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wave.png")), (300, 120))


# Name List of Towers
towers_name = ["LongTower", "ShortTower"]

waves = [
    [20, 0, 0],
    [50, 0, 0],
    [100, 0, 0],
    [0, 20, 0],
    [0, 50, 0],
    [0, 100, 0],
    [20, 100, 0],
    [50, 100, 0],
    [100, 100, 0],
    [0, 0, 50],
    [20, 0, 100],
    [20, 0, 150],
    [200, 100, 200],
]


# Main game class
class Game:
    # Initialize Game Variables
    def __init__(self):
        pygame.init()
        # Height of the Window
        self.height = 700
        self.width = 1200
        self.window = pygame.display.set_mode((self.width, self.height))

        # List of Towers
        self.towers = [ShortTower(280, 320)]

        # list of enemies ----- Jet() as the first enemy
        self.enemies = [Jet()]

        # Lives and Money
        self.lives = 10
        self.money = 100

        # Initialize Background image
        self.background = pygame.image.load(os.path.join("Assets", "map rotated.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # Mouse clicks list
        self.clicks = []

        # Game Timer
        self.timer = time.time()

        # Select Tower to view Range
        self.selectedTowers = None

        # Main Font
        self.life_font = pygame.font.SysFont("comicsansms", 35)

        # Shop's settings
        self.shop_font = pygame.font.SysFont("Times New Roman", 25)
        self.shop = Shop(300, 0, Shop_img)
        self.shop.add_btn(Shop_icon1, "ShortTower", 100)
        self.shop.add_btn(Shop_icon2, "LongTower", 300)

        # For placing new Towers
        self.movingTowers = None

        # Game Play/Pause
        self.pause = True
        self.play_pause = Play(play, pause, 10, 20)

        # Enemy Waves
        self.wave = 1
        self.current_wave = waves[self.wave][:]
        self.wave_font = pygame.font.SysFont("comicsansms", 50)

        # Tower path
        self.path = []

    def gen_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.play_pause.paused = self.pause
                self.play_pause.img_change()
        else:
            wave_enemies = [Jet(), Robot(), Tanker()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    # MAIN RUN

    def run(self):
        run = True
        # Frame
        clock = pygame.time.Clock()

        while run:
            clock.tick(40)

            # GENERATE SPAWNS
            if not self.pause:
                # gen monsters
                if time.time() - self.timer >= random.randrange(1, 6) / 3:
                    self.timer = time.time()
                    self.gen_enemies()

            # Get mouse pos
            pos = pygame.mouse.get_pos()

            # If tower is moving
            if self.movingTowers:
                self.movingTowers.move(pos[0], pos[1])

            # Game Event Starts

            # Quit GAME EVENT
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

                # Mouse position
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    self.clicks.append(pos)
                    print(self.clicks)
                    # If you are buying towers
                    if self.movingTowers:
                        if self.movingTowers.name in towers_name:
                            self.towers.append(self.movingTowers)

                        self.movingTowers = None

                    else:
                        # Check for play/pause
                        if self.play_pause.click(pos[0], pos[1]):
                            self.pause = not(self.pause)
                            self.play_pause.img_change()

                        # Buying Towers From The Shop
                        Shop_btn = self.shop.get_clicked(pos[0], pos[1])

                        # Determine cost and subtract them from self.money
                        if Shop_btn:
                            if Shop_btn == "ShortTower":
                                cost = 100
                            else:
                                cost = 300
                            if self.money >= cost:
                                self.money -= cost
                                self.buy_towers(Shop_btn)

                    for tw in self.towers:
                        if tw.click(pos[0], pos[1]):
                            tw.selected = True
                            self.selectedTowers = tw
                        else:
                            tw.selected = False

            if not self.pause:
                # Loop Through Enemies:
                delete = []
                for Enemy in self.enemies:
                    Enemy.move()
                    if Enemy.x > 1200:
                        delete.append(Enemy)

                # Delete end path Enemies
                for delete in delete:
                    self.lives -= 1
                    self.enemies.remove(delete)

                # Adding Money
                for towers in self.towers:
                    self.money += towers.attack(self.enemies)

                # Game Over
                if self.lives <= 0:
                    print("GAME OVER" + "\n" + "YOU LOSE")
                    run = False

            # Drawing Circles (path)
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks.append(pos)
                print(self.clicks)'''

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.blit(self.background, (0, 0))

        for pos in self.path:
            pygame.draw.circle(self.window, (255, 0, 0), pos, 5, 0)

        # Draw Clicks
        '''for p in self.clicks:
            pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 5, 0)'''

        # Draw Enemy
        for enemies in self.enemies:
            enemies.draw(self.window)

        # Draw Towers
        for tower in self.towers:
            tower.draw(self.window)

        # Draw Buying_towers
        if self.movingTowers:
            self.movingTowers.draw(self.window)

        # Draw Lives
        text = self.life_font.render(str(self.lives), 1, (255, 255, 255))
        life = pygame.transform.scale(lives_img, (45, 45))
        start_x = self.width - life.get_width() - 10

        self.window.blit(text, (start_x - 700, 15))
        self.window.blit(life, (start_x - 650, 15))

        # Draw Money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        Energy = pygame.transform.scale(coin_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.window.blit(text, (start_x - 400, 15))
        self.window.blit(Energy, (start_x - 320, 15))

        # Draw play/ pause btn
        self.play_pause.draw(self.window)

        # Draw Shop
        self.shop.draw(self.window)
        start_x = self.width - (self.width - 855)
        end_x = self.width - 140
        shop_title = self.life_font.render("ROFENCE SHOP :", 1, (255, 255, 255))
        cost1 = self.shop_font.render(str(100), 1, (0, 0, 0))
        cost2 = self.shop_font.render(str(300), 1, (0, 0, 0))
        self.window.blit(cost1, (start_x, 655))
        self.window.blit(cost2, (end_x, 655))
        self.window.blit(shop_title, (start_x - 50, 560))

        # Draw Wave
        text = self.life_font.render("Wave #" + str(self.wave), 1, (255, 255, 255))
        self.window.blit(text, (30, 640))

        pygame.display.update()

    # Buy Towers From Shop

    def buy_towers(self, tower):
        # Get mouse position
        x, y = pygame.mouse.get_pos()

        # Tower
        towerName = ["ShortTower", "LongTower"]
        towerSelf = [ShortTower(x, y), LongTower(x, y)]

        # Buy towers and add them in
        try:
            buy = towerSelf[towerName.index(tower)]
            self.movingTowers = buy
            buy.moving = True

        except Exception as E:
            print(E)


# Run game
game = Game()
game.run()




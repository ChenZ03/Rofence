import pygame
import os
import math
import time
from .Tower import Tower

ShortTower_images = []
Bullet_images = []

# Load imgs for Short tower:
ShortTower_images.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE/Tower/Ice tower", "Ice.png")), (135, 135)))

# Load bullet imgs:
for i in range(1, 7):
    Bullet_images.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE/Tower/Ice tower", "ice_00" + str(i) + ".png")), (55, 55)))


# Short Tower Class (inherit from Tower Class)
class ShortTower(Tower):
    # Initialise ShortTower's Vars
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = ShortTower_images[:]
        self.bullet_imgs = Bullet_images[:]
        self.bullet_count = 0
        self.range = 120
        self.inRange = False
        self.hitTimer = time.time()
        self.damage = 2.5
        self.moving = False
        self.name = "ShortTower"
        self.left = False

    # Draw tower
    def draw(self, window):
        super().draw(window)

        if self.inRange:
            self.bullet_count += 1
            if self.bullet_count >= len(self.bullet_imgs) * 5:
                self.bullet_count = 0
        else:
            self.bullet_count = 0

        bullet = self.bullet_imgs[self.bullet_count // 5]
        window.blit(bullet, ((self.x + self.width - 22) - (bullet.get_width() / 10), (self.y - bullet.get_height() + 10)))

        # Draw Range Circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (224, 224, 224, 30), (self.range, self.range), self.range, 0)

        window.blit(surface, (self.x - self.range, self.y - self.range))

        # Tower Range

    def range(self, ran):
        self.range = ran

        # Attack enemies and add money to self.money

    def attack(self, enemies):
        money = 0

        self.inRange = False
        # Find Closest enemy
        closest_enemy = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if distance < self.range:
                self.inRange = True
                closest_enemy.append(enemy)

        # Attack closest enemy and add money
        if len(closest_enemy) > 0:
            first_enemy = closest_enemy[0]
            if time.time() - self.hitTimer >= 1:
                self.hitTimer = time.time()
                if first_enemy.hit(self.damage):
                    money = first_enemy.money
                    enemies.remove(first_enemy)

            '''if first_enemy.x > self.x and not (self.left):
                self.left = True
                for x, img in enumerate(self.bullet_imgs):
                    self.bullet_imgs[x] = pygame.transform.flip(img, True, False)
            elif first_enemy.x < self.x and self.left:
                self.left = False
                for x, img in enumerate(self.bullet_imgs):
                    self.bullet_imgs[x] = pygame.transform.flip(img, True, False)'''

        return money

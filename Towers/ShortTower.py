import pygame
import os
import math
import time
from .Tower import Tower

ShortTower_images = []
Bullet_images = []

# Load imgs for Short tower:
ShortTower_images.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Stone_tower/ShortRange", "ShortTower.png")), (150, 150)))
# Load bullet imgs:
for i in range(1, 6):
    Bullet_images.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Stone_tower/ShortRange","explosion_00" + str(i) + ".png")), (20, 20)))


class ShortTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = ShortTower_images[:]
        self.bullet_imgs = Bullet_images[:]
        self.bullet_count = 0
        self.range = 120
        self.inRange = False
        self.hitTimer = time.time()
        self.damage = 1
        self.moving = False
        self.name = "ShortTower"

    def draw(self, window):
        super().draw(window)

        if self.inRange and not self.moving:
            self.bullet_count += 1
            if self.bullet_count >= len(self.bullet_imgs) * 5:
                self.bullet_count = 0
        else:
            self.bullet_count = 0

        bullet = self.bullet_imgs[self.bullet_count // 5]
        window.blit(bullet, ((self.x + self.width - 5) - (bullet.get_width() / 2), (self.y - bullet.get_height() - 20)))

        # Draw Range Circle

        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (224, 224, 224, 30), (self.range, self.range), self.range, 0)

        window.blit(surface, (self.x - self.range, self.y - self.range))

    def range(self, ran):
        self.range = ran

    def attack(self, enemies):
        money = 0

        self.inRange = False
        closest_enemy = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if distance < self.range:
                self.inRange = True
                closest_enemy.append(enemy)

        if len(closest_enemy) > 0:
            first_enemy = closest_enemy[0]
            if time.time() - self.hitTimer >= 2:
                self.hitTimer = time.time()
                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money
                    enemies.remove(first_enemy)

        return money
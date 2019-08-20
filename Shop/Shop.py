import pygame
import os
pygame.font.init()

coin = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "coin.png")), (45, 45))
coint = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "coin.png")), (75, 75))


class Menu:
    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)
        self.tower = tower

    def add_btn(self, img, name):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        self.buttons.append(Button(self, img, name))

    def get_item_cost(self):
        """
        gets cost of upgrade to next level
        :return: int
        """
        return self.item_cost[self.tower.level - 1]

    def draw(self, win):
        """
        draws btns and menu bg
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y - 120))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x + item.width + 5, item.y - 9))
            text = self.font.render(str(self.item_cost[self.tower.level - 1]), 1, (255, 255, 255))
            win.blit(text, (item.x + item.width + 30 - text.get_width() / 2, item.y + star.get_height() - 8))

    def get_clicked(self, X, Y):
        """
        return the clicked item from the menu
        :param X: int
        :param Y: int
        :return: str
        """
        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name

        return None

    def update(self):
        """
        update menu and button location
        :return: None
        """
        for btn in self.buttons:
            btn.update()


class Button:
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.item_cost = cost

    def click(self, X, Y):
        """
        returns if the positon has collided with the menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, win):
        """
        draws the button image
        :param win: surface
        :return: None
        """
        win.blit(self.img, (self.x, self.y))

    def update(self):
        """
        updates button position
        :return: None
        """
        self.x = self.menu.x - 50
        self.y = self.menu.y - 110


class Shop:
    def __init__(self, x, y, image):
        self.tower = None
        self.buttons = []
        self.item = 0
        self.x = x
        self.y = y
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.cost = 0
        self.font = pygame.font.SysFont("Times New Roman", 25)

    def add_btn(self, image, name, cost):
        self.cost = cost
        self.item += 1
        btnX = self.x - 20 + (self.item - 1) * 400
        btnY = self.y + 620
        self.buttons.append(Button(btnX, btnY, image, name, cost))

    def item_cost(self):
        return None

    def draw(self, window):
        window.blit(self.image, (100, 600))
        for item in self.buttons:
            item.draw(window)
            window.blit(coin, (item.x + item.width + 5, item.y - 9))
            cost = self.font.render(self.item_cost(), 1, (255, 255, 255))
            window.blit(cost, (item.x + item.width + 30 - cost.get_width() / 2, item.y + coin.get_height() - 8))

    def get_clicked(self, X, Y):
        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name

        return None

    def update(self):
        for btn in self.buttons:
            btn.update()


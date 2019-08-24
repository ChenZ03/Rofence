# Imports
import pygame
import os
pygame.font.init()


# Load Coin image
coin = pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE", "Energy.png")), (45, 45))
coint = pygame.transform.scale(pygame.image.load(os.path.join("Assets/ROFENCE", "Energy.png")), (75, 75))


# create a class and inherit
class Menu:
    def __init__(self, tower, x, y, images, item_cost):
        self.x = x
        self.y = y
        self.width = images.get_width()
        self.height = images.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.background = images
        self.font = pygame.font.SysFont("comicsans", 20)
        self.tower = tower

    # add button for 'shop'
    def add_btn(self, image, name):

        self.items += 1
        self.buttons.append(Button(self, image, name))

    # cost for tower
    def get_item_cost(self):

        return self.item_cost[self.tower.level - 1]

    # to render the window for 'Menu'
    def draw(self, win):

        win.blit(self.background, (self.x - self.background.get_width() / 2, self.y - 120))
        for item in self.buttons:
            item.draw(win)
            win.blit(coin, (item.x + item.width + 5, item.y - 9))

    # return the name of button if the button is clicked
    def get_clicked(self, X, Y):

        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name

        return None

    # update button
    def update(self):

        for btn in self.buttons:
            btn.update()


# create a class for the buttons and initialize the properties of button
class Button:
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.images = img
        self.x = x
        self.y = y
        self.width = self.images.get_width()
        self.height = self.images.get_height()
        self.item_cost = cost

    # returns True if the button collided
    def click(self, X, Y):

        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    # to render the image of button
    def draw(self, win):

        win.blit(self.images, (self.x, self.y))

    # to update
    def update(self):

        self.x = self.menu.x - 50
        self.y = self.menu.y - 110


# create a class for shop and initialize the properties of shop
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
        self.font = pygame.font.SysFont("Times New Roman", 20)

    # add button for shop
    def add_btn(self, image, name, cost):
        self.cost = cost
        self.item += 1
        button_X = self.x - 20 + (self.item - 1) * 400
        button_Y = self.y + 620
        self.buttons.append(Button(button_X, button_Y, image, name, cost))

    #
    def item_cost(self):
        pass

    # to render window for 'shop'
    def draw(self, window):
        window.blit(self.image, (100, 600))
        for item in self.buttons:
            item.draw(window)
            window.blit(coin, (item.x + item.width + 5, item.y - 9))
            cost = self.font.render(self.item_cost(), 1, (255, 255, 255))
            window.blit(cost, (item.x + item.width + 30 - cost.get_width() / 2, item.y + coin.get_height() - 8))

    # returns the name of button when the button is clicked
    def get_clicked(self, X, Y):
        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name

        return None

    # to update button
    def update(self):
        for btn in self.buttons:
            btn.update()


# Play / Pause
class Play(Button):
    def __init__(self, play, pause, x, y):
        self.images = play
        self.play = play
        self.pause = pause
        self.x = x
        self.y = y
        self.width = self.images.get_width()
        self.height = self.images.get_height()

    def img_change(self):
        if self.images == self.play:
            self.images = self.pause
        else:
            self.images = self.play
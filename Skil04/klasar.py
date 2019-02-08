import pygame
import tkinter
from random import *

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

clock = pygame.time.Clock()


def random(low, high):
    a = randint(low, high)
    return a


class Obj(pygame.sprite.Sprite):
    def __init__(self, window, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.window = window

    def make_data_package(self):
        datax = str(self.rect.centerx).rjust(4, '0')
        datay = str(self.rect.centery).rjust(4, '0')
        return datax + datay

class Player(pygame.sprite.Sprite):
    def __init__(self, window, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/"+img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 390
        self.stig = 0
        self.window = window

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, dy)
        if dy != 0:
            self.move_single_axis(dx, dy)

    def move_single_axis(self, dx, dy):
        if self.rect.x <= 1838:
            self.rect.x += dx
        else:
            self.rect.x = 1838

        if self.rect.x >= 50:
            self.rect.x += dx
        else:
            self.rect.x = 50

        if self.rect.y <= 998:
            self.rect.y += dy
        else:
            self.rect.y = 998

        if self.rect.y >= 50:
            self.rect.y += dy
        else:
            self.rect.y = 50

    def make_data_package(self):
        datax = str(self.rect.centerx).rjust(4, '0')
        datay = str(self.rect.centery).rjust(4, '0')

        return datax + datay


class Bakgrunnur(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_file.convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

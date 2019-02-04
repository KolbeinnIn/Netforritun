import pygame

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/hero.png").convert_alpha()
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


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (1920, 1080))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

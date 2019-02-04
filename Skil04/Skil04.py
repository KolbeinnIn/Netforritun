# Kolbeinn, Ágúst og Bjarki
# Miðannarverkefni netforritun og þráðavinnsla


import pygame
import klasar

pygame.init()

window_size = window_width, window_height = (0, 0)
window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)

pygame.display.set_caption('Jónatan á þræðinum')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)
img = pygame.image.load

my_font = pygame.font.SysFont("", 60)
clock = pygame.time.Clock()

player = klasar.Player(window, "hero.jpg")
gamli = klasar.Obj(window, pygame.image.load("images/wizard.jpg").convert_alpha(), 1590, 390)

bakgrunnur = klasar.Bakgrunnur('images/bak.jpg', [0, 0])
# gamli = pygame.image.load('images/wizard.png').convert_alpha()
#gamli = pygame.transform.scale(gamli, (80, 80))


player_list = pygame.sprite.Group()
obj_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(gamli)
speed = 2
player_list.add(player)
obj_list.add(gamli)

running = True
while running:
    clock.tick(144)
    key = pygame.key.get_pressed()
    window.blit(bakgrunnur.image, bakgrunnur.rect)
    window.blit(gamli, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player.move(-speed, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player.move(speed, 0)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        player.move(0, speed)
    if key[pygame.K_UP] or key[pygame.K_w]:
        player.move(0, -speed)

    if pygame.sprite.groupcollide(obj_list, player_list, True, True):
        pass
    all_sprites_list.draw(window)
    pygame.display.update()
pygame.quit()



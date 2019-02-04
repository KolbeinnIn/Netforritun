# Kolbeinn, Ágúst og Bjarki
# Miðannarverkefni netforritun og þráðavinnsla


import pygame
import klasar

pygame.init()

window_size = window_width, window_height = (0, 0)
window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)

pygame.display.set_caption('Jónatan á þræðinum')
bakgrunnur = pygame.image.load("images/bak.png")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)

my_font = pygame.font.SysFont("", 60)
clock = pygame.time.Clock()

player = klasar.Player(window)

BackGround = klasar.Background('images/bak.png', [0, 0])
player_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
#window.blit(bakgrunnur, [0,0])
speed = 5

running = True
while running:
    clock.tick(60)
    key = pygame.key.get_pressed()
    window.blit(BackGround.image, BackGround.rect)
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

    all_sprites_list.draw(window)
    pygame.display.update()
pygame.quit()


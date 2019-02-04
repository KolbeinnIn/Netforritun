# Kolbeinn, Ágúst og Bjarki
# Miðannarverkefni netforritun og þráðavinnsla


import pygame
import pygame.freetype
import klasar
pygame.init()

window_size = window_width, window_height = (0, 0)
window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
width = klasar.width
height = klasar.height

pygame.display.set_caption('Jónatan á þræðinum')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)
img = pygame.image.load

#my_font = pygame.font.SysFont("./asd.ttf", 23)
my_font = pygame.freetype.Font("./asd.ttf", 23)
clock = pygame.time.Clock()

player = klasar.Player(window, "hero.jpg")
gamliM = img('images/wizard.png').convert_alpha()
gamliM = pygame.transform.scale(gamliM, (80, 80))
#1590 390
gamli = klasar.Obj(window, gamliM.convert_alpha(), width * 0.82, height * 0.36)

player_list = pygame.sprite.Group()
obj_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(gamli)

player_list.add(player)
obj_list.add(gamli)

bakgrunnur = klasar.Bakgrunnur(img('images/bak.jpg'), [0, 0])



textsurface = my_font.render('Geturðu sótt handa mér 5 blóm fyrir seiðið mitt', False, (0, 0, 0))


speed = 3
running = True
while running:
    clock.tick(60)
    key = pygame.key.get_pressed()
    window.blit(bakgrunnur.image, bakgrunnur.rect)
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

    if pygame.sprite.groupcollide(obj_list, player_list, False, False):
        #window.blit(img("images/text1.png"), [(width * 0.82)-64, (height * 0.36)-64])
        bubble = pygame.transform.scale(img("images/bubble.png"), (400, 70))
        window.blit(bubble, [(width * 0.82)-290, (height * 0.36)-54])
        window.blit(textsurface, [(width * 0.82)-270, (height * 0.36)-30])

    pygame.display.update()
pygame.quit()



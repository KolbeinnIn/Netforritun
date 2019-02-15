# Kolbeinn, Ágúst og Bjarki
# Miðannarverkefni netforritun og þráðavinnsla


import pygame
import klasar
import time
import connection
import socket
import pickle

pygame.init()

window_size = window_width, window_height = (0, 0)
window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
width = klasar.width
height = klasar.height

MY_SERVER_HOST = '10.220.226.53'
MY_SERVER_PORT = 9992
OTHER_HOST = '10.220.226.55'
OTHER_PORT = 9999


class Player_1(klasar.Player):
    def __init__(self):
        super().__init__(window, "hero.png")


class Player_2(klasar.Player):
    def __init__(self):
        super().__init__(window, "hero2.png")


def ip_value(ip):
    return int(''.join([x.rjust(3, '0') for x in ip.split('.')]))


def define_players():
    if ip_value(MY_SERVER_HOST) > ip_value(OTHER_HOST):
        me = Player_1()
        enemy = Player_2()
    else:
        me = Player_2()
        enemy = Player_1()
    return me, enemy


def data_transfer():
    me_data = player.make_data_package()

    connection.send(me_data, OTHER_HOST, OTHER_PORT)# the send code

    enemy_data = server.receive()# the receive code

    player2.rect.centerx = int(enemy_data[:4])
    player2.rect.centery = int(enemy_data[4:])


pygame.display.set_caption('Jónatan á þræðinum')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)
img = pygame.image.load

my_font = pygame.font.SysFont("", 23)
my_font2 = pygame.font.SysFont("", 43)

clock = pygame.time.Clock()

player, player2 = define_players()
gamliM = img('images/wizard.png')
gamliM = pygame.transform.scale(gamliM, (80, 80)).convert_alpha()
#1590 390
gamli = klasar.Obj(window, gamliM, width * 0.82, height * 0.36)

blomM = img('images/blom.png')
blomM = pygame.transform.scale(blomM, (40, 40)).convert_alpha()
blomstra = []
for x in range(9):
    cx = (klasar.random(90, width-90))
    cy = (klasar.random(90, height-90))
    blomstra.append((cx, cy))


HOST = socket.gethostname()
PORT = 12345

s = socket.socket()
s.bind((HOST, PORT))
s.listen(2)

while True:
    c, addr = s.accept()
    c.send(pickle.dumps(blomstra))
    blomstra2 = pickle.loads(c.recv(1024))
    if len(blomstra2) != 0:
        break

print(blomstra2)


player_list = pygame.sprite.Group()
player_list2 = pygame.sprite.Group()
obj_list = pygame.sprite.Group()
blom_list = pygame.sprite.Group()

for i in range(len(blomstra)):
    x = (blomstra[i][0] + blomstra2[i][0]) // 2
    y = (blomstra[i][1] + blomstra2[i][1]) // 2
    blom = klasar.Obj(window, blomM, x, y)
    blom_list.add(blom)

player_list.add(player)
player_list2.add(player2)
obj_list.add(gamli)

bakgrunnur = klasar.Bakgrunnur(img('images/bak.jpg'), [0, 0])

textsurface = my_font.render('Geturðu sótt handa mér 5 blóm fyrir seiðið mitt', False, (0, 0, 0))

vann1 = my_font.render('Jónatann vann, Gummi tapaði', False, (255, 255, 255))
vann2 = my_font.render('Gummi vann, Jónatan tapaði', False, (255, 255, 255))

server = connection.Server(MY_SERVER_HOST, MY_SERVER_PORT)

bubble = pygame.transform.scale(img("images/bubble.png"), (400, 70))
bubblePos = [(width * 0.82)-290, (height * 0.36)-54]
textPos = [(width * 0.82)-270, (height * 0.36)-30]
bubble = bubble.convert_alpha()
textsurface = textsurface.convert_alpha()


speed = 3
running = True
mission = False
mission2 = False
collected = 0
collected2 = 0
while running:
    clock.tick(60)
    key = pygame.key.get_pressed()
    safn = my_font2.render('Blómum safnað: %d' % collected, False, (0, 255, 255))

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

    player_list.draw(window)
    player_list2.draw(window)
    obj_list.draw(window)
    blom_list.draw(window)

    if pygame.sprite.groupcollide(obj_list, player_list, False, False) or pygame.sprite.groupcollide(obj_list, player_list2, False, False):
        window.blit(bubble, bubblePos)
        window.blit(textsurface, textPos)
        #if key[pygame.K_SPACE]:
        mission = True

    if mission:
        if collected == 5 or collected2 == 5:
            window.fill((0, 0, 0, 1))
            if collected == 5:
                window.blit(vann2, [width//2, height//2])
            elif collected2 == 5:
                window.blit(vann1, [width//2, height//2])
            pygame.display.flip()
            #time.sleep(5)
            pygame.time.wait(3000)
            running = False

        cx = (klasar.random(90, width-90))
        cy = (klasar.random(90, height-90))
        if pygame.sprite.groupcollide(blom_list, player_list, True, False):
            collected += 1
        if pygame.sprite.groupcollide(blom_list, player_list2, True, False):
            collected2 += 1

        window.blit(safn, [10, 10])
    data_transfer()
    pygame.display.update()
pygame.quit()


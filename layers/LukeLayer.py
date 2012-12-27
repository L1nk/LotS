import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # lock the game at 30 fps
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Luke Layer')

WHITE = (255, 255, 255)
lukeImg = pygame.image.load('../img/Luke_right.png')
lukex = 10
lukey = 10
direction = 'right'

while True: #main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        lukeImg = pygame.image.load('../img/Luke_right.png')
        lukex += 3
        if lukex >= 300:
            direction = 'down'
    elif direction == 'down':
        lukeImg = pygame.image.load('../img/Luke_down.png')
        lukey += 3
        if lukey >= 220:
            direction = 'left'
    elif direction == 'left':
        lukeImg = pygame.image.load('../img/Luke_left.png')
        lukex -= 3
        if lukex <= 10:
            direction = 'up'
    elif direction == 'up':
        lukeImg = pygame.image.load('../img/Luke_up.png')
        lukey -= 3
        if lukey <= 10:
            direction = 'right'

    DISPLAYSURF.blit(lukeImg, (lukex, lukey))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

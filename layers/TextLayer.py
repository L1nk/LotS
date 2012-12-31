import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Text Layer - LotS')

WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 128)

fontObj = pygame.font.Font('../fonts/SerpentisBlack.ttf', 12)
textSurfaceObj = fontObj.render('Luke:', True, WHITE, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.topleft = (10, 230)

while True: #main game loop
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, BLUE, (5,225,390,70))
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

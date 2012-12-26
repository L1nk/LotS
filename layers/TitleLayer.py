import pygame, sys
from pygame.locals import *

pygame.init()

# set up the title window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('TITLE - LotS')

# set up the colors to use
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
SILVER = (192, 192, 192)
GOLD   = (255, 216,   0)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
#pygame.draw.polygon(DISPLAYSURF, GREEN, ((146,0), (291, 106), (236, 277), (56,277), (0, 106)))
#pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
#pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
#pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
#pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
#pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
swordBlade = pygame.draw.rect(DISPLAYSURF, SILVER, (100, 150, 300, 10))
swordTip = pygame.draw.polygon(DISPLAYSURF, SILVER, ((400,150), (420,155), (400, 159)))
swordHilt = pygame.draw.rect(DISPLAYSURF, GOLD, (92,135, 8, 40))
#pixObj = pygame.PixelArray(DISPLAYSURF)
#pixObj[480][380] = BLACK
#pixObj[482][382] = BLACK
#pixObj[484][384] = BLACK
#pixObj[486][386] = BLACK
#pixObj[488][388] = BLACK
#del pixObj

# run the title loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

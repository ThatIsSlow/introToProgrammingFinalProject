import pygame as pg 
from random import randint
from pygame.sprite import Sprite
from settings import *
from sprites import *

vec = pg.math.Vector2

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(" ")
clock = pg.time.Clock()

running = True
while running:
    delta = clock.tick(FPS)
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()

pg.quit()
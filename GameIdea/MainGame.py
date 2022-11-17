import pygame as pg 
from random import randint
from pygame.sprite import Sprite
from GameIdea.settings import *
from GameIdea.sprites import *

vec = pg.math.Vector2

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(" ")
clock = pg.time.Clock()

# Function to get things on screen
mob1 = Mob(WHITE, 10)

mobs = pg.sprite.Group()

mobs.add(mob1)

running = True
while running:
    delta = clock.tick(FPS)
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False

    mobs.draw(screen)
    pg.display.flip()

pg.quit()
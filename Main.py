############################################################################################################################################################
"""
PROJECT OUTLINE:
    - Two possible ideas
        - gaem
            - will use pygame, will use randint
            - will use settings and sprites as different python files to increase the modularity
            - will use image files as characters 
            - GAME DESIGN:
                - most likely strategy based, maybe something like RISK or a towere defense game. Something Turn based would be cool.
                - Definitely want to use mulitple levels
        - HereNow (rowing results website) parser
            - Will likely use Tkinter
            - will enable the user to input a team name or a rower name or a boat class
                - will then scan HereNow, looking through certain races, or a lot of races, to assemble all of the results of the
                    desired search, and then place it into a new window/file
"""
###############################################################################################################################################################

"""
Sources: 

"""

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

# Function to get things on screen
mob1 = Mob(WHITE)

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
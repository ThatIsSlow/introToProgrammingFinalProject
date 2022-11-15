# this holds all of my classes and objects
from pygame.sprite import Sprite
import pygame as pg
from random import randint

class Mob(Sprite):
    def __init__(self, color, hitpoints):
        Sprite.__init__(self)
        self.image = pg.Surface((randint(15,25),randint(15,25)))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width/2, self.rect.height/2)
        self.health = hitpoints



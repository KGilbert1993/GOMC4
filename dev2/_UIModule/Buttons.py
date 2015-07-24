import pygame
from pygame.locals import *
import os

green = (0,200,0, 50)
red = (200,0,0, 50)
grey = (160,160,160,70)

def test():
    print 'test worked!'

class Button(object):
    width = 0
    height = 0
    x = 0
    y = 0
    img = pygame.Surface
    window = None

    def __init__(self, window, w, h, x, y, image):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.window = window
        self.img = pygame.image.load(os.path.join(os.path.abspath('../'), image)).convert(24)
        self.img = pygame.transform.scale(self.window, (self.width, self.height))
        self.img.set_alpha(128)

        self.window.blit(self.img, (self.x, self.y))

    def draw(self):
        pygame.draw.rect(self.window, green, (self.x, self.y, self.width, self.height), 2)
        self.window.blit(self.img, (self.x, self.y))

    def on_click(self):
        print 'on clicking'

import pygame
from pygame.locals import *
import os, sys

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
    img = None
    window = None

    def __init__(self, window, w, h, x, y, image):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.window = window
        print os.path.dirname(os.path.realpath(__file__))
        print os.path.join(os.path.abspath('dev2'), 'img\\button2.png')
        print os.path.join(os.path.abspath('dev2.py'), 'img\\button2.png')
        self.img = pygame.image.load('button2.png')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.window.blit(self.img, (self.x, self.y))

    def draw(self):
        pygame.draw.rect(self.window, green, (self.x-1, self.y-1, self.width+1, self.height+1), 4)
        self.window.blit(self.img, (self.x, self.y))

    def on_click(self):
        print 'on clicking'

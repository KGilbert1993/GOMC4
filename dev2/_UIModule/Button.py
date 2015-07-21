import pygame
from pygame.locals import *

def test():
    print 'test worked!'

class Button:
    width = 0
    height = 0
    x = 0
    y = 0
    img = ''

    def draw(self):
        print 'drawing'

    def on_click(self):
        print 'on clicking'

import pygame
from pygame.locals import *

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
        self.img = pygame.image.load(image)
        self.img = pygame.transform.scale(self.window, (self.width, self.height))

        disp = screen = pygame.display.set_mode(size,HWSURFACE|DOUBLEBUF|RESIZABLE)
        disp.blit(self.img, (self.x, self.y))
        disp.display.update()

    def draw(self):
        pygame.draw.rect(self.window, green, (self.x, self.y, self.width, self.height), 2)
        #self.window.blit(self.img, (self.x, self.y))

    def on_click(self):
        print 'on clicking'

import pygame
from pygame.locals import *
from time import sleep
from game_constants import *
import game_constants

"""
SOURCE: 
http://powerfield-software.com/?p=851
"""
def draw_hex(screen, row, col):
    ofst = 0
    c = 30
    #c = c * cm

    # Calculate a and b from c.

    a = c * 433 / 500
    b = c / 2

    # Get coords for leftmost corner.

    x = col * (b + c) + ofst
    y = a + a * row * 2 + (col % 2) * a + ofst
    pygame.draw.line (screen, red, (x,       y),   (x+b,     y+a))
    pygame.draw.line (screen, red, (x+b,     y+a), (x+b+c,   y+a))
    pygame.draw.line (screen, red, (x+b+c,   y+a), (x+b+c+b, y))
    pygame.draw.line (screen, red, (x+b+c+b, y),   (x+b+c,   y-a))
    pygame.draw.line (screen, red, (x+b+c,   y-a), (x+b,     y-a))
    pygame.draw.line (screen, red, (x+b,     y-a), (x,       y))

coords = []
a = 0
b = 0
c = 30
def generate_hexcenter_list():
    global coords, a, b, c
    c = 30
    a = c * 433/500
    b = c / 2
    for row in xrange(0,25):
        for col in xrange(0,40):
            x = col * (b + c)
            y = a + a * row * 2 + (col % 2) * a
            coords.append((int(x+b+(0.5*c)),int(y), col, row))

def get_pos():
    """
    
    """
    mouse = pygame.mouse.get_pos()
    xbin = mouse[0] / (c + (2*b))
    ybin = mouse[1] / (2 * a)
    for c in coords:
        if((mouse[0]-40 <= c[0] <= mouse[0]+40) and (mouse[1]-40 <= c[1] <= mouse[1]+40)):
            return (c[2], c[3])
    return (-1, -1)

def start_game(screen):
    screen.fill((128,128,128))
    pygame.display.update()
    generate_hexcenter_list()
    while(True):
        pygame.event.pump()
        events = pygame.event.get()

        for y in xrange(0,40):
            for x in xrange(0,25):
                draw_hex(screen, x, y)

        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                print get_pos()

            if(pygame.key.get_pressed()[K_SPACE]):
                pygame.display.quit()

        for c in coords:
            pygame.draw.circle(screen, green, (c[0], c[1]), 3)

        pygame.display.update()
        game_constants.clock.tick(60)
            
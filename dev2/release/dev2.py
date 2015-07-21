"""
    Game Dev Test 2
    Current Revision: 4
    5 July 2015
"""

import os
import pygame, sys
from pygame.locals import *
import random
import pygame.gfxdraw

##################################################################################################
#   Global Attributes
##################################################################################################
debug = False
debug_lv2 = True

SCREEN_RATE = 60
size = display_w, display_h = 800, 600
scale = 1,1
quit_w = 53
quit_h = 20
green = (0,200,0, 50)
red = (200,0,0, 50)
grey = (160,160,160,70)
filename = "img/space1.jpg"
font_size = 12
test_box_w = 180 - 2 
test_box_h = 125 - 2
line_ep1 = [10, 10, 1, 1.2]   # (x, y, speed_x, speed_y)
line_ep2 = [20, 60, 1.1, -2]

##################################################################################################
#   Update Functions
##################################################################################################
def quit_loc_x():
    return (display_w - (display_w/20)) - quit_w

def quit_loc_y():
    return (display_h - (display_h/20)) - quit_h

def update_constants():
    global display_w, display_h, quit_w, quit_h
    info = pygame.display.Info()
    display_w = info.current_w
    display_h = info.current_h
    quit_w = display_w/15
    quit_h = display_h/30
    if debug:
       print info, ' (', display_w, ',', display_h, ') (', quit_w, ',', quit_h, ')'

def move_line():
    global line_ep1, line_ep2
    # Check bounds
    if (line_ep1[0] < 2) or (line_ep1[0] >= test_box_w):
        line_ep1[2] *= -1
    if (line_ep1[1] < 2) or (line_ep1[1] >= test_box_h):
        line_ep1[3] *= -1
    if (line_ep2[0] < 2) or (line_ep2[0] >= test_box_w):
        line_ep2[2] *= -1
    if (line_ep2[1] < 2) or (line_ep2[1] >= test_box_h):
        line_ep2[3] *= -1

    if debug_lv2:
        print 'End Point 1 --> '
        for n in line_ep1:
            print n
        print 'End Point 2 --> '
        for n in line_ep2:
            print n

    line_ep1[0] += (line_ep1[2])# + random.uniform(0, 0.5))
    line_ep1[1] += (line_ep1[3])# + random.uniform(0, 0.5))
    line_ep2[0] += (line_ep2[2])# + random.uniform(0, 0.5))
    line_ep2[1] += (line_ep2[3])# + random.uniform(0, 0.5))

##################################################################################################
#   Main
##################################################################################################
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size,HWSURFACE|DOUBLEBUF|RESIZABLE)

    bg = pygame.image.load(filename)
    bg = pygame.transform.scale(bg, (display_w, display_h))

    button = pygame.image.load('img/button.png').convert(24)
    button.set_alpha(180)
    screen.blit(button, (400,300))

    font = pygame.font.SysFont("monospace", font_size)
    title = pygame.font.SysFont("monospace", 24)
    clock = pygame.time.Clock()

    if debug:
       print 'debugging!'

    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
    pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), red)

    pygame.display.flip()

##################################################################################################
#   Runtime environment
##################################################################################################
    while True:
        pygame.event.pump()
        #event = pygame.event.wait()
        event = pygame.event.poll()

        # Refresh Screen
        screen.fill((0,0,0))
        bg = pygame.transform.scale(bg, (display_w, display_h))
        screen.blit(bg, (0,0))

        # Generate Text
        label = font.render("Exit", 1, (255,255,0))
        title_msg = title.render("Galatic Ocarina of Metroid Combat 4: Modern Windwaker", 5, (255,255,0))

        screen.blit(label, ((quit_loc_x() + quit_w/4), (quit_loc_y() + quit_h/4)))
        screen.blit(title_msg, (display_w/25, display_h/15))

        screen.blit(button, (360,300))
        pygame.draw.rect(screen, grey, (360,300,91,40),2)

        # Generate Button
        if event.type == pygame.NOEVENT or event.type != pygame.MOUSEMOTION:
            if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                    quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), green)
            else:
                pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), red)

        # Generate visual test box
        pygame.draw.rect(screen, grey, (30,450,180,125), 2)
        pygame.gfxdraw.box(screen, pygame.Rect(30, 450, 180, 125), grey)
        move_line()
        pygame.draw.line(screen, (255,255,0), (line_ep1[0]+30, line_ep1[1]+450), (line_ep2[0]+30, line_ep2[1]+450),2)


##################################################################################################
#   Event Loop
##################################################################################################
        if event.type == pygame.QUIT:
            pygame.display.quit()

        elif event.type == pygame.VIDEORESIZE:
            update_constants()
            screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
            screen.blit(pygame.transform.scale(bg, event.dict['size']), (0, 0))
            font_size = 12
            font = pygame.font.SysFont("monospace", font_size)
            #pygame.display.update()

        elif event.type == pygame.MOUSEMOTION:
            update_constants()
            if debug:
               print quit_w, ' ', quit_h
               print 'Box: ', quit_loc_x(), ',', quit_w + quit_loc_x(), 'Mouse: ', pygame.mouse.get_pos()

            if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                    quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), green)
            else:
                pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), red)
            #pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                    quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                if debug:
                    print 'Exiting...'
                pygame.display.quit()

        pygame.display.update()
        clock.tick(SCREEN_RATE)


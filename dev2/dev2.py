"""
    Game Dev Test 2
    Current Revision: 5
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
debug_lv2 = False

SCREEN_RATE = 60
size = display_w, display_h = 800, 600
scale = 1,1
quit_w = 53
quit_h = 20
green = (0,200,0, 50)
red = (200,0,0, 50)
grey = (160,160,160,70)
filename = "img/space1.jpg"
BUTTON_IMG = "img/button2.png"
EXIT_GR = "img/exit_green.jpg"
EXIT_RED = "img/exit_red.jpg"
font_size = 12
test_box_w = 180 - 2 
test_box_h = 125 - 2
line_ep1 = [10, 10, 1, 1.2]   # (x, y, speed_x, speed_y)
line_ep2 = [20, 60, 1.1, -2]
CURSOR_SIZE = 5

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

    exit_r = pygame.image.load(EXIT_RED).convert(24)
    exit_g = pygame.image.load(EXIT_GR).convert(24)
    exit_r = pygame.transform.scale(exit_r, (quit_w, quit_h))
    exit_g = pygame.transform.scale(exit_g, (quit_w, quit_h))
    exit_r.set_alpha(128)
    exit_g.set_alpha(128)

    font = pygame.font.SysFont("monospace", font_size)
    title = pygame.font.SysFont("monospace", 24)
    clock = pygame.time.Clock()

    if debug:
       print 'debugging!'

    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
    pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), red)

    pygame.mouse.set_visible(False)

    pygame.display.flip()

##################################################################################################
#   Runtime environment
##################################################################################################
    while True:
        pygame.event.pump()
        print clock.get_fps()
        events = pygame.event.get()

        # Refresh Screen
        screen.fill((0,0,0))
        bg = pygame.transform.scale(bg, (display_w, display_h))
        exit_g = pygame.transform.scale(exit_g, (quit_w, quit_h))
        exit_r = pygame.transform.scale(exit_r, (quit_w, quit_h))
        screen.blit(bg, (0,0))

        # Generate Text
        title_msg = title.render("Galatic Ocarina of Metroid Combat 4: Modern Windwaker", 5, (255,255,0))
        screen.blit(title_msg, (display_w/25, display_h/15))

        # Generate Button
        #if pygame.MOUSEMOTION not in events:
        #if not (pygame.MOUSEMOTION in event.type for event in events):
        mouse_motion = False
        for event in events:
            if event.type is pygame.MOUSEMOTION:
                mouse_motion = True
                break

        if not mouse_motion:
            print 'NO MOUSE EVENT, DRAWING BUTTON'
            """
            if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                    quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), green)
            else:
                pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), red)
            """
            if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                screen.blit(exit_g, (quit_loc_x(), quit_loc_y()))
            else:
                pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                screen.blit(exit_r, (quit_loc_x(), quit_loc_y()))

        # Generate visual test box
        pygame.draw.rect(screen, grey, (30,450,180,125), 2)
        pygame.gfxdraw.box(screen, pygame.Rect(30, 450, 180, 125), grey)
        move_line()
        pygame.draw.line(screen, (255,255,0), (line_ep1[0]+30, line_ep1[1]+450), (line_ep2[0]+30, line_ep2[1]+450),2)

        # Draw mouse cursor thing
        pygame.draw.line(screen, (255,255,0), (0, (pygame.mouse.get_pos()[1]-CURSOR_SIZE)), 
                            (pygame.mouse.get_pos()[0]+CURSOR_SIZE, (pygame.mouse.get_pos()[1]-CURSOR_SIZE)), 1)
        pygame.draw.line(screen, (255,255,0), ((pygame.mouse.get_pos()[0]+CURSOR_SIZE), (pygame.mouse.get_pos()[1]-CURSOR_SIZE)), 
                            ((pygame.mouse.get_pos()[0]+CURSOR_SIZE),  display_h))

        pygame.draw.line(screen, (255,255,0), ((pygame.mouse.get_pos()[0]-CURSOR_SIZE), 0),
                                    ((pygame.mouse.get_pos()[0]-CURSOR_SIZE), pygame.mouse.get_pos()[1]+CURSOR_SIZE), 1)
        pygame.draw.line(screen, (255,255,0), ((pygame.mouse.get_pos()[0]-CURSOR_SIZE), (pygame.mouse.get_pos()[1]+CURSOR_SIZE)),
                                     (display_w, (pygame.mouse.get_pos()[1]+CURSOR_SIZE)), 1)


##################################################################################################
#   Event Loop
##################################################################################################
        for event in events:
            print event
            if event.type == pygame.QUIT:
                pygame.display.quit()

            elif event.type == pygame.VIDEORESIZE:
                update_constants()
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(bg, event.dict['size']), (0, 0))
                font_size = 12
                font = pygame.font.SysFont("monospace", font_size)

            elif event.type == pygame.MOUSEMOTION:
                update_constants()
                if debug:
                   print quit_w, ' ', quit_h
                   print 'Box: ', quit_loc_x(), ',', quit_w + quit_loc_x(), 'Mouse: ', pygame.mouse.get_pos()
                """
                if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and 
                        quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                    pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                    pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), green)
                else:
                    pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                    pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), red)
                """
                if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                    quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                    pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                    screen.blit(exit_g, (quit_loc_x(), quit_loc_y()))
                else:
                    pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                    screen.blit(exit_r, (quit_loc_x(), quit_loc_y()))


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                        quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                    if debug:
                        print 'Exiting...'
                    pygame.display.quit()

        pygame.display.update()
        clock.tick(SCREEN_RATE)


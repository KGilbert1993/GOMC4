"""4
    Game Dev Test 2
    Current Revision: 8
    Start: 05 June 2015
    Edit: 01 August 2015
"""

import os
import pygame, sys
from pygame.locals import *
import random
import pygame.gfxdraw
import cProfile, pstats, StringIO

#   Custom Modules
from _UIModule import buttons
from _UIModule.constants import *
from game_constants import *

##################################################################################################
#   Global Attributes
##################################################################################################
#   Debug and Profiling
debug = False
debug_lv2 = False
debug_fps = False
profile = False

#   Attributes
expand_settings = False


##################################################################################################
#   Update Functions
##################################################################################################

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
    screen = pygame.display.set_mode(size,HWSURFACE|DOUBLEBUF|RESIZABLE|FULLSCREEN)

    buttons.test()
    settings = buttons.Button(screen, 90, 25, 75, 115, SETTINGS_IMG)
    settings_g = buttons.Button(screen, 90, 25, 75, 115, SETTINGS_G_IMG)
    settings.attach_callback(buttons.test)

    bg = pygame.image.load(BACKGROUND_IMG).convert(24)
    bg = pygame.transform.scale(bg, (display_w, display_h))
    bg.set_alpha(200)

    title_img = pygame.image.load(TITLE).convert(24)
    title_img = pygame.transform.scale(title_img, (title_img.get_width()*2, title_img.get_height()*2))
    title_img.set_alpha(128)

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

    if (profile):
        pr = cProfile.Profile()
        pr.enable()

##################################################################################################
#   Runtime environment
##################################################################################################
    while True:
        pygame.event.pump()
        if debug_fps:
            print clock.get_fps()
        events = pygame.event.get()

        # Refresh Screen
        #screen.fill((0,0,0))
        bg = pygame.transform.scale(bg, (display_w, display_h))
        exit_g = pygame.transform.scale(exit_g, (quit_w, quit_h))
        exit_r = pygame.transform.scale(exit_r, (quit_w, quit_h))
        screen.blit(bg, (0,0))

        # Generate Text
        #title_msg = title.render("Galatic Ocarina of Metroid Combat 4: Modern Windwaker", 10, (255,0,0))
        screen.blit(title_img, (display_w/5, 20))
        #screen.blit(title_msg, (display_w/3, display_h/20))

        # Settings Box
        pygame.draw.rect(screen, grey, (30,100,180,275), 2)
        pygame.gfxdraw.box(screen, pygame.Rect(30, 100, 180, 275), grey)

        if(expand_settings):
            pygame.gfxdraw.box(screen, pygame.Rect(235, 113, 350, 462), green)
            pygame.draw.rect(screen, green, (235, 113, 350, 462), 2)
            pygame.draw.line(screen, green, (75,113), (235, 113), 2)

        # Generate Button
        mouse_motion = False
        for event in events:
            if event.type is pygame.MOUSEMOTION:
                mouse_motion = True
                break

        if not mouse_motion:
            if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                screen.blit(exit_g, (quit_loc_x(), quit_loc_y()))
            else:
                pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                screen.blit(exit_r, (quit_loc_x(), quit_loc_y()))

            if ((pygame.mouse.get_pos()[0] > 80 and pygame.mouse.get_pos()[0] < 160) and (
                pygame.mouse.get_pos()[1] > 115 and pygame.mouse.get_pos()[1] < 140)):
                settings_g.draw()
            else:
                settings.draw()

        # Generate visual test box
        pygame.draw.rect(screen, grey, (30,450,180,125), 2)
        pygame.gfxdraw.box(screen, pygame.Rect(30, 450, 180, 125), grey)
        move_line()
        pygame.draw.line(screen, (255,0,0), (line_ep1[0]+30, line_ep1[1]+450), (line_ep2[0]+30, line_ep2[1]+450),2)

       

##################################################################################################
#   Event Loop
##################################################################################################
        for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()


            elif event.type == pygame.VIDEORESIZE:
                """
                update_constants()
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(bg, event.dict['size']), (0, 0))
                font_size = 12
                font = pygame.font.SysFont("monospace", font_size)
                """
                print 'resize'

            elif event.type == pygame.MOUSEMOTION:
                update_constants()
                if debug:
                   print quit_w, ' ', quit_h
                   print 'Box: ', quit_loc_x(), ',', quit_w + quit_loc_x(), 'Mouse: ', pygame.mouse.get_pos()
                if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                    quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                    pygame.draw.rect(screen, green, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                    screen.blit(exit_g, (quit_loc_x(), quit_loc_y()))
                else:
                    pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
                    screen.blit(exit_r, (quit_loc_x(), quit_loc_y()))

                if ((pygame.mouse.get_pos()[0] > 80 and pygame.mouse.get_pos()[0] < 160) and (
                    pygame.mouse.get_pos()[1] > 115 and pygame.mouse.get_pos()[1] < 140)):
                    settings_g.draw()
                else:
                    settings.draw()


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                        quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) ):
                    if debug:
                        print 'Exiting...'
                    if (profile):
                        pr.disable()
                        s = StringIO.StringIO()
                        sortby = 'cumulative'
                        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
                        ps.print_stats()
                        print s.getvalue()
                        log = open('profile_log', 'w')
                        log.write(s.getvalue())
                        log.close()
                    pygame.display.quit()

                if (settings.x < pygame.mouse.get_pos()[0] < (settings.width + settings.x) and
                        settings.y < pygame.mouse.get_pos()[1] < (settings.height + settings.y)):
                    expand_settings = not expand_settings
                    settings.handle_event(event)

        # Draw mouse cursor thing
        pygame.draw.line(screen, (255,0,0), (0, (pygame.mouse.get_pos()[1]-CURSOR_SIZE)), 
                            (pygame.mouse.get_pos()[0]+CURSOR_SIZE, (pygame.mouse.get_pos()[1]-CURSOR_SIZE)), 1)
        pygame.draw.line(screen, (255,0,0), ((pygame.mouse.get_pos()[0]+CURSOR_SIZE), (pygame.mouse.get_pos()[1]-CURSOR_SIZE)), 
                            ((pygame.mouse.get_pos()[0]+CURSOR_SIZE),  display_h))

        pygame.draw.line(screen, (255,0,0), ((pygame.mouse.get_pos()[0]-CURSOR_SIZE), 0),
                                    ((pygame.mouse.get_pos()[0]-CURSOR_SIZE), pygame.mouse.get_pos()[1]+CURSOR_SIZE), 1)
        pygame.draw.line(screen, (255,0,0), ((pygame.mouse.get_pos()[0]-CURSOR_SIZE), (pygame.mouse.get_pos()[1]+CURSOR_SIZE)),
                                     (display_w, (pygame.mouse.get_pos()[1]+CURSOR_SIZE)), 1)

        pygame.display.update()
        clock.tick(SCREEN_RATE)


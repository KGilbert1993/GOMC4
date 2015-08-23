"""
    Game Dev Test 2
    Current Revision: 10
    Start: 05 June 2015
    Edit: 18 August 2015
"""

import os
import pygame, sys
from pygame.locals import *
import random
import pygame.gfxdraw
import cProfile, pstats, StringIO
import ConfigParser
import game_constants

#   Custom Modules
from _UIModule import buttons
from _UIModule.constants import *
from _UIModule.inputbox import *
from game_constants import *
from game import *

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
button_list = []


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

def cursor_handle():
    cursor_current = config.get('Display', 'cursor')
    if(cursor_current == 'True'):                        
        config.set('Display', 'cursor', 'False')
    else:
        config.set('Display', 'cursor', 'True')
    conf_file = open(CONFIG_FILE, 'w')
    config.write(conf_file)
    conf_file.close()
    pygame.mouse.set_visible('True' == config.get('Display', 'cursor'))

def settings_handle():
    global expand_settings
    expand_settings = not expand_settings

def new_game_handle():
    start_game(screen)

##################################################################################################
#   Main
##################################################################################################
if __name__ == '__main__':
    global config
    pygame.init()
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    size_config = config.get('Display', 'Resolution').split(',')
    size = (int(size_config[0]), int(size_config[1]))
    screen = pygame.display.set_mode(size,HWSURFACE|DOUBLEBUF|RESIZABLE|FULLSCREEN)

    buttons.test()
    settings = buttons.Button(screen, 100, 25, 75, 115, SETTINGS_IMG)
    settings_g = buttons.Button(screen, 100, 25, 75, 115, SETTINGS_G_IMG)
    settings.attach_callback(settings_handle)

    cursor_button = buttons.Button(screen, 150, 25, 335, 130, CHANGE_CURSOR)
    cursor_button_sel = buttons.Button(screen, 150, 25, 335, 130, CHANGE_CURSOR_SEL)
    cursor_button.attach_callback(cursor_handle)

    new_game = buttons.Button(screen, 100, 25, 75, 160, NEW_GAME)
    new_game_sel = buttons.Button(screen, 100, 25, 75, 160, NEW_GAME_SEL)
    new_game_sel.attach_callback(new_game_handle)

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
    title = pygame.font.SysFont("monospace",  24)
    #game_constants.clock = pygame.time.Clock()

    button_list.append(settings)
    button_list.append(cursor_button)
    button_list.append(new_game_sel)

    if debug:
       print 'debugging!'

    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, red, (quit_loc_x(), quit_loc_y(), quit_w, quit_h), 2)
    pygame.gfxdraw.box(screen, pygame.Rect(quit_loc_x(), quit_loc_y(), quit_w, quit_h), red)

    pygame.mouse.set_visible('True' == config.get('Display', 'cursor'))

    pygame.display.flip()


#    a = ask(screen, "Name")
#    config.set('User', 'Name', a)
#    conf_file = open(CONFIG_FILE, 'w')
#    config.write(conf_file)
#    conf_file.close()


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
            pygame.gfxdraw.box(screen, pygame.Rect(235, 115, 350, 460), green)
            pygame.draw.rect(screen, green, (235, 115, 350, 460), 2)
            pygame.draw.line(screen, green, (75,115), (235, 115), 2)

            if (cursor_button.region_check()):
                cursor_button_sel.draw()
            else:
                cursor_button.draw()

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

            if (new_game.region_check()):
                new_game_sel.draw()
            else:
                new_game.draw()

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
 
                if (new_game.region_check()):
                    new_game_sel.draw()
                else:
                    new_game.draw()

                if (cursor_button.region_check() and expand_settings):
                    cursor_button_sel.draw()
                elif(expand_settings):
                    cursor_button.draw()


            elif event.type == pygame.MOUSEBUTTONDOWN:
                print event.button
                for button in button_list:
                    if(button.region_check() and event.button == 1):
                        button.handle_event(event)

                if(event.button == 4 and pygame.key.get_pressed()[K_LSHIFT]):          # Scroll Up
                    if(CURSOR_SIZE > 229):
                        CURSOR_SIZE = 230
                    else:
                        CURSOR_SIZE *= 1.35

                if(event.button == 5 and pygame.key.get_pressed()[K_LSHIFT]):          # Scroll Down
                    if(CURSOR_SIZE < 1):
                        CURSOR_SIZE = 1
                    else:
                        CURSOR_SIZE /= 1.35

                if ((quit_loc_x() < pygame.mouse.get_pos()[0] < (quit_w + quit_loc_x())) and
                        quit_loc_y() < pygame.mouse.get_pos()[1] < (quit_h + quit_loc_y()) and
                        event.button == 1):
                    if debug:
                        print 'Exiting...'
                    if (profile):
                        pr.disable()
                        s = StringIO.StringIO()
                        sortby = 'cumulative'
                        ps = pstats.Stats(pr, stream=s.sort_stats(sortby))
                        ps.print_stats()
                        print s.getvalue()
                        log = open('profile_log', 'w')
                        log.write(s.getvalue())
                        log.close()
                    pygame.display.quit()

                """
                if (settings.x < pygame.mouse.get_pos()[0] < (settings.width + settings.x) and
                        settings.y < pygame.mouse.get_pos()[1] < (settings.height + settings.y)):
                    expand_settings = not expand_settings
                    settings.handle_event(event)

                if (cursor_button.x < pygame.mouse.get_pos()[0] < (cursor_button.width + cursor_button.x) and
                        cursor_button.y < pygame.mouse.get_pos()[1] < (cursor_button.height + cursor_button.y) and
                        expand_settings):
                    cursor_current = config.get('Display', 'cursor')
                    if(cursor_current == 'True'):                        
                        config.set('Display', 'cursor', 'False')
                    else:
                        config.set('Display', 'cursor', 'True')
                    conf_file = open(CONFIG_FILE, 'w')
                    config.write(conf_file)
                    conf_file.close()
                    pygame.mouse.set_visible('True' == config.get('Display', 'cursor'))
                """

        # Draw mouse cursor thing
        if(config.get('Display', 'cursor') == 'False'):
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


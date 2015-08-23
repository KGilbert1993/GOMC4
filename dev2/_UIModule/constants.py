"""
    Button Constants
"""

import sys
sys.path.append("../")
from game_constants import *
from menu import *
import pygame

quit_w = 53
quit_h = 20

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
import pygame
from pygame.font import *

def draw(screen, scores = None):
    screen_size = screen.get_size()
    centre = (screen_size[0]/2 if screen_size[0] != 0 else 0, screen_size[1]/2 if screen_size[1] != 0 else 0)
    scoreboard_size = (400,300)

    # scoreboard = pygame.Rect(width=scoreboard_size[0],height=scoreboard_size[1])
    # scoreboard.center = centre

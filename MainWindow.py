import pygame
from pygame.locals import *
import numpy as np


pygame.init()
screen_dims = (750,569)
screen = pygame.display.set_mode(screen_dims)
pygame.display.set_caption("Pygame Demo")

bg = pygame.image.load("background.jpg").convert()
donut = pygame.image.load("donut.png").convert_alpha()
screen.blit(bg, (0, 0))

donut_coords = np.array(screen_dims)[:]

def pause_game():
    return

game_exit = False
motion = False
while not game_exit:
    for event in pygame.event.get():
    
        if event.type == QUIT:
            game_exit = True
            
        elif event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pause_game()
                
            if keys[K_UP]:
                if not motion:
                    motion = True
                
            # if keys[K_DOWN]:
                
    screen.blit(bg, (0,0))
    screen.blit(donut, (donut_coords[0], donut_coords[1]))
    pygame.display.update()
pygame.quit()
quit()
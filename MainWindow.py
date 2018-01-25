import pygame
from pygame.locals import *
import numpy as np


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen_dims = (750,569)
screen = pygame.display.set_mode(screen_dims)
screen.fill([255, 255, 255])
pygame.display.set_caption("Pygame Demo")

bg = pygame.image.load("background.jpg").convert()
donut = pygame.image.load("donut.png").convert_alpha()

screen.blit(bg, (0, 0))

donut_coords = np.array([screen_dims[0]/4, screen_dims[1]/2])
screen.blit(donut, (donut_coords[0], donut_coords[1]))

myfont = pygame.font.SysFont('Comic Sans MS', 50)
# def display_msg(msg, col):
    
pillar_speed = 0
count = 0
speed = 0
gravity = 2
game_exit = False
started = False

while not game_exit:
    tick_time = clock.tick(50)
    if started:
        if speed >= -30:
            speed -= gravity
    
    for event in pygame.event.get():
    
        if event.type == QUIT:
            game_exit = True
            
        elif event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                started = False
                speed = 0
                pillar_speed = 0
                
            if keys[K_UP]:
                if not started:
                    started = True
                speed = 20
                pillar_speed = 2
    donut_coords[1] -= speed
    
    
    if donut_coords[1] >= screen_dims[1]-63:
        speed = 0
        pillar_speed = 0
        started = False
        textsurface = myfont.render('You lose!', True, (255, 0, 0))
    else:
        textsurface = myfont.render('{}'.format(count), True, (255, 0, 0))
    screen.blit(bg, (0,0))
    screen.blit(donut, (donut_coords[0], donut_coords[1]))
    screen.blit(textsurface, (screen_dims[0]/2, screen_dims[1]*0.05))
    pygame.display.update()
pygame.quit()
quit()
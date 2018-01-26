import pygame
from pygame.locals import *
import random

thug_mode = False

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen_dims = (750,569)
screen = pygame.display.set_mode(screen_dims)
screen.fill([255, 255, 255])
pygame.display.set_caption("Pygame Demo")

if thug_mode:
    bg = pygame.image.load("./data/background.png").convert()
    donut = pygame.image.load("./data/sprite2.png").convert_alpha()
else:
    bg = pygame.image.load("background.jpg").convert()
    donut = pygame.image.load("beaker.png").convert_alpha()
    
screen.blit(bg, (0, 0))

donut_coords = [screen_dims[0]/4, screen_dims[1]/2]
screen.blit(donut, (donut_coords[0], donut_coords[1]))

myfont = pygame.font.SysFont('Comic Sans MS', 50)
# def display_msg(msg, col):

pillar_timer = 0
pillar_trigger = 60
pillar_speed = 0
pillar_gap = 200
pillar_width = 25
pillars = []
count = 0
speed = 0
gravity = 2
game_exit = False
started = False

while not game_exit:
    tick_time = clock.tick(60)
    
    if started:
        pillar_timer = (pillar_timer+1) % pillar_trigger
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
                pillar_speed = 5
    
    
    if pillar_timer == pillar_trigger-1:
        pillars.append([screen_dims[0], random.randrange(0+screen_dims[1]//5, round(screen_dims[1]*0.8)), False])
        print(pillars)
    
    if started:
        if pillars:
            if pillars[0][0] <= 0:
                pillars = pillars[1:]
            for pil in pillars:
                pil[0] -= pillar_speed
                # pygame.draw.rect(screen, (25, 25, 25), [pil[0], pil[1], pillar_width, screen_dims[1]-pil[1]])
    # if len(pillars) != 0:
    
            
        
    donut_coords[1] -= speed
    
    screen.blit(bg, (0,0))
    screen.blit(donut, (donut_coords[0], donut_coords[1]))
    
    
    for pil in pillars:
        if pil[0] <= donut_coords[0] and not pil[2]:
            pil[2] = True
            count += 1
        screen.fill((75, 75, 75), [pil[0], pil[1], pillar_width, screen_dims[1]-pil[1]])
        screen.fill((75, 75, 75), [pil[0], 0, pillar_width, pil[1]- pillar_gap])
    if donut_coords[1] >= screen_dims[1]-63:
        speed = 0
        pillar_speed = 0
        started = False
        textsurface = myfont.render('You lose! You scored {}'.format(count), True, (255, 0, 0))
        screen.blit(textsurface, (screen_dims[0]/5, screen_dims[1]*0.05))
    else:
        textsurface = myfont.render('{}'.format(count), True, (255, 0, 0))
        screen.blit(textsurface, (screen_dims[0]/2, screen_dims[1]*0.05))
    pygame.display.flip()
pygame.quit()
quit()
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
with open("scores") as s:
    hs = s.read()
pygame.display.set_caption("Good ol' flap: High Score {}".format(hs))

if thug_mode:
    bg = pygame.image.load("./data/background.png").convert()
    donut = pygame.image.load("./data/sprite2.png").convert_alpha()
else:
    bg = pygame.image.load("background.jpg").convert()
    donut = pygame.image.load("beaker.png").convert_alpha()
    
screen.blit(bg, (0, 0))

donut_coords = [screen_dims[0]/4, screen_dims[1]/2]
screen.blit(donut, (donut_coords[0], donut_coords[1]))

if thug_mode:
    myfont = pygame.font.Font('./data/OLDENGL.TTF', 60)
else:
    myfont = pygame.font.SysFont('Comic Sans MS', 60)

    
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
lost = False
top_score = hs

while not game_exit:
    tick_time = clock.tick(60)
    
    if started:
        pillar_timer = (pillar_timer+1) % pillar_trigger
        if speed >= -30:
            speed -= gravity
    
    for event in pygame.event.get():
    
        if event.type == QUIT:
            if count > int(hs):
                hs = count
                with open("scores", 'w') as f: 
                    f.write(str(hs)) 
            pygame.quit()
            quit()
            
        elif event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                started = False
                speed = 0
                pillar_speed = 0
            
            if keys[K_RETURN]:
                donut_coords = [screen_dims[0]/4, screen_dims[1]/2]
                started = False
                speed = 0
                pillar_speed = 0
                pillars = []
                if count > int(hs):
                    hs = count
                count = 0
                speed = 0
                lost = False
                pillar_timer = 0
                
            if keys[K_UP]:
                if not started:
                    started = True
                speed = 20
                pillar_speed = 5
    
    if pillar_timer == pillar_trigger-1:
        pillars.append([screen_dims[0], random.randrange(0+screen_dims[1]//5, round(screen_dims[1]*0.8)), False])
    
    if started:
        if pillars:
            if pillars[0][0] <= 0:
                pillars = pillars[1:]
            for pil in pillars:
                pil[0] -= pillar_speed

    donut_coords[1] -= speed
    
    screen.blit(bg, (0,0))
    screen.blit(donut, (donut_coords[0], donut_coords[1]))
    
    for pil in pillars:
        if (pil[0] < donut_coords[0]+30) and (pil[0] > donut_coords[0]):
            if (donut_coords[1] <= screen_dims[1] - pil[1] - pillar_gap-30) or (donut_coords[1] >= pil[1]+30):
                started = False
                speed = 0
                pillar_speed = 0
                lost = True
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
        screen.blit(textsurface, (screen_dims[0]/6, screen_dims[1]*0.05))
    elif lost:
        textsurface = myfont.render('You lose! You scored {}'.format(count), True, (255, 0, 0))
        screen.blit(textsurface, (screen_dims[0]/6, screen_dims[1]*0.05))
    else:
        textsurface = myfont.render('{}'.format(count), True, (255, 0, 0))
        screen.blit(textsurface, (screen_dims[0]/2, screen_dims[1]*0.05))
    
    pygame.display.flip()
    
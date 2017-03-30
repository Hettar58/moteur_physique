# -*- coding: utf-8 -*-

#IMPORTS ---------------------------------
from pygame import *
from pygame.locals import *
from math import *
import sys
#/IMPORTS --------------------------------


#INIT ------------------------------------
init()
width = 800
height = 600
screen = display.set_mode([width, height], 0, 32)
#/INIT------------------------------------


#VARS-------------------------------------
t = time.get_ticks()
t_o = time.get_ticks()
clock = time.Clock()

box_X = 0                           #position X
box_Y = screen.get_height()-10      #position Y
g = 9.81                            #gravité terrestre
angle = 80*3.14/180                 #angle (en radian)
masse = 10                          #masse
ax = 0                              #accélération sur X
ay = masse * g                      #accélération sur Y
velocite = 250                      #vélocité initiale
vx = velocite * cos(angle)          #vélocité sur axe X  
vy = -velocite * sin(angle)         #vélocité sur axe Y

sol_X = 0
sol_Y = 590
dp = 0                              #différence de position entre la boite et le sol
#/VARS------------------------------------


#TEXTURES --------------------------------
blanc = (255, 255, 255)
screen.fill(blanc)

box = image.load("square.png")
screen.blit(box, (box_X, box_Y))

sol = image.load("ground_texture.png")
screen.blit(sol,(sol_X, sol_Y))
#/TEXTURES -------------------------------

#MAIN LOOP -------------------------------
continuer = True
while continuer == True:
    
    #EVENTS ------------------------------
    for evenement in event.get():
        if evenement.type == QUIT:
            continuer = False
        elif evenement.type == KEYDOWN and evenement.key == K_ESCAPE:
            continuer = False
    #/EVENTS -----------------------------
            
    #PROCESSING --------------------------
    clock.tick(60)
    t = time.get_ticks()
    dt =  (t - t_o) * 0.001
    t_o = t

    vx += ax * dt
    vy += ay * dt
    box_X += vx * dt
    box_Y += vy * dt

    

 
    screen.fill(blanc)
    screen.blit(sol, (sol_X, sol_Y))
    screen.blit(box, (box_X, box_Y))
    display.flip()

    print(val)
    #/PROCESSING -------------------------
    
#/MAIN LOOP -----------------------------

quit()

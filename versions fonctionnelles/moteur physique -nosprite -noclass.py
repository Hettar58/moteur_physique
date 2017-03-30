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
t = time.get_ticks()                #temps de rendu de la frame actuelle
t_o = time.get_ticks()              #temps de la frame d'avant
clock = time.Clock()                #horloge
box_X = 10                           #position X
box_Y = screen.get_height() -30     #position Y
g = 9.81                            #gravité terrestre
angle = 80*3.14/180                 #angle (en radian)
masse = 10                          #masse
ax = 0                              #accélération sur X
ay = masse * g                      #accélération sur Y
velocite = 250                      #vélocité initiale
vx = velocite * cos(angle)          #vélocité sur axe X  
vy = -velocite * sin(angle)         #vélocité sur axe Y
dx = 0
dy = 0
mousepos_origin = []
mousepos_last = []
mouseInPlace = False
move = True
clic = False
capture = True
hauteur_ecran = screen.get_height()
#/VARS------------------------------------


#TEXTURES --------------------------------
blanc = (255, 255, 255)
screen.fill(blanc)

box = image.load("square.png")
screen.blit(box, (box_X, box_Y))

ground = image.load("ground_texture.png")
screen.blit(ground, (0, hauteur_ecran -10))
#/TEXTURES -------------------------------

#MAIN LOOP -------------------------------
continuer = True
while continuer == True:
    
    mousepos = mouse.get_pos()
    if box_X < mousepos[0] < box_X + 21 and box_Y < mousepos[1] < box_Y + 21:
        mouseInPlace = True
    else:
        mouseInPlace = False
        
    #EVENTS ------------------------------
        
    for evenement in event.get():
        if evenement.type == QUIT:
            continuer = False
        elif evenement.type == KEYDOWN and evenement.key == K_ESCAPE:
            continuer = False
        elif evenement.type == MOUSEBUTTONDOWN and mouseInPlace == True:
            move = False
            clic = True
            if capture == True:
                mousepos_origin = mousepos
                capture = False
        elif evenement.type == MOUSEBUTTONUP and clic == True:
            mousepos_last = mousepos
            dx = mousepos_last[0] - mousepos_origin[0]
            dy = mousepos_last[1] - mousepos_origin[1]
            print(dx, dy)
            velocite = sqrt(dx**2 + dy**2) * 2
            angle = atan2(dy, dx)
            print(angle)
            vx = velocite * cos(angle)
            vy = -velocite * sin(angle)
            move = True
            clic = False
            capture = True
        elif evenement.type == MOUSEMOTION and move == False and clic == True:
            box_X = mousepos[0] - 10
            box_Y = mousepos[1] - 10   
    #/EVENTS -----------------------------
            
    #PROCESSING -------------------------
    clock.tick(60)
    t = time.get_ticks()
    dt =  (t - t_o) * 0.001
    t_o = t
        
    if move == True:   
        vx += ax * dt
        vy += ay * dt
        box_X += vx * dt
        box_Y += vy * dt
        
        if (int(box_Y) >= hauteur_ecran-30):
            vy = -vy * 0.80
            vx = vx * 0.80

    #RENDER -----------------------------    
    screen.fill(blanc)
    screen.blit(ground, (0, hauteur_ecran -10))
    screen.blit(box, (box_X, box_Y))
    display.flip()
    #/RENDER ----------------------------

    print("velocite:", velocite, "angle", angle, "dx/dy", dx, dy,"vx/vy",  vx, vy)         #DEBUG 
    
    #/PROCESSING -------------------------
    
#/MAIN LOOP -----------------------------

quit()

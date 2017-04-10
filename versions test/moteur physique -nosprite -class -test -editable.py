# -*- coding: utf-8 -*-

#IMPORTS ----------------------------------------
from pygame import *
from pygame.locals import *
from math import *
import sys
import string
#/IMPORTS ---------------------------------------


#INIT -------------------------------------------
init()
width = 800
height = 600
screen = display.set_mode([width, height], 0, 32)
#/INIT --------------------------------------------

#CLASS -----------------------------------
class Objet:
    def __init__(self, name, x, y, angle, masse, velocite):
        global mousepos, mousepos_last, mousepos_origin, dx, dy, mouseInPlace, objectToMove, allBoxes
        
        self.x = x
        self.y = y #screen.get_height() - 30
        self.angle = angle
        self.masse = masse
        self.velocite = velocite
        self.ax = 0
        self.ay = masse * g
        self.vx = velocite * cos(angle)
        self.vy = -velocite * sin(angle)
        self.image = image.load("square.png")
        self.move = True
        allBoxes.append(name)
        
    def render(self):
        screen.blit(self.image, (self.x, self.y))

    def isMouseOnPos(self):
        global mousepos, mousepos_last, mousepos_origin, dx, dy, mouseInPlace, objectToMove
        
        if self.x < mousepos[0] < self.x+ 21 and self.y < mousepos[1] < self.y + 21:
            self.mouseInPlace = True
        else:
            self.mouseInPlace = False
            
    def moveBox(self):
        if self.move == True:
            self.vx += self.ax * dt
            self.vy += self.ay * dt
            self.x += self.vx * dt
            self.y += self.vy * dt           
        if int(self.y) >= hauteur_ecran-30:
            self.vy = -self.vy * 0.80
            self.vx = self.vx * 0.80
        if int(self.x + 21) >= bloc.x and bloc.y < self.y < bloc.y + 50 :
            self.vx = -self.vx
        if int(self.y + 21) >= bloc.y and bloc.x < self.x < bloc.x + 50 :
            self.vy = -self.vy
            
    def eventScan(self):
        global mousepos, mousepos_last, mousepos_origin, dx, dy, mouseInPlace, objectToMove, clic, capture
        
        if evenement.type == MOUSEBUTTONDOWN and self.mouseInPlace == True and box2.move == True:
            self.move = False
            clic = True
            if capture == True:
                mousepos_origin = mousepos
                capture = False
        elif evenement.type == MOUSEBUTTONUP and clic == True and self.move == False:
            mousepos_last = mousepos
            dx = mousepos_last[0] - mousepos_origin[0]
            dy = mousepos_last[1] - mousepos_origin[1]
            self.velocite = sqrt(dx**2 + dy**2) * 2
            self.angle = atan2(dy, dx)
            self.vx = self.velocite * cos(self.angle)
            self.vy = -self.velocite * sin(self.angle)
            self.move = True
            clic = False
            capture = True
        elif evenement.type == MOUSEMOTION and self.move == False and clic == True:
            self.x = mousepos[0]
            self.y = mousepos[1]
            
class Bloc:
    def __init__(self):
        self.x = 600
        self.y = 540
        self.texture = image.load("square.png")
        self.image = transform.smoothscale(self.texture, (50, 50))
        
    def render(self):
        screen.blit(self.image, (self.x, self.y))

#VARS_GENERAL -------------------------------------
t = time.get_ticks()                #temps de rendu de la frame actuelle
t_o = time.get_ticks()              #temps de la frame d'avant
clock = time.Clock()                #horloge
g = 9.81                            #gravité terrestre
dx = 0                              #différence entre le X d'origine de la souris et celui d'arrivée
dy = 0                              #différence entre le Y d'origine de la souris et celui d'arrivée
mousepos_origin = []                #position de la souris à l'origine
mousepos_last = []                  #dernière position de la souris
mouseInPlace = False                #est ce que la souris est dans la boite ?
move = True                         #est ce que le bloc peut bouger ?
clic = False                        #est ce que un bouton de la souris est appuyé ?
capture = True                      #est ce que l'on peut prendre la psition de la souris ?
hauteur_ecran = screen.get_height() #la hauteur de l'écran
nbBoites = 2
allBoxes = []
#/VARS_GENERAL ------------------------------------
      
#TEXTURES --------------------------------
blanc = (255, 255, 255)
screen.fill(blanc)

ground = image.load("ground_texture.png")
screen.blit(ground, (0, hauteur_ecran -10))
#/TEXTURES -------------------------------


#MAIN LOOP -------------------------------
#--- = objet (numéro, posX, posY, angle, masse, vélocité)
box = Objet("box", 20, hauteur_ecran - 30, 45*3.14/180, 10, 250)
box2 = Objet("box2",  30,  hauteur_ecran -40, 50*3.14/180, 10, 250)
bloc = Bloc()

continuer = True
while continuer == True:
    
    mousepos = mouse.get_pos()
    
    box.isMouseOnPos()
    box2.isMouseOnPos()
        
    #EVENTS ------------------------------
    for evenement in event.get():
        if evenement.type == QUIT:
            continuer = False
        elif evenement.type == KEYDOWN and evenement.key == K_ESCAPE:
            continuer = False
        elif evenement.type == KEYDOWN and evenement.key == K_c:
            box.move = False
            box2.move = False
            i_type = str(input("quel type d'objet voulez vous ? (bloc ou objet) \n"))
            print(i_type)
            if i_type == "objet":
                nbBoites += 1
                i_name = "box" + str(nbBoites)
                i_posX = int(input("entrez la position X de départ\n"))
                i_posY = int(input("entrez la position Y de départ\n"))
                i_angle = int(input("entrez l'angle de l'objet\n"))
                i_angle *= 3.14/180
                i_masse = int(input("entrez la masse de l'objet\n"))
                i_velocite = int(input("entrez la vélocité de l'objet\n"))
                v = locals()
                v["box%d" % nbBoites] = Objet(i_name, i_posX, i_posY, i_angle, i_masse, i_velocite)
                print(allBoxes)
                print(box3.name)
                
        
            
    box.eventScan()
    box2.eventScan()
    #/BOX_2-----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
    #/EVENTS -----------------------------
            
    #PROCESSING -------------------------
    clock.tick(60)
    t = time.get_ticks()
    dt =  (t - t_o) * 0.001
    t_o = t

    allBoxes[0] = box
    allBoxes[0].moveBox()
    allBoxes[1] = box2
    allBoxes[1].moveBox()
        
    #RENDER -----------------------------    
    screen.fill(blanc)
    screen.blit(ground, (0, hauteur_ecran -10))
    
    box.render()
    box2.render()
        
    bloc.render()
    display.flip()
    #/RENDER ----------------------------

             #DEBUG 
    
    #/PROCESSING -------------------------
    
#/MAIN LOOP -----------------------------

quit()

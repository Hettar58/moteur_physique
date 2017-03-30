# -*- coding: utf-8 -*-

#IMPORTS ----------------------------------------
from pygame import *
from pygame.locals import *
from math import *
import sys
#/IMPORTS ---------------------------------------


#INIT -------------------------------------------
init()
width = 800
height = 600
screen = display.set_mode([width, height], 0, 32)
#/INIT --------------------------------------------

#VARS_GENERAL -------------------------------------
t = time.get_ticks()                #temps de rendu de la frame actuelle
t_o = time.get_ticks()              #temps de la frame d'avant
clock = time.Clock()                #horloge
g = 9.81                            #gravit√© terrestre
dx = 0                              #diff√©rence entre le X d'origine de la souris et celui d'arriv√©e
dy = 0                              #diff√©rence entre le Y d'origine de la souris et celui d'arriv√©e
mousepos_origin = []                #position de la souris √† l'origine
mousepos_last = []                  #derni√®re position de la souris
mouseInPlace = False                #est ce que la souris est dans la boite ?
move = True                         #est ce que le bloc peut bouger ?
clic = False                        #est ce que un bouton de la souris est appuy√© ?
capture = True                      #est ce que l'on peut prendre la psition de la souris ?
hauteur_ecran = screen.get_height() #la hauteur de l'√©cran
#/VARS_GENERAL ------------------------------------

#CLASS -----------------------------------
class Objet:
    def __init__(self, number, x, y, angle, masse, velocite):
        global mousepos, mousepos_last, mousepos_origin, dx, dy, mouseInPlace, objectToMove
        
        self.number = number
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
        if (int(self.y) >= hauteur_ecran-30):
            self.vy = -self.vy * 1.005
            self.vx = self.vx * 1.005
        if (int(self.y) <= 0):
            self.vy = -self.vy * 1.005
            self.vx = self.vx * 1.005
        if (int(self.x) <= 0):
            self.vx = -self.vx * 1.005
        if (int(self.x) >= (screen.get_width()- 20)):
            self.vx = -self.vx * 1.005
            
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
#/CLASS ----------------------------------
        
#TEXTURES --------------------------------
blanc = (255, 255, 255)
screen.fill(blanc)

ground = image.load("ground_texture.png")
screen.blit(ground, (0, hauteur_ecran -10))
#/TEXTURES -------------------------------

#MAIN LOOP -------------------------------

box = Objet(0, 20, hauteur_ecran - 30, 80*3.14/180, 10, -10)
box2 = Objet(1, 30,  hauteur_ecran -40, 50*3.14/180, 20, 300)
box3 = Objet(2, 40,  hauteur_ecran -65, 45*3.14/180, 30, 250)
box4 = Objet(3, 60,  hauteur_ecran -35, 78*3.14/180, 40, 300)
box5 = Objet(4, 30,  hauteur_ecran -50, 70*3.14/180, -10, 350)
box6 = Objet(5, 35,  hauteur_ecran -55, 22*3.14/180, 60, 400)
box7 = Objet(6, 45,  hauteur_ecran -60, 64*3.14/180, 70, 450)
box8 = Objet(7, 50,  hauteur_ecran -63, 128*3.14/180, 80, 10)
box9 = Objet(8, 55,  hauteur_ecran -80, 360*3.14/180, 20, 0)
box10 = Objet(9, 65,  hauteur_ecran -85, 40*3.14/180, 0, 110)
box11 = Objet(9, 70,  hauteur_ecran -90, 45*3.14/180, 12, 110)
box12 = Objet(9, 75,  hauteur_ecran -95, 50*3.14/180, 65, 110)
box13 = Objet(9, 80,  hauteur_ecran -100, 55*3.14/180, 87, 110)
box14 = Objet(9, 85,  hauteur_ecran -105, 60*3.14/180, 12, 110)
box15 = Objet(9, 90,  hauteur_ecran -110, 56*3.14/180, 36, 110)
box16 = Objet(9, 95,  hauteur_ecran -115, 65*3.14/180, 66, 110)
box17 = Objet(9, 100,  hauteur_ecran -120, 70*3.14/180, 45, 110)
box18 = Objet(9, 105,  hauteur_ecran -125, 75*3.14/180, 21, 110)
box19 = Objet(9, 110,  hauteur_ecran -130, 80*3.14/180, 5, 110)
box20 = Objet(9, 115,  hauteur_ecran -135, 85*3.14/180, 74, 110)
box21 = Objet(9, 120,  hauteur_ecran -140, 90*3.14/180, 65, 110)
box22 = Objet(9, 125,  hauteur_ecran -145, 95*3.14/180, 99, 110)
box23 = Objet(9, 130,  hauteur_ecran -150, 99*3.14/180, 21, 110)
box24 = Objet(9, 135,  hauteur_ecran -155, 100*3.14/180, 62, 110)
box25 = Objet(9, 140,  hauteur_ecran -160, 105*3.14/180, 85, 110)
box26 = Objet(9, 145,  hauteur_ecran -165, 120*3.14/180, 62, 110)
box27 = Objet(9, 150,  hauteur_ecran -170, 720*3.14/180, 20, 110)
box28 = Objet(9, 155,  hauteur_ecran -175, 666*3.14/180, 58, 110)
box29 = Objet(9, 160,  hauteur_ecran -180, 142*3.14/180, 45, 110)
box30 = Objet(9, 165,  hauteur_ecran -185, 584*3.14/180, 46, 110)






continuer = True
while continuer == True:
    
    mousepos = mouse.get_pos()
    
    box.isMouseOnPos()
    box2.isMouseOnPos()
    box3.isMouseOnPos()
    box4.isMouseOnPos()
    box5.isMouseOnPos()
    box6.isMouseOnPos()
    box7.isMouseOnPos()
    box8.isMouseOnPos()
    box9.isMouseOnPos()
    box10.isMouseOnPos()
    box11.isMouseOnPos()
    box12.isMouseOnPos()
    box13.isMouseOnPos()
    box14.isMouseOnPos()
    box15.isMouseOnPos()
    box16.isMouseOnPos()
    box17.isMouseOnPos()
    box18.isMouseOnPos()
    box19.isMouseOnPos()
    box20.isMouseOnPos()
    box21.isMouseOnPos()
    box22.isMouseOnPos()
    box23.isMouseOnPos()
    box24.isMouseOnPos()
    box25.isMouseOnPos()
    box26.isMouseOnPos()
    box27.isMouseOnPos()
    box28.isMouseOnPos()
    box29.isMouseOnPos()
    box30.isMouseOnPos()
    
        
    #EVENTS ------------------------------
    for evenement in event.get():
        if evenement.type == QUIT:
            continuer = False
        elif evenement.type == KEYDOWN and evenement.key == K_ESCAPE:
            continuer = False
            
        box.eventScan()
        box2.eventScan()
        box3.eventScan()
        box4.eventScan()
        box5.eventScan()
        box6.eventScan()
        box7.eventScan()
        box8.eventScan()
        box9.eventScan()
        box10.eventScan()
        box11.eventScan()
        box12.eventScan()
        box13.eventScan()
        box14.eventScan()
        box15.eventScan()
        box16.eventScan()
        box17.eventScan()
        box18.eventScan()
        box19.eventScan()
        box20.eventScan()
      .           \ŸLmJmJ ⁄LmJéa    ..          \ŸLmJmJ ⁄LmJça    Âi   ˇˇˇˇˇˇ mˇˇˇˇˇˇˇˇˇˇˇˇ  ˇˇˇˇÂw i n p r  mo f i l e .   i n ÂINPRO~1INI  d¯LmJmJ  MmJía7  ÂEADME  TXT ≥¯LmJmJ  MmJìag  ÂOIT    LOG ¥¯LmJmJ  ˘LmJîaÃ  ÂLD     ZIP √¯LmJmJ  ˙LmJòaz  ÂLD     LST √¯LmJmJ  ˙LmJôad   ÂLD     TXT √¯LmJmJ  ˙LmJóa  ÂOIT    LOG ¥¯LmJmJ  MmJîa¡  ÂEW     ZIP √¯LmJmJ  MmJüaz  ÂEW     LST √¯LmJmJ  MmJ†ad   ÂEW     TXT √¯LmJmJ  MmJña                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
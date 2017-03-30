# -*- coding: utf-8 -*-
from pygame import *
from pygame.locals import * 
from math import * 
import sys

init()
width = 800
height = 600
screen = display.set_mode([width, height])
key.set_repeat(450, 20)

g = 9.81

t = time.get_ticks()
clock = time.Clock()
t_o = time.get_ticks()

blanc = (255, 255, 255)
screen.fill(blanc)

class Objet(sprite.Sprite):
	g = 9.81
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = image.load("square.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 0                                 #position X
		self.rect.y = screen.get_height() - 10                                #position Y

		self.angle = 80*3.14/180                        #angle thêta (en degrés)
		self.masse = 10
		self.ax = 0                                     #accélération sur axe X
		self.ay = self.masse * g                                    #accélération sur axe Y

		self.velocite = 250                                   #vitesse initiale ( en m/s)
		self.vx = self.velocite*cos(self.angle)		#vitesse initiale sur l'axe X
		self.vy = -self.velocite*sin(self.angle)	#vitesse initiale sur l'axe Y

		self.nx = 0
		self.ny = screen.get_height() - 10 
	def move(self, dt):
		self.vx += self.ax*dt
		self.vy += self.ay*dt
		self.nx += self.vx * dt
		self.ny += self.vy * dt

		
		
objet = Objet()
allsprites = sprite.RenderPlain((objet))

continuer = True
while continuer == True:
	#EVENTS -------------------------------------
	for evenement in event.get():
		if evenement.type == QUIT:
			continuer = False
		elif evenement.type == KEYDOWN:
			if evenement.key == K_ESCAPE:
				continuer = False
	#/EVENTS -------------------------------------

	#PROCESSING ----------------------------------
	clock.tick(60)
	t = time.get_ticks()
	dt = (t - t_o) * 0.001
	t_o = t
	objet.move(dt)
	
	screen.fill(blanc)
	allsprites.draw(screen)
	display.flip()
	#/PROCESSING ---------------------------------
	
quit()

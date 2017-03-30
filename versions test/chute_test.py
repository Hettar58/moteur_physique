from pygame import * 
from pygame.locals import * 
from math import *  
import sys

init()
width = 800
height = 600
screen = display.set_mode([width, height], RESIZABLE)

gravity = 9.81
key.set_repeat(450, 20)

t = 0
time.Clock()

class Objet(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = image.load("square.png").convert_alpha()
		self.rect = self.image.get_rect()

		self.rect.x = 0
		self.x_origine = 0
		self.newX = 0

		self.rect.y = 0
		self.y_origine = 0
		self.newY = 0

		self.poids = 1
		self.angle = 0
		self.vitesse = 0

	def move(self):
		self.cos_angle = cos(self.angle)
		self.newX = self.vitesse * self.cos_angle * t + x_origine
		self.rect.x = self.newX

		self.sin_angle = sin(self.angle)
		self.pow_time = pow(t, 2)
		self.newY = -0.5 * gravity * pow_time + self.vitesse * sin_angle * t + self.y_origine
		self.rect.y = self.newY



display.flip()

objet = Objet()
allsprites = sprite.RenderPlain ((objet))

continuer = True
while continuer == true:
	for evenement in event.get():
		if evenement.type == QUIT:
			continuer = False

		elif evenement.type == KEYDOWN:
			if evenement.key == K_ESCAPE:
				continuer = False
	
	timer.tick(60)
	t = t + timer.get_time() / 1000
	print (t)
	allsprites.draw(screen)
	display.flip()
	#placer code ici

quit()

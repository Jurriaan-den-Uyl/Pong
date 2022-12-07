import pygame
import math
from random import uniform
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
		super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
 
        # Draw the ball!
		pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()
	
	#move function. Updates x and y coordinates seperately with respect to angle + collision check for top and bottom sides.
	def move(self, vilocity, angle):
		self.rect.x += vilocity*math.sin(angle)
		self.rect.y += vilocity*math.cos(angle)
		if self.rect.x < -10:
			return 2
		if self.rect.x > 800:
			return 1
		if self.rect.y < 0:
			self.rect.y = 0
		if self.rect.y > 490:
			self.rect.y = 490
		return 0
	
	#collisioncheck for the A paddle
	def collisionCheckA(self, collisiony):
		if self.rect.x in range(20, 27) and collisiony <= self.rect.y <= collisiony+80:
			return True
	
	#collisioncheck for the B paddle
	def collisionCheckB(self, collisiony):
		if self.rect.x in range(763, 770) and collisiony <= self.rect.y <= collisiony+80:
			return True
	
	#collisioncheck for the sides.
	def collisionCheckSides(self,angle):
		if self.rect.y == 0:
			return True
		if self.rect.y == 490:
			return True
	
	#reset function for the ball
	def ballReset(self):
		self.rect.x = 400
		self.rect.y	= 250
		nbr = uniform(0.25, 1.25)
		if nbr >= 0.75:
			nbr += 0.5
		angle = nbr*math.pi
		return angle
		
import pygame
BLACK = (0,0,0)

class Text(pygame.font.init):
	def __init__(self, color, width, height):
        # Call the parent class (font) constructor
		super().__init__()
        
        # Pass in the color of the tekst, its width and height.
        # Set the background color and set it to be transparent
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
 
        # Draw the tekst!
		pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()
	
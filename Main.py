#pong
import pygame
from random import uniform
from time import sleep
from math import pi
from paddle import Paddle
from ball import Ball

# init
pygame.init()

# colours
black = (0,0,0)
white = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

# True value for running program
run = True

#clock for updating game
clock = pygame.time.Clock()

# init screen
scr_width=800
scr_height=500
screen = pygame.display.set_mode(size=([scr_width, scr_height]))
pygame.display.set_caption('pong')

#sprites
paddleA = Paddle(white, 10, 80)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(white, 10, 80)
paddleB.rect.x = 770
paddleB.rect.y = 200

ball = Ball(white, 10, 10)
ball.rect.x = 400
ball.rect.y	= 250
vilocity = 5

#scores
scoreA = 0
scoreB = 0

#text generation
number_font  = pygame.font.SysFont( None, 45 )

#scores for player A and B
number_image = number_font.render( str(scoreA), True, white, black )
number_image2 = number_font.render( str(scoreB), True, white, black )
text_rect_obj = number_image.get_rect()
text_rect_obj.center = (200, 150)
text_rect_obj2 = number_image2.get_rect()
text_rect_obj2.center = (600, 150)
screen.blit(number_image, text_rect_obj)
screen.blit(number_image2, text_rect_obj2)

#generating a random angle for ball within 0.25 to 0.75 pi and 1.25 and 1.75 pi
nbr = uniform(0.25, 1.25)
if nbr >= 0.75:
	nbr += 0.5
angle = nbr*pi

#list that will contain all the sprites
all_sprites_list = pygame.sprite.Group()
 
# Add the paddles and bal to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#main loop with exit functionality
while run:

	for ev in pygame.event.get():

		if ev.type == pygame.QUIT:
			run = False

	#moving the paddles
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddleA.moveUp(5)
	if keys[pygame.K_s]:
		paddleA.moveDown(5)
	if keys[pygame.K_UP]:
		paddleB.moveUp(5)
	if keys[pygame.K_DOWN]:
		paddleB.moveDown(5)
	
	#collision checks + adding a random extra angle to prefend horizontal deadlock
	if ball.collisionCheckB(paddleB.rect.y) == True:
		angle = -angle+uniform(-0.1,0.1)
	if ball.collisionCheckA(paddleA.rect.y) == True:
		angle = -angle+uniform(-0.1,0.1)
	if ball.collisionCheckSides(angle) == True:
		angle = pi-angle+uniform(-0.1,0.1)

	#moving the ball
	win = ball.move(vilocity,angle)
	
	#checking if there is a win + reset ball to centre with random angle
	if win == 1:
		scoreA += 1
		angle = ball.ballReset()
		sleep(1)
	if win == 2:
		scoreB += 1
		angle = ball.ballReset()
		sleep(1)

	#update all sprites in list.
	all_sprites_list.update()
	
	# clear the screen to black. 
	screen.fill(black)
	
	#Draw the net
	pygame.draw.line(screen, white, [scr_width/2, 0], [scr_width/2, scr_height], 5)
	
	#Update/draw text for the scores.
	number_image = number_font.render( str(scoreA), True, white, black )
	number_image2 = number_font.render( str(scoreB), True, white, black )
	screen.blit(number_image, text_rect_obj)
	screen.blit(number_image2, text_rect_obj2)
	
	#draw sprites
	all_sprites_list.draw(screen) 
	
	#update the screen
	pygame.display.flip()
     
	#Limit to 60 frames per second
	clock.tick(60)

#exit
pygame.quit()
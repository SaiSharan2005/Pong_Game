import pygame , sys
import time

def player_movement(keys , player):
	if keys[pygame.K_UP] and player.top >=0 :
		player.y -= player_speed
	if keys[pygame.K_DOWN] and player.bottom <= screen_height:
		player.y += player_speed

def ball_movement(ball):
	global ball_speed_x ,ball_speed_y
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1

	if ball.right <= 0 or ball.left >= screen_width:
		ball.x = screen_width/2 - 10 
		ball.y = screen_height/2 - 10
		time.sleep(0.2)

	if ball.colliderect(player) or ball.colliderect(player_ai):
		ball_speed_x *= -1

def player_AI(player_ai , ball):
	
	# player_ai.y += player_AI_speed

	if player_ai.top < ball.y :
		player_ai.top += player_AI_speed

	if player_ai.bottom - 20 > ball.y :
		player_ai.bottom -= player_AI_speed 

	if player_ai.top <= 0:
		player_ai.top = 0

	if player_ai.bottom>= screen_height :
		player_ai.bottom = screen_height 

def	player_score():
	global player_AI_score , playerscore

	if ball.left == 0 :
		player_AI_score +=1

	if ball.right == screen_width :
		playerscore +=1

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
grey_colour = (128, 128, 128)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 10 , screen_height/2 - 10 , 20 , 20)
player = pygame.Rect(screen_width - 10 , screen_height/2 - 40, 20  , 80)
player_ai = pygame.Rect( 0 , screen_height/2 - 40 , 10 , 80)

# Ball Velocity
ball_speed_x = -7
ball_speed_y = -7

#Some other velocity
player_speed = 8
player_AI_speed =7
# vel = 4

#Score value
playerscore = 0
player_AI_score = 0 


while True:

	font = pygame.font.SysFont(None , 50)
	ply_score = font.render("SCORE : "+ str(player_AI_score) , True , grey_colour)

	AI_score = font.render("SCORE : "+ str(playerscore) , True , grey_colour)
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()

	player_movement(keys , player)
	ball_movement(ball )
	player_AI(player_ai , ball)
	player_score()

	# Drawing some stuff on screen
	screen.fill("Black")
	pygame.draw.line(screen , grey_colour , (screen_width/2 - 3 , 0), (screen_width/2 - 3 , screen_height), 6)
	pygame.draw.ellipse(screen,   'WHITE'  ,   ball   )
	pygame.draw.rect(screen   , grey_colour,  player  )
	pygame.draw.rect(screen   , grey_colour, player_ai)
	# print(player_AI_score , playerscore)

	#placeing the score on the screen
	screen.blit(AI_score, (200, 50 ))
	screen.blit(ply_score ,(700 , 50))


	pygame.display.update()




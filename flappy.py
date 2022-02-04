import pygame, sys

# draw the moving floor
def draw_floor():
	screen.blit(floor_surface, (floor_x_position,450))
	screen.blit(floor_surface, (floor_x_position + width,450))

# initialization
pygame.init()
height = 512
width = 288
screen = pygame.display.set_mode((width, height)) #width, height
clock = pygame.time.Clock()

#Game variables
gravity = 0.20
bird_movement = 0

# background surface
bg_surface = pygame.image.load('assets/background-day.png').convert()

# floor surface
floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_position = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50,height/2))

# game loop
while True:
	# event loop
	for event in pygame.event.get():
		# if user quits
		if event.type == pygame.QUIT:
			pygame.quit() 
			sys.exit()

		# if user presses any key on the keyboard
		if event.type == pygame.KEYDOWN:
			# if user presses spacebar while the game is active
			if event.key == pygame.K_SPACE:
				bird_movement = 0
				bird_movement -= 5
					
	screen.blit(bg_surface, (0,0))

	# Bird
	bird_movement += gravity
	bird_rect.centery += bird_movement
	screen.blit(bird_surface, bird_rect)

	# Floor
	floor_x_position -= 0.5
	draw_floor()
	if floor_x_position <= -width:
		floor_x_position = 0
	
	# update the display with the max refresh rate being 120hz
	pygame.display.update()
	clock.tick(120)
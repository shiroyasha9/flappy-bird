import pygame, sys, random

# draw the moving floor
def draw_floor():
	screen.blit(floor_surface, (floor_x_position,900))
	screen.blit(floor_surface, (floor_x_position + width,900))

# create the top and bottom pipes
def create_pipe():
	random_pipe_position = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_position))
	top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_position - 300))
	return bottom_pipe, top_pipe

# move the pipes and delete the pipes that are not visible
def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
	return visible_pipes

# draw the pipes on the screen
def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= height:
			screen.blit(pipe_surface, pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface, False, True)
			screen.blit(flip_pipe, pipe)

# check collision between the bird and the pipes or the top and bottom of the screen
def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			return False

	if bird_rect.top <= -100 or bird_rect.bottom >= 900:
		return False
	
	return True

# initialization
pygame.init()
# width = 576
# height = 1024
width = 432
height = 768
screen = pygame.display.set_mode((width, height)) #width, height
clock = pygame.time.Clock()

#Game variables
gravity = 0.20
bird_movement = 0
game_active = True

# background surface
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

# floor surface
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_position = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,384))

# pipe surface and pipe userevent
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 500, 600,700]

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
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement -= 8
			
			# if user presses spacebar while the game is not active
			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (100, 384)
				bird_movement = 0
		
		# custom event for spawning pipe
		if event.type == SPAWNPIPE:
			pipe_list.extend(create_pipe())
					
	screen.blit(bg_surface, (0,0))

	if game_active:
		# Bird
		bird_movement += gravity
		bird_rect.centery += bird_movement
		screen.blit(bird_surface, bird_rect)
		game_active = check_collision(pipe_list)

		# Pipes
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)
	else:
		pass

	# Floor
	floor_x_position -= 1
	draw_floor()
	if floor_x_position <= -width:
		floor_x_position = 0
	
	# update the display with the max refresh rate being 120hz
	pygame.display.update()
	clock.tick(120)
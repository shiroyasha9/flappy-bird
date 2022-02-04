import pygame, sys, random

# draw the moving floor
def draw_floor():
	screen.blit(floor_surface, (floor_x_position,450))
	screen.blit(floor_surface, (floor_x_position + width,450))

# create the top and bottom pipes
def create_pipe():
	random_pipe_position = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (350, random_pipe_position))
	top_pipe = pipe_surface.get_rect(midbottom = (350, random_pipe_position - 150))
	return bottom_pipe, top_pipe

# move the pipes and delete the pipes that are not visible
def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 3
	visible_pipes = [pipe for pipe in pipes if pipe.right > -25]
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

	if bird_rect.top <= -50 or bird_rect.bottom >= 450:
		return False
	
	return True

# rotate the bird while flapping
def rotate_bird(bird):
	return pygame.transform.rotate(bird, -bird_movement * 3)
	
# animate the bird flap
def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center = (50, bird_rect.centery))
	return new_bird, new_bird_rect

# initialization
pygame.init()
height = 512
width = 288
screen = pygame.display.set_mode((width, height)) #width, height
clock = pygame.time.Clock()

#Game variables
gravity = 0.20
bird_movement = 0
game_active = True

# background surface
bg_surface = pygame.image.load('assets/background-day.png').convert()

# floor surface
floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_position = 0

# bird images and surface
bird_downflap = pygame.image.load('assets/bluebird-downflap.png').convert()
bird_midflap = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_upflap = pygame.image.load('assets/bluebird-upflap.png').convert()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (50,height/2))

# bird userevent
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# pipe surface and pipe userevent
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 300, 350, 400]

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
				bird_movement -= 5
			
			# if user presses spacebar while the game is not active
			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (50, height/2)
				bird_movement = 0

		# custom event for spawning pipe
		if event.type == SPAWNPIPE:
			pipe_list.extend(create_pipe())

		# custom event for flapping bird wings
		if event.type == BIRDFLAP:
			if bird_index == 2:
				bird_index = 0
			else:
				bird_index += 1
			bird_surface, bird_rect = bird_animation()
					
	screen.blit(bg_surface, (0,0))

	if game_active:
		# Bird
		bird_movement += gravity
		rotated_bird = rotate_bird(bird_surface)
		bird_rect.centery += bird_movement
		screen.blit(rotated_bird, bird_rect)
		game_active = check_collision(pipe_list)

		# Pipes
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)
	else: 
		pass

	# Floor
	floor_x_position -= 0.5
	draw_floor()
	if floor_x_position <= -width:
		floor_x_position = 0
	
	# update the display with the max refresh rate being 120hz
	pygame.display.update()
	clock.tick(120)
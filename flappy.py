import pygame, sys

# draw the moving floor
def draw_floor():
	screen.blit(floor_surface, (floor_x_position,900))
	screen.blit(floor_surface, (floor_x_position + width,900))

# initialization
pygame.init()
# width = 576
# height = 1024
width = 432
height = 768

screen = pygame.display.set_mode((width, height)) #width, height

clock = pygame.time.Clock()

# background surface
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

# floor surface
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_position = 0

# game loop
while True:
	# event loop
	for event in pygame.event.get():
		# if user quits
		if event.type == pygame.QUIT:
			pygame.quit() 
			sys.exit()
					
	screen.blit(bg_surface, (0,0))

	# Floor
	floor_x_position -= 1
	draw_floor()
	if floor_x_position <= -width:
		floor_x_position = 0
	
	# update the display with the max refresh rate being 120hz
	pygame.display.update()
	clock.tick(120)
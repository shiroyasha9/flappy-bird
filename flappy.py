import pygame, sys

# initialization
pygame.init()
height = 512
width = 288
screen = pygame.display.set_mode((width, height)) #width, height
clock = pygame.time.Clock()

# game loop
while True:
	# event loop
	for event in pygame.event.get():
		# if user quits
		if event.type == pygame.QUIT:
			pygame.quit() 
			sys.exit()

	# update the display with the max refresh rate being 120hz
	pygame.display.update()
	clock.tick(120)
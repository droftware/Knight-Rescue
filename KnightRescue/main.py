import pygame
import constants
import graphics
from landforms import *



def main():
	pygame.init()

	screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
	pygame.display.set_caption('Donkey Kong')

	done = False
	clock = pygame.time.Clock()

	platform_one = FirstPlatform()
	platform_two = SecondPlatform()
	platform_three = ThirdPlatform()

	
	

	while not done:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		

		screen.fill(constants.WHITE)
		platform_one.draw(screen)
		platform_two.draw(screen)
		platform_three.draw(screen)

		clock.tick(60)

		pygame.display.flip()

	

	pygame.quit()

if __name__ == '__main__':
	main()


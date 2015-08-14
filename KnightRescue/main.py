import pygame
import constants
import graphics
import player
import donkey
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
	platform_four = FourthPlatform()

	knight = player.Player()
	knight.current_platform = platform_three
	print 'Knights current_platform' + str(knight.current_platform)

	active_sprite_list = pygame.sprite.Group()
	active_sprite_list.add(knight)

	villain = donkey.Donkey()
	villain.current_platform = platform_four
	active_sprite_list.add(villain)

	frame_count = 0

	while not done:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					knight.move_left()
				if event.key == pygame.K_d:
					knight.move_right()
				if event.key == pygame.K_w:
					knight.jump()
					print 'Jump given'


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a and knight.get_x_vector() < 0:
					knight.stop()
				if event.key == pygame.K_d and knight.get_x_vector() > 0:
					knight.stop()

		print 'Knights current_platform' + str(knight.current_platform.block_list)
		
		active_sprite_list.update()

		# Draw on the screen
		screen.fill(constants.WHITE)

		platform_one.draw(screen)
		platform_two.draw(screen)
		platform_three.draw(screen)
		platform_four.draw(screen)
		active_sprite_list.draw(screen)

		clock.tick(constants.FPS)

		pygame.display.flip()

	

	pygame.quit()

if __name__ == '__main__':
	main()


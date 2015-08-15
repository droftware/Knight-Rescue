import pygame
import constants
import graphics
import player
import donkey
import ladder
from landforms import *
import fireball



def main():
	pygame.init()

	screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
	pygame.display.set_caption('Donkey Kong')

	done = False
	clock = pygame.time.Clock()

	platform_zero = ZeroPlatform()
	platform_one = FirstPlatform()
	platform_two = SecondPlatform()
	platform_three = ThirdPlatform()
	platform_four = FourthPlatform()

	ladder_one = ladder.Ladder(200,constants.SCREEN_HEIGHT)
	ladder_two = ladder.Ladder(400,constants.SCREEN_HEIGHT)
	ladder_three = ladder.Ladder(500,constants.ONE_Y)
	ladder_four = ladder.Ladder(300,constants.TWO_Y)

	knight = player.Player()
	#knight.current_platform = platform_one

	active_sprite_list = pygame.sprite.Group()
	active_sprite_list.add(knight)

	villain = donkey.Donkey(constants.SCREEN_HEIGHT - 600, constants.FOUR_Y,200,700)
	#villain.current_platform = platform_one
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
					knight.move_up()
				if event.key == pygame.K_s:
					knight.move_down()
				if event.key == pygame.K_SPACE:
					knight.jump()
					print 'Jump given'


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a and knight.get_x_vector() < 0:
					knight.stop()
				if event.key == pygame.K_d and knight.get_x_vector() > 0:
					knight.stop()


		
		active_sprite_list.update()
		


		# Draw on the screen
		screen.fill(constants.WHITE)

		platform_zero.draw(screen)
		platform_one.draw(screen)
		platform_two.draw(screen)
		platform_three.draw(screen)
		platform_four.draw(screen)
		ladder.Ladder.draw(screen)
		fireball.Fireball.draw(screen)

		active_sprite_list.draw(screen)
		

		clock.tick(constants.FPS)

		pygame.display.flip()

	

	pygame.quit()

if __name__ == '__main__':
	main()


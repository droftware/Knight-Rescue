import pygame
import constants
import levels

def main():
	pygame.init()

	screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
	pygame.display.set_caption('Donkey Kong')


	clock = pygame.time.Clock()

	current_level = levels.LevelOne(screen)

	stop = False

	while not stop:


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				stop = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					current_level.knight.move_left()
				if event.key == pygame.K_d:
					current_level.knight.move_right()
				if event.key == pygame.K_w:
					current_level.knight.move_up()
				if event.key == pygame.K_s:
					current_level.knight.move_down()
				if event.key == pygame.K_SPACE:
					current_level.knight.jump()
					print 'Jump given'
				if event.key == pygame.K_q:
					stop = True


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a and current_level.knight.get_x_vector() < 0:
					current_level.knight.stop()
				if event.key == pygame.K_d and current_level.knight.get_x_vector() > 0:
					current_level.knight.stop()


		
		current_level.update()
		
		# Draw on the screen
		current_level.draw()

		if current_level.check_alive_player() == False:
			stop = True

		clock.tick(constants.FPS)

		pygame.display.flip()

		if stop == True:
			pygame.quit()

		elif current_level.check_level_cleared() == True:
			if type(current_level) == levels.LevelOne:
				current_level = levels.LevelTwo(screen)
				current_level.knight.score += 50

			elif type(current_level) == levels.LevelTwo:
				current_level = levels.LevelThree(screen)
				current_level.knight.score += 50






if __name__ == '__main__':
	main()


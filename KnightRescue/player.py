import pygame
import constants
import person

class Player(person.Person):

	def __init__(self):

		super(Player,self).__init__(0,0,66,92,'p2_stand.png')
		self.rect.left = 5
		self.rect.bottom = constants.SCREEN_HEIGHT

	def move_left(self):

		self.set_x_vector(-1 * constants.PLAYER_SPEED)

	def move_right(self):

		self.set_x_vector(constants.PLAYER_SPEED)

	def jump(self):

		if self.current_platform != None:
			self.rect.y -= 2
			collided_blocks = pygame.sprite.spritecollide(self,self.current_platform.block_list,False)
			self.rect.y += 2

			if len(collided_blocks) > 0:
				self.set_y_vector(-30)
				print 'Jump inside player'

		else:
			if self.rect.bottom == constants.SCREEN_HEIGHT:
				self.set_y_vector(-30)
				print 'Jump inside player from ground'


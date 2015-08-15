import pygame
import constants
import item
import ladder

class Fireball(item.Item):

	all_fireballs = pygame.sprite.Group()

	def __init__(self,left,bottom):

		super(Fireball,self).__init__(22,22,24,27,'fireball.png')
		self.rect.left = left
		self.rect.bottom = bottom
		self.direction = 'LEFT'

	def update(self):

		if self.direction == 'LEFT':
			self.set_x_vector(-1 * constants.FIREBALL_SPEED)
		else:
			self.set_x_vector(constants.FIREBALL_SPEED)

		super(Fireball,self).update()

		self.__change_direction()
		self.__check_ladder()



	def __change_direction(self):

		if self.rect.left <= 0:
			self.direction = 'RIGHT'
		elif self.rect.right >= constants.SCREEN_WIDTH:
			self.direction = 'LEFT'

	def __check_ladder(self):
		
		self.rect.top += 50
		collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ladders,False)
		self.rect.top -= 50

		if len(collided_ladders) > 0:
			self.rect.top += 100

	@staticmethod
	def draw(screen):
		Fireball.all_fireballs.draw(screen)


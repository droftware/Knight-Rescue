import pygame
import constants
import person
import landforms
import ladder

class Player(person.Person):

	def __init__(self):

		super(Player,self).__init__(0,0,50,70,'p2_stand.png')
		self.rect.left = 5
		self.rect.bottom = 280
		self.score = 0

	def update(self):

		super(Player,self).update()
		self.__check_coin()

	def move_left(self):

		self.set_x_vector(-1 * constants.PLAYER_SPEED)

	def move_right(self):

		self.set_x_vector(constants.PLAYER_SPEED)

	def move_up(self):
		collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ladders,False)
		if len(collided_ladders) > 0:
			self.set_y_vector(-20)

	def move_down(self):
		self.rect.y += 80
		collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ladders,False)
		self.rect.y -= 80

		if len(collided_ladders) > 0:
			self.rect.y = self.rect.y + 130
			print 'move down'



	def jump(self):

		
		self.rect.y += 2
		collided_blocks = pygame.sprite.spritecollide(self,landforms.Platform.all_blocks,False)
		self.rect.y -= 2

		if len(collided_blocks) > 0 or self.rect.bottom == constants.SCREEN_HEIGHT:
			self.set_y_vector(-30)
			


	def __check_coin(self):

		collided_coins = pygame.sprite.spritecollide(self,landforms.Platform.all_coins,True)
		for gold_coin in collided_coins:
			self.score += 5
import pygame
import constants
import person
import landforms
import ladder
import fireball
import sys
import donkey


class Player(person.Person):


	"""	Defines the player object.It inherits from Person class."""

	def __init__(self):

		"""Constructor for Player class."""
		super(Player,self).__init__(0,0,50,70,'p2_stand.png')
		self.rect.left = 0
		self.rect.bottom = constants.SCREEN_HEIGHT
		self.score = 0
		self.life = constants.PLAYER_LIFE
		self.__princess = None
		self.__reached_princess = False

	def update(self):

		"""
			Moves the player acording to the user and also checks if it
			has collected any coins,has been hit with a fireball or has
			reached the princess.
		"""
		super(Player,self).update()
		self.__check_coin()
		self.__check_fireball()
		self.__check_princess()
		self.__check_donkey()

	def move_left(self):

		""" Moves the player left """
		self.set_x_vector(-1 * constants.PLAYER_SPEED)

	def move_right(self):

		""" Moves the player right """
		self.set_x_vector(constants.PLAYER_SPEED)

	def move_up(self):

		""" Checks if there is a ladder and only then allowes the player to move up """
		collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ladders,False)
		if len(collided_ladders) > 0:
			self.set_y_vector(-20)

	def move_down(self):

		""" Checks if there is a ladder and only then allows the player to move down """
		self.rect.y += 80
		collided_ladders = pygame.sprite.spritecollide(self,ladder.Ladder.all_ladders,False)
		self.rect.y -= 80
		if len(collided_ladders) > 0:
			self.rect.y = self.rect.y + 130
			print 'move down'

	def jump(self):

		""" 
			Makes the player jump only after checking if the player is on the 
			ground or standing on a platform
		"""
		self.rect.y += 2
		collided_blocks = pygame.sprite.spritecollide(self,landforms.Platform.all_blocks,False)
		self.rect.y -= 2
		if len(collided_blocks) > 0 or self.rect.bottom == constants.SCREEN_HEIGHT:
			self.set_y_vector(-10)
			

	def __check_coin(self):

		"""
			Checks if there is a coin at players current position.If it is so then increment 
			the players score and make the coin disappear.
		"""
		collided_coins = pygame.sprite.spritecollide(self,landforms.Platform.all_coins,True)
		for gold_coin in collided_coins:
			self.score += 5

	def __check_fireball(self):

		"""
			Checks if the player is hit with a fireball.
		"""
		collided_fireballs = pygame.sprite.spritecollide(self,fireball.Fireball.all_fireballs,True)
		if len(collided_fireballs) > 0:
			self.life -= 1
			self.score -= 25
			self.rect.left = 0
			self.rect.bottom = constants.SCREEN_HEIGHT

	def set_princess(self,princess):

		""" Assigns princess to the player """
		self.__princess = princess

	def __check_princess(self):

		""" Checks whether the player has reached the princess or not """
		flag = pygame.sprite.collide_rect(self,self.__princess)
		if flag == True:
			self.__check_princess = True

	def check_reached_princess(self):

		""" Returns true if the player has reached the princess """
		return self.__check_princess

	def __check_donkey(self):

			collided_donkeys = pygame.sprite.spritecollide(self,donkey.Donkey.all_donkeys,False)
			if len(collided_donkeys) > 0:
				print 'Collided with donkey'
				self.life -= 1
				self.score -= 25
				self.rect.left = 0
				self.rect.bottom = constants.SCREEN_HEIGHT



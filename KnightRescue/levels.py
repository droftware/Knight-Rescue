import pygame
import constants
import donkey
import board

class LevelOne(board.Board):

	def __init__(self,screen):

		super(LevelOne,self).__init__(screen)
		self.villain_one = None
		self._set_villain()

	def _set_villain(self):

		self.villain_one = donkey.Donkey(100 , constants.THREE_Y,0,500)
		self.active_sprite_list.add(self.villain_one)

class LevelTwo(board.Board):

	def __init__(self,screen):

		super(LevelTwo,self).__init__(screen)
		self.villain_one =None
		self.villain_two = None
		self._set_villain()

	def _set_villain(self):

		self.villain_one = donkey.Donkey(100 , constants.THREE_Y,0,500)
		self.active_sprite_list.add(self.villain_one)

		self.villain_two = donkey.Donkey(900, constants.TWO_Y,700,950)
		self.active_sprite_list.add(self.villain_two)


class LevelThree(board.Board):

	def __init__(self,screen):

		super(LevelThree,self).__init__(screen)
		self.villain_one =None
		self.villain_two = None
		self.villain_three = None
		self._set_villain()

	def _set_villain(self):

		self.villain_one = donkey.Donkey(100 , constants.THREE_Y,0,500)
		self.active_sprite_list.add(self.villain_one)

		self.villain_two = donkey.Donkey(900, constants.TWO_Y,700,950)
		self.active_sprite_list.add(self.villain_two)

		self.villain_three = donkey.Donkey(200, constants.ONE_Y,0,300)
		self.active_sprite_list.add(self.villain_three)





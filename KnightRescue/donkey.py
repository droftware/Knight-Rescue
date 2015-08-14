import pygame
import person
import constants

class Donkey(person.Person):

	def __init__(self):

		super(Donkey,self).__init__(0,0,69,71,'p1_duck.png')
		self.rect.right = constants.SCREEN_WIDTH - 50
		self.rect.bottom = 120


	def move_left(self):

		self.set_x_vector(-1 * constants.DONKEY_SPEED)

	def move_right(self):

		self.set_x_vector(constants.DONKEY_SPEED)



	

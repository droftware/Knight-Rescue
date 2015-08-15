import pygame
import person
import constants
import random 
import fireball

class Donkey(person.Person):

	def __init__(self,left,bottom,left_boundary,right_boundary):

		super(Donkey,self).__init__(0,0,69,71,'p1_duck.png')
		self.rect.left = left
		self.rect.bottom = bottom
		self.left_boundary = left_boundary
		self.right_boundary = right_boundary
		self.move_right()
		self.steps = 0
		self.threshold_steps = random.randint(25,50)
		self.direction = 'RIGHT'
		self.__loop_count = 0


	def move_left(self):

		self.set_x_vector(-1 * constants.DONKEY_SPEED)

	def move_right(self):

		self.set_x_vector(constants.DONKEY_SPEED)

	def __random_movement(self):

		self.steps += 1
		if self.steps >= self.threshold_steps:
			if self.direction == 'RIGHT':
				self.move_left()
				self.direction = 'LEFT'
			else:
				self.move_right()
				self.direction = 'RIGHT'
			self.threshold_steps = random.randint(25,50)
			self.steps = 0

		self.__check_boundary()


	def __check_boundary(self):
		if self.rect.left <= self.left_boundary:
			self.move_right()

		if self.rect.right >= self.right_boundary:
			self.move_left()


	def update(self):

		self.__loop_count += 1

		if self.__loop_count >= 200:
			fireball.Fireball.all_fireballs.add(fireball.Fireball(self.rect.left,self.rect.bottom))
			self.__loop_count = 0


		self.__random_movement()

		super(Donkey,self).update()
	


	

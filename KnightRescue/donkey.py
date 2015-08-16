import pygame
import person
import constants
import random 
import fireball


class Donkey(person.Person):


	""" Class which defines the Donkey object """

	def __init__(self,left,bottom,left_boundary,right_boundary):

		"""
			Constructor for the Donkey object.Assigns the donkey at the
			given left,bottom position.Ensures that the donkey does motions
			whithin the specified boundary.
		"""
		super(Donkey,self).__init__(0,0,69,71,'p1_duck.png')
		self.rect.left = left
		self.rect.bottom = bottom
		self.left_boundary = left_boundary
		self.right_boundary = right_boundary
		self.move_right()
		# Variable for keeping track so as to when to change the Donkeys direction 
		self.__steps = 0		
		self.__threshold_steps = random.randint(25,50)	
		self.direction = 'RIGHT' # Current direction of Donkey
		# Variable for keeping track so to when to emit fireballs  
		self.__loop_count = 0	 

	def move_left(self):

		""" Moves the Donkey to the left """
		self.set_x_vector(-1 * constants.DONKEY_SPEED)

	def move_right(self):

		""" Moves the Donkey to the right """
		self.set_x_vector(constants.DONKEY_SPEED)

	def __random_movement(self):

		""" Responsible for random motion of the Donkey """
		self.__steps += 1   		# Increment after every frame
		# When __steps greater than threshold reverse the direction
		# and set threshold to a new random value
		if self.__steps >= self.__threshold_steps:	
			if self.direction == 'RIGHT':
				self.move_left()
				self.direction = 'LEFT'
			else:
				self.move_right()
				self.direction = 'RIGHT'
			self.__threshold_steps = random.randint(25,50)
			self.__steps = 0
		# Confines the Donkeys movement to within the boundary 
		self.__check_boundary()

	def __check_boundary(self):

		""" Confines Donkeys movement to within the boundary """
		if self.rect.left <= self.left_boundary:
			self.move_right()
		if self.rect.right >= self.right_boundary:
			self.move_left()

	def update(self):

		""" Updates Donkey's motion and determines whether to emit fireball or not """
		self.__loop_count += 1
		if self.__loop_count >= 100:
			fireball.Fireball.all_fireballs.add(fireball.Fireball(self.rect.left,self.rect.bottom))
			self.__loop_count = 0
		self.__random_movement()
		super(Donkey,self).update()
	


	

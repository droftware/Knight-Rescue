import pygame
import constants
import graphics
import landforms

class Person(pygame.sprite.Sprite):

	def __init__(self,x,y,width,height,image_path):

		super(Person,self).__init__()

		self.graphic_obj = graphics.Graphics(image_path)
		self.image = self.graphic_obj.extract_graphic(x,y,width,height)
		self.rect = self.image.get_rect()

		self.__x_vector = 0
		self.__y_vector = 0
		self.current_platform = None

	def update(self):

		#print 'Self rect bottom in update' + str(self.rect.bottom)
		#Updating the x coordinates

		#Add effect of gravity on person
		self.__gravity_effect()
		#Move the person left/right 
		self.rect.x += self.__x_vector

		#Updating the y coordinates

		#Moves the person top/bottom 
		self.rect.y += self.__y_vector

		#Maintains persons position on the current platform 
		if self.current_platform != None:
			self.__check_platform()

		#Maintains that the player does not leave the board width
		self.__check_board()


	def __gravity_effect(self):

		self.__y_vector += constants.GRAVITY

		#Checks and maintains the person on ground
		self.__check_ground()


	def __check_board(self):

		if self.rect.left <= 0:
			self.rect.left = 0
		elif self.rect.right >= constants.SCREEN_WIDTH:
			self.rect.right = constants.SCREEN_WIDTH
	

	def __check_ground(self):

		#Maintains the person on the ground
		if self.rect.bottom > constants.SCREEN_HEIGHT:
			self.rect.bottom = constants.SCREEN_HEIGHT
			self.__y_vector = 0

	def __check_platform(self):

		
		collided_blocks = pygame.sprite.spritecollide(self,self.current_platform.block_list,False)
		for block in collided_blocks:
			
			if self.__y_vector > 0:
				self.rect.bottom = block.rect.top
				#print 'self rect bottom in check platform' + str(self.rect.bottom)
			self.__y_vector = 0
			
	def set_x_vector(self,x):
		self.__x_vector = x

	def set_y_vector(self,y):
		self.__y_vector = y

	def get_x_vector(self):
		return self.__x_vector

	def get_y_vector(self):
		return self.__y_vector

	def move_left(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def move_right(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def stop(self):
		
		self.__x_vector = 0
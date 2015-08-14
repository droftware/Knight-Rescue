"""
	Module whch contains the lanforms such as blocks and platforms for the game
"""

import pygame
import constants
import graphics


class Block(pygame.sprite.Sprite):
	"""
		Atomic unit for forming the platform.
	"""

	def __init__(self):

		super(Block,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(506,506,68,40)
		self.rect = self.image.get_rect()

	def set_x(self,x):
		self.rect.x = x

	def set_y(self,y):
		self.rect.y = y


class Platform(pygame.sprite.Sprite):

	def __init__(self):

		super(Platform,self).__init__()
		self._block_list = pygame.sprite.Group()

	def update(self):

		self._block_list.update()

	def draw(self,screen):

		self._block_list.draw(screen)


class FirstPlatform(Platform):
	
	def __init__(self):

		super(FirstPlatform,self).__init__()

		for i in range(0,600,68):

			block = Block()
			block.set_x(i)
			block.set_y(550)

			self._block_list.add(block)

class SecondPlatform(Platform):

	def __init__(self):

		super(SecondPlatform,self).__init__()

		for i in range(400,900,68):

			block = Block()
			block.set_x(i)
			block.set_y(420)

			self._block_list.add(block)

class ThirdPlatform(Platform):

	def __init__(self):

		super(ThirdPlatform,self).__init__()

		for i in range(0,700,68):

			block = Block()
			block.set_x(i)
			block.set_y(280)

			self._block_list.add(block)

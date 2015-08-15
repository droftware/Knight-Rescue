"""
	Module whch contains the lanforms such as blocks and platforms for the game
"""

import pygame
import constants
import graphics
import coin
import random


class Block(pygame.sprite.Sprite):
	"""
		Atomic unit for forming the platform.
	"""

	def __init__(self):

		super(Block,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(506,506,68,25)
		self.rect = self.image.get_rect()

	def set_x(self,x):
		self.rect.x = x

	def set_y(self,y):
		self.rect.y = y


class Platform(object):

	all_blocks = pygame.sprite.Group()
	all_coins = pygame.sprite.Group()

	def __init__(self):

		super(Platform,self).__init__()
		self.block_list = pygame.sprite.Group()
		self.coins_list = pygame.sprite.Group()

	def update(self):

		self.block_list.update()
		self.coins_list.update()

	def draw(self,screen):

		self.block_list.draw(screen)
		self.coins_list.draw(screen)


class ZeroPlatform(Platform):
	
	def __init__(self):

		super(ZeroPlatform,self).__init__()

		for i in range(0,constants.SCREEN_WIDTH,68):

			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.SCREEN_HEIGHT
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)	


class FirstPlatform(Platform):
	
	def __init__(self):

		super(FirstPlatform,self).__init__()

		for i in range(constants.ONE_X1,constants.ONE_X2,68):

			block = Block()
			block.set_x(i)
			block.set_y(constants.ONE_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)

			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.ONE_Y
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)



class SecondPlatform(Platform):

	def __init__(self):

		super(SecondPlatform,self).__init__()

		for i in range(constants.TWO_X1,constants.TWO_X2,68):

			block = Block()
			block.set_x(i)
			block.set_y(constants.TWO_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)

			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.TWO_Y
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)

class ThirdPlatform(Platform):

	def __init__(self):

		super(ThirdPlatform,self).__init__()

		for i in range(constants.THREE_X1,constants.THREE_X2,68):

			block = Block()
			block.set_x(i)
			block.set_y(constants.THREE_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)

			random_num = random.randint(0,100)
			if random_num % 2 == 0:
				gold_coin = coin.Coin()
				gold_coin.rect.left = i + 5
				gold_coin.rect.bottom = constants.THREE_Y
				self.coins_list.add(gold_coin)
				Platform.all_coins.add(gold_coin)



class FourthPlatform(Platform):

	def __init__(self):

		super(FourthPlatform,self).__init__()

		for i in range(constants.FOUR_X1,constants.FOUR_X2,68):

			block = Block()
			block.set_x(i)
			block.set_y(constants.FOUR_Y)
			self.block_list.add(block)
			Platform.all_blocks.add(block)



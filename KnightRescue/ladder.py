import pygame
import graphics
import constants


class LadderBlock(pygame.sprite.Sprite):


	""" Class which defines the individual ladder block """

	def __init__(self):

		"""Constructor for LadderBlock class """
		super(LadderBlock,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(502,71,73,74)
		self.rect = self.image.get_rect()


class BrokenLadderBlock(pygame.sprite.Sprite):


	""" Class which defines the individual broken ladder block """

	def __init__(self):

		"""Constructor for BrokenLadderBlock class """
		super(BrokenLadderBlock,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(647,80,73,64)
		self.rect = self.image.get_rect()


class Ladder(object):


	""" Class which defines the Ladder object """

	all_ladders = pygame.sprite.Group()	# Class variable which stores every ladder block object 

	def __init__(self,left,bottom):

		""" Constructor for Ladder class """
		super(Ladder,self).__init__()
		self.block_one = LadderBlock()		# Initializes one ladder block object 
		self.block_one.rect.left = left
		self.block_one.rect.bottom = bottom + 5
		Ladder.all_ladders.add(self.block_one)	# Adds the ladder block in all_ladders group
		self.block_two = LadderBlock()		# Initialize another block object
		self.block_two.rect.left = left
		self.block_two.rect.bottom = self.block_one.rect.top + 20	
		Ladder.all_ladders.add(self.block_two)	# Adds the second ladder block in all_ladders
												# block as well
															
	def update():

		"""Updates all the Ladder blocks """
		Ladder.all_ladders.update()

	@staticmethod
	def draw(screen):

		""" Draws all the ladder block """
		Ladder.all_ladders.draw(screen)


class BrokenLadder(object):


	""" Class which defines the individual broken ladder block """

	all_broken_ladders = pygame.sprite.Group() # Class variable which stores every broken ladder block

	def __init__(self,left,bottom):

		""" Constructor for BrokenLadder object """
		super(BrokenLadder,self).__init__()
		self.block_one = LadderBlock()
		self.block_one.rect.left = left
		self.block_one.rect.bottom = bottom + 5
		BrokenLadder.all_broken_ladders.add(self.block_one)
		self.block_two = BrokenLadderBlock()
		self.block_two.rect.left = left
		self.block_two.rect.bottom = self.block_one.rect.top + 20
		BrokenLadder.all_broken_ladders.add(self.block_two)
		
	def update():

		""" Updates all the broken ladder blocks """
		BrokenLadder.all_broken_ladders.update()

	@staticmethod
	def draw(screen):

		""" Draws all the broken ladder blocks on the screen """
		BrokenLadder.all_broken_ladders.draw(screen)



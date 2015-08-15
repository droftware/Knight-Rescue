import pygame
import graphics
import constants


class LadderBlock(pygame.sprite.Sprite):

	def __init__(self):

		super(LadderBlock,self).__init__()
		self.graphic_obj = graphics.Graphics('blocks.png')
		self.image = self.graphic_obj.extract_graphic(502,71,73,74)
		self.rect = self.image.get_rect()


class Ladder(object):

	all_ladders = pygame.sprite.Group()

	def __init__(self,left,bottom):
		super(Ladder,self).__init__()

		self.block_one = LadderBlock()
		self.block_one.rect.left = left
		self.block_one.rect.bottom = bottom + 5
		Ladder.all_ladders.add(self.block_one)

		self.block_two = LadderBlock()
		self.block_two.rect.left = left
		self.block_two.rect.bottom = self.block_one.rect.top + 20
		Ladder.all_ladders.add(self.block_two)
		

	def update():
		Ladder.all_ladders.update()

	@staticmethod
	def draw(screen):
		Ladder.all_ladders.draw(screen)


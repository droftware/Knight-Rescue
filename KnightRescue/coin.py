import pygame
import graphics
import constants


class Coin(pygame.sprite.Sprite):

	def __init__(self):

		super(Coin,self).__init__()
		self.graphic_obj = graphics.Graphics('coinGold.png')
		self.image = self.graphic_obj.extract_graphic(0,0,70,70)
		self.rect = self.image.get_rect()


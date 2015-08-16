import pygame
import player
import constants

class ScoreBoard(object):

	def __init__(self,protagnist):

		self.protagnist = protagnist
		self.font = pygame.font.Font('freesansbold.ttf',35)
		self.score_line = 'Score : ' + str(self.protagnist.score) + ' Life : ' + str(self.protagnist.life)
		self.text = self.font.render(self.score_line,True,constants.BLACK)

	def update(self):

		self.score_line = 'Score : ' + str(self.protagnist.score) + ' Life : ' + str(self.protagnist.life)
		self.text = self.font.render(self.score_line,True,constants.BLACK)
		
	def draw(self,screen):

		screen.blit(self.text,(0,0))
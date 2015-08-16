import pygame
import constants
import player
import donkey
import princess
import ladder
import landforms
import scoreboard
import fireball

class Board(object):

	def __init__(self,screen):

		self.active_sprite_list = pygame.sprite.Group()

		self.screen = screen
		self.platform_zero = landforms.ZeroPlatform()
		self.platform_one = landforms.FirstPlatform()
		self.platform_two = landforms.SecondPlatform()
		self.platform_three = landforms.ThirdPlatform()
		self.platform_four = landforms.FourthPlatform()

		self.broken_ladder_one = ladder.BrokenLadder(200,constants.SCREEN_HEIGHT)

		self.ladder_two = ladder.Ladder(400,constants.SCREEN_HEIGHT)
		self.ladder_three = ladder.Ladder(300,constants.ONE_Y)
		self.ladder_four = ladder.Ladder(550,constants.TWO_Y)
		self.ladder_five = ladder.Ladder(450,constants.THREE_Y)

		self.knight = player.Player()
		self.lady = princess.Princess(constants.SCREEN_HEIGHT - 100,constants.FOUR_Y)

		self.knight.set_princess(self.lady)
		self.active_sprite_list.add(self.knight)
		self.active_sprite_list.add(self.lady)

		self.score_board = scoreboard.ScoreBoard(self.knight)

	def update(self):

		self.active_sprite_list.update()
		fireball.Fireball.all_fireballs.update()
		self.score_board.update()

	def draw(self):

		self.screen.fill(constants.WHITE)

		self.platform_zero.draw(self.screen)
		self.platform_one.draw(self.screen)
		self.platform_two.draw(self.screen)
		self.platform_three.draw(self.screen)
		self.platform_four.draw(self.screen)

		ladder.Ladder.draw(self.screen)
		ladder.BrokenLadder.draw(self.screen)

		fireball.Fireball.draw(self.screen)

		self.active_sprite_list.draw(self.screen)

		self.score_board.draw(self.screen)


	def _set_villain(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def check_alive_player(self):
		if self.knight.life == -1:
			return False
		else:
			return True

	def check_level_cleared(self):
		if self.knight.check_reached_princess() == True:
			return True
		else:
			return False





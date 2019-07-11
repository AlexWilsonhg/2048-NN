from .iGame import iGame
import random

class Mock2048(iGame):

	def IsGameOver(self):
		return True

	def GetScore(self):
		return random.randrange(400,3500)

	def GetTiles(self):
		return [0] * 16

	def NewGame(self):
		pass

	def DoMove(self, moves):
		pass

	def Close(self):
		pass
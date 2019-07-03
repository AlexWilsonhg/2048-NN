from .iGame import iGame

class Mock2048(iGame):

	def GameOver(self):
		return True

	def GetScore(self):
		return 500

	def GetTiles(self):
		return [0] * 16

	def NewGame(self):
		pass

	def DoMove(self, moves):
		pass

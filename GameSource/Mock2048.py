from .iGame import iGame
import random

class Tile:
	def __init__(self):
		self.value = 0
		self.hasCombined = False

class Mock2048(iGame):

	def __init__(self):
		self.score = 0
		self.gameOver = False
		self.tiles = [[Tile() for j in range(4)] for i in range(4)]
		self.ResetTiles()
		self.cachedTiles = self.GetTiles()
		self.actionMappings = [
								self.MoveDown,
								self.MoveRight,
								self.MoveUp,
								self.MoveLeft]

	def IsGameOver(self):
		return self.gameOver

	def GetScore(self):
		return self.score

	def GetTiles(self):
		unpackedTiles = []
		for row in range(4):
			for col in range(4):
				unpackedTiles.append(self.tiles[row][col].value)
		return unpackedTiles

	def NewGame(self):
		self.score = 0
		self.gameOver = False
		self.ResetTiles()

	def DoMove(self, moves):
   		for i in range(len(moves)):
   			index = moves.index(max(moves))
   			moves[index] = 0
	   		self.actionMappings[index]()
   			if(self.HasChanged()):
   				break

	def Close(self):
		pass

	def MoveDown(self):
		boardHasChanged = False
		for row in range(2, -1, -1):
			for col in range(4):
				if(self.tiles[row][col].value == 0):
					pass
				else:
					cachedTile = self.tiles[row][col]
					for nextTile in range(row, 3):
						tile = self.tiles[nextTile+1][col]
						if(tile.value == 0):
							tile.value = cachedTile.value
							cachedTile.value = 0
							cachedTile = self.tiles[nextTile+1][col]
							boardHasChanged = True
						elif(tile.value == cachedTile.value) and (tile.hasCombined == False):
							tile.value *= 2
							tile.hasCombined = True
							cachedTile.value = 0
							self.score += tile.value
							boardHasChanged = True
						else:
							pass

		if(boardHasChanged):
			self.SpawnNewTile()
			if not self.HasValidMove():
				self.gameOver = True

	def MoveUp(self):
		boardHasChanged = False
		for row in range(1, 4):
			for col in range(4):
				if(self.tiles[row][col].value == 0):
					pass
				else:
					cachedTile = self.tiles[row][col]
					for nextTile in range(row, 0, -1):
						tile = self.tiles[nextTile-1][col]
						if(tile.value == 0):
							tile.value = cachedTile.value
							cachedTile.value = 0
							cachedTile = self.tiles[nextTile-1][col]
							boardHasChanged = True
						elif(tile.value == cachedTile.value) and (tile.hasCombined == False):
							tile.value *= 2
							tile.hasCombined = True
							cachedTile.value = 0
							self.score += tile.value
							boardHasChanged = True
						else:
							break

		if(boardHasChanged):
			self.SpawnNewTile()
			if not self.HasValidMove():
				self.gameOver = True
				
	def MoveLeft(self):
		boardHasChanged = False
		for row in range(4):
			for col in range(1, 4):
				if(self.tiles[row][col].value == 0):
					pass
				else:
					cachedTile = self.tiles[row][col]
					for nextTile in range(col, 0, -1):
						tile = self.tiles[row][nextTile-1]
						if(tile.value == 0):
							tile.value = cachedTile.value
							cachedTile.value = 0
							cachedTile = self.tiles[row][nextTile-1]
							boardHasChanged = True
						elif(tile.value == cachedTile.value) and (tile.hasCombined == False):
							tile.value *= 2
							tile.hasCombined = True
							cachedTile.value = 0
							self.score += tile.value
							boardHasChanged = True
						else:
							pass

		if(boardHasChanged):
			self.SpawnNewTile()
			if not self.HasValidMove():
				self.gameOver = True

	def MoveRight(self):
		boardHasChanged = False
		for row in range(4):
			for col in range(2, -1, -1):
				if(self.tiles[row][col].value == 0):
					pass
				else:
					cachedTile = self.tiles[row][col]
					for nextTile in range(col,3):
						tile = self.tiles[row][nextTile+1]
						if(tile.value == 0):
							tile.value = cachedTile.value
							cachedTile.value = 0
							cachedTile = self.tiles[row][nextTile+1]
							boardHasChanged = True
						elif(tile.value == cachedTile.value) and (tile.hasCombined == False):
							tile.value *= 2
							tile.hasCombined = True
							cachedTile.value = 0
							self.score += tile.value
							boardHasChanged = True
						else:
							pass

		if(boardHasChanged):
			self.SpawnNewTile()
			if not self.HasValidMove():
				self.gameOver = True
		

	def SpawnNewTile(self):
		# get empty tiles
		freeTiles = []
		for row in range(4):
			for col in range(4):
				self.tiles[row][col].hasCombined = False
				if self.tiles[row][col].value == 0:
					freeTiles.append(self.tiles[row][col])

		# randomly select one free tile, set value to 2 or 4
		if(freeTiles):
			value = random.choice([2,4])
			random.choice(freeTiles).value = value

	def HasValidMove(self):
		# iterate each tile, check adjacent tiles for same value or empty spot.
		# If there is one, return True. If we get to the end, return false.
		for row in range(4):
			for col in range(4):
				# check above tile
				if(row == 0):
					pass
				else:
					aboveTile = self.tiles[row-1][col].value
					if(self.tiles[row][col].value == aboveTile) or not aboveTile:
						return True

				# check below tile
				if(row == 3):
					pass
				else:
					belowTile = self.tiles[row+1][col].value
					if(self.tiles[row][col].value == belowTile) or not belowTile:
						return True

				# check right tile
				if(col == 3):
					pass
				else:
					rightTile = self.tiles[row][col+1].value
					if(self.tiles[row][col].value == rightTile) or not rightTile:
						return True

				# check left tile
				if(col == 0):
					pass
				else:
					leftTile = self.tiles[row][col-1].value
					if(self.tiles[row][col].value == leftTile) or not leftTile:
						return True

		# we reached the end and found no valid moves				
		return False

	def ResetTiles(self):
		for row in range(4):
			for col in range(4):
				self.tiles[row][col].value = 0

		for i in range(2):
			self.SpawnNewTile()

	def PrintTiles(self):
		for row in range(4):
			string = ""
			for col in range(4):
				string += str(self.tiles[row][col].value)
			print(string)

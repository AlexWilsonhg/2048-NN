class GAME_OVER:
	def __init__(self, score, generation):
		self.score = score
		self.generation = generation

class NEW_SIMULATION:
        def __init__(self, gameSource, numPlayers, generations, gamesPerGeneration):
                self.gameSource = gameSource
                self.numPlayers = numPlayers
                self.generations = generations
                self.gamesPerGeneration = gamesPerGeneration

class PLAY_SIMULATION:
	def __init__(self):
		pass

class PAUSE_SIMULATION:
	def __init__(self):
		pass

class CLOSE_SIMULATION:
	def __init__(self):
		pass
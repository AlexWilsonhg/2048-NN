class GAME_OVER:
	def __init__(self, score, generation):
		self.score = score
		self.generation = generation

class NEW_SIMULATION:
        def __init__(self, gameSource, numPlayer, generations, gamesPerGeneration):
                self.gameSource = gameSource
                self.numPlayer = numPlayer
                self.generations = generations
                self.gamesPerGeneration = gamesPerGeneration

class PLAY_SIM:
	def __init__(self):
		pass

class PAUSE_SIM:
	def __init__(self):
		pass
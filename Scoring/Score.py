import numpy as np

class ScoreContainer:
	def __init__(self):
		self.scores = []

	def AddScore(self, score):
		self.scores.append(score)

	def GetAverageScore(self):
		if(self.scores):
			return np.mean(self.scores)
		else:
			return 0

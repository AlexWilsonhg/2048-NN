from Scoring.Score import ScoreContainer

class ScoreLog:
	def __init__(self):
		self.scoreContainers = []
		self.currentGeneration = 0

	def AddScore(self, score):
		if(not self.scoreContainers):
			self.scoreContainers.append(ScoreContainer())
		self.scoreContainers[self.currentGeneration].AddScore(score)

	def AdvanceGeneration(self):
		self.scoreContainers.append(ScoreContainer())
		self.currentGeneration += 1

	def GetAverageScores(self):
		averageScores = []
		for i in self.scoreContainers:
			averageScores.append(i.GetAverageScore())
		return averageScores

	def Reset(self):
		self.currentGeneration = 0
		self.scoreContainers.clear()

	def GetCurrentGenerationAverage(self):
		average = 0
		if(self.scoreContainers):
			average = self.scoreContainers[len(self.scoreContainers)-1].GetAverageScore()
		return average
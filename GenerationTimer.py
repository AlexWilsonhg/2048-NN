from Simulator import Simulator

class GenerationTimer:

	def __init__(self, updateFrequency = 10):
		self.timeRemaining = 0
		self.updateFrequency = updateFrequency
		self.timeSinceLastUpdate = 0
		self.oldEstimate = 0

	def Update(self, simulator, deltaTime):
		self.timeSinceLastUpdate += deltaTime
		self.timeRemaining -= deltaTime

		if(self.timeRemaining <= 0):
			self.timeRemaining = 0

		if(self.timeSinceLastUpdate > self.updateFrequency):
			newEstimate = simulator.EstimateGenerationEnd()
			self.timeRemaining = newEstimate
			self.GetTimeRemaining()
			self.timeSinceLastUpdate = 0

	def GetTimeRemaining(self):
		return self.timeRemaining
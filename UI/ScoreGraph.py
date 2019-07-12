from UI.Graph import Graph

class ScoreGraph:

	def __init__(self, master, width, height):
		self.graph = Graph(master, width, height)
		self.graph.SetYMax(3000)
		self.generation = 0

	def Update(self):
		self.graph.Draw()

	def Reset(self):
		self.graph.Reset()
		self.generation = 0

	def SetBarValue(self, value):
		self.graph.AddBar()
		self.graph.SetBarValue(self.generation, value)

	def AdvanceGeneration(self):
		self.generation += 1
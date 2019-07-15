from tkinter import *

class GenerationCounter:

	def __init__(self, master):
		self.currentGeneration = 1

		self.GenerationCounterText = Label(master, text = "Generation: ", fg = "black")
		self.GenerationCounterText.place(relheight = 1)

		self.GenerationCounterValue = Label(master, text = "", fg = "black")
		self.GenerationCounterValue.place(relheight = 1, relx = 0.45)
		
	def AdvanceGeneration(self):
		self.currentGeneration += 1

	def Update(self):
		self.GenerationCounterValue.config(text = str(self.currentGeneration))

	def Reset(self):
		self.currentGeneration = 1

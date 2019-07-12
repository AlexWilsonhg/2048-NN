from tkinter import *

class GenerationCounter:

	def __init__(self, master):
		self.currentGeneration = 1
		self.GenerationCounterFrame = Frame(master)
		self.GenerationCounterFrame.place(relheight = 0.1, relwidth = 0.1, relx = 0.45)
		self.GenerationCounterLabel = Label(self.GenerationCounterFrame, text = "", fg = "black")
		self.GenerationCounterLabel.place(relwidth = 1, relheight = 1)
		
	def AdvanceGeneration(self):
		self.currentGeneration += 1

	def Update(self):
		self.GenerationCounterLabel.config(text = "Generation: " + str(self.currentGeneration))

from tkinter import *

class GenerationAverageScore:

	def __init__(self, master):

		self.GenerationAverageScoreText = Label(master, text = "Generation Average: ", fg = "Black")
		self.GenerationAverageScoreText.place(relheight = 1)

		self.GenerationAverageScoreValue = Label(master, text = "", fg = "black")
		self.GenerationAverageScoreValue.place(relheight = 1, relx = 0.75)


	def Update(self, averageScore):
		self.GenerationAverageScoreValue.config(text = str(averageScore))


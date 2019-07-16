from tkinter import *
from tkinter import ttk

from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048

GameSource = {
	"Web 2048" 		: Web2048,
	"Desktop 2048" 	: Desktop2048,
	"Mock 2048" 	: Mock2048
	}

class NewSimDialog():

	def __init__(self, parent):
		self.parent = parent
		self.window = Toplevel(parent.window)
		self.window.wm_title("New Simulation")
		self.window.geometry("300x300")
		self.window.resizable(False, False)
		self.window.grab_set()

		self.CreateButton = ttk.Button(self.window, text = "Create", command = self.Create)
		self.CreateButton.place(relx = 0.40, rely = 0.9)

		self.CancelButton = ttk.Button(self.window, text = "Cancel", command = self.Cancel)
		self.CancelButton.place(relx = 0.70, rely = 0.9)

		self.GameSourceLabel = Label(self.window, text = "Game Source:", fg = "black")
		self.GameSourceLabel.place(relx = 0.05, rely = 0.1)

		self.GameSourceVar = StringVar(self.window)
		self.GameSourceVar.set("Web 2048")
		self.GameSourceEntryBox = OptionMenu(self.window, self.GameSourceVar, "Web 2048", "Desktop 2048", "Mock 2048")
		self.GameSourceEntryBox.place(relx = 0.50, rely = 0.075)

		self.NumberOfGameplayersLabel = Label(self.window, text = "Number of Players:", fg = "black")
		self.NumberOfGameplayersLabel.place(relx = 0.05, rely = 0.2)

		self.NumberOfGameplayersSelection = Spinbox(self.window, from_ = 2, to = 10)
		self.NumberOfGameplayersSelection.place(relx = 0.5, rely = 0.2)

		self.NumberOfGenerationsLabel = Label(self.window, text = "Number of Generations:", fg = "black")
		self.NumberOfGenerationsLabel.place(relx = 0.05, rely = 0.3)

		self.NumberOfGenerationsSelection = Spinbox(self.window, from_ = 1, to = 1000)
		self.NumberOfGenerationsSelection.place(relx = 0.5, rely = 0.3)

		self.GamesPerGenerationLabel = Label(self.window, text = "Games Per Generation:", fg = "black")
		self.GamesPerGenerationLabel.place(relx = 0.05, rely = 0.4)

		self.GamesPerGenerationSelection = Spinbox(self.window, from_ = 2, to = 10)
		self.GamesPerGenerationSelection.place(relx = 0.5, rely = 0.4)

	def Cancel(self):
		self.window.destroy()

	def Create(self):
		source = GameSource[self.GameSourceVar.get()]
		numPlayers = int(self.NumberOfGameplayersSelection.get())
		numGenerations = int(self.NumberOfGenerationsSelection.get())
		gamesPerGeneration = int(self.GamesPerGenerationSelection.get())

		self.parent.NewSim(source, numPlayers, numGenerations, gamesPerGeneration)
		self.window.destroy()

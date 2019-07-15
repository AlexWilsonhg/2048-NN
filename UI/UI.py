from tkinter import *
from tkinter import ttk

from Messaging.BusNode import BusNode
from Messaging.Events import *

from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048

from UI.ScoreGraph import ScoreGraph
from UI.GenerationCounter import GenerationCounter

class UI(BusNode):

	def __init__(self, eventBus):
		super().__init__(eventBus)

		## Main Window
		self.window = Tk()
		self.window.title('2048 Neural Evolution')
		self.window.geometry('800x500')
		self.window.resizable(False, False)
		self.window.protocol("WM_DELETE_WINDOW", self.Shutdown)

		## Menu bar
		self.NewSimButton = ttk.Button(self.window, text = "New Sim", command = self.NewSim)
		self.NewSimButton.place(relx = 0.025, rely = 0.025)

		# Toolbar
		self.PlayPauseFrame = Frame(self.window)
		self.PlayPauseFrame.place(relheight = 0.05, relwidth = 0.2, relx = 0.25, rely = 0.025, anchor = N)

		self.PlayButton = ttk.Button(self.PlayPauseFrame, text = "Play", command = self.PlaySim)
		self.PlayButton.place(relheight = 1, relwidth = 0.40, relx = 0.05)

		self.PauseButton = ttk.Button(self.PlayPauseFrame, text = "Pause", command = self.PauseSim)
		self.PauseButton.place(relheight = 1, relwidth = 0.40, relx = 0.55)

		## Sim Score Graph
		self.ScoreGraphFrame = Frame(self.window, bd = 1, relief = "sunken")
		self.ScoreGraphFrame.place(relheight = 0.85, relwidth = 0.95, relx = 0.025, rely = 0.10, anchor = NW)
		self.ScoreGraph = ScoreGraph(self.ScoreGraphFrame, 400, 400)

		## Generation Counter
		self.GenerationCounterFrame = Frame(self.window)
		self.GenerationCounterFrame.place(relheight = 0.05, relwidth = 0.2, relx = 0.40, rely = 0.025)
		self.GenerationCounter = GenerationCounter(self.GenerationCounterFrame)

		## Current generation average score
		self.CurrentGenerationScoreFrame = Frame(self.window)

	def Update(self):
		self.ScoreGraph.Update()
		self.GenerationCounter.Update()
		self.window.update()

	def OnEvent(self, event):
		if(type(event) == NEW_GENERATION):
			self.ScoreGraph.AdvanceGeneration()
			self.GenerationCounter.AdvanceGeneration()

		if(type(event) == GAME_OVER):
			self.ScoreGraph.SetBarValue(event.score)

	def PauseSim(self):
		super().SendEvent(PAUSE_SIMULATION())

	def PlaySim(self):
		super().SendEvent(PLAY_SIMULATION())

	def NewSim(self):
		super().SendEvent(NEW_SIMULATION(Mock2048, 2, 1000, 1))
		self.ScoreGraph.Reset()

	def CloseSim(self):
		super().SendEvent(CLOSE_SIMULATION())
		self.ScoreGraph.Reset()

	def Shutdown(self):
		super().SendEvent(SHUTDOWN())
		self.window.destroy()
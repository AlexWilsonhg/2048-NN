from Messaging.BusNode import BusNode
from Messaging.Events import *
from tkinter import *

from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048

class UI(BusNode):

	def __init__(self, eventBus):
		super().__init__(eventBus)

		## Main Window
		self.window = Tk()
		self.window.title('2048 Neural Evolution')
		self.window.geometry('1200x800')
		self.window.minsize(width = 800, height = 500)

		## Menu bar
		self.menu = Menu(self.window)
		self.window.config(menu = self.menu)

		## File sub-menu
		self.fileMenu = Menu(self.menu)
		self.menu.add_cascade(label="File", menu = self.fileMenu)
		self.fileMenu.add_command(label="New Sim", command = self.NewSim)
		self.fileMenu.add_command(label="Close Sim", command = self.CloseSim)

			## Save / Load Sim ( MAYBE )

		# Toolbar
		self.PlayPauseFrame = Frame(self.window, bg = 'gray')
		self.PlayPauseFrame.place(relheight = 0.05, relwidth = 0.1,relx = 0.5, anchor = N)

		self.PlayButton = Button(self.PlayPauseFrame, bg = 'green', bd = 1, command = self.PlaySim)
		self.PlayButton.place(relheight = 0.95, relwidth = 0.40, relx = 0.05)

		self.PauseButton = Button(self.PlayPauseFrame, bg = 'red', bd = 1, command = self.PauseSim)
		self.PauseButton.place(relheight = 0.95, relwidth = 0.40, relx = 0.55)

		## Sim Score Graph

	def Update(self):
		self.window.update()

	def OnEvent(self, event):
		pass

	def PauseSim(self):
		super().SendEvent(PAUSE_SIMULATION())

	def PlaySim(self):
		super().SendEvent(PLAY_SIMULATION())

	def NewSim(self):
		super().SendEvent(NEW_SIMULATION(Web2048, 2, 2, 2))

	def CloseSim(self):
		super().SendEvent(CLOSE_SIMULATION())
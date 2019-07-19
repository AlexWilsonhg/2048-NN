from tkinter import *

class SimLoadedPopup:

	def __init__(self, master, message):
		self.popup = Frame(master)
		self.popup.place(relwidth = 0.25, relheight = 0.05, relx = 0.35, rely = 0.15)
		self.label = Label(self.popup, text = message, fg = "black", relief = "raised")
		self.label.place(relheight = 1, relwidth = 1)
		self.popup.after(2000, lambda: self.popup.destroy())
from tkinter import *

class Graph:

	def __init__(self, master, width, height):
		self.canvas = Canvas(master, width = width, height = height)
		self.canvas.place()
		self.values = []
		self.currentActiveXValue = 0

	def draw(self):
		pass

	def AddValue(self, value):
		self.values[self.currentActiveXValue].append(value)
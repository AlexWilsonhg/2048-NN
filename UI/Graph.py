from tkinter import *
import numpy as np

class Graph:

	def __init__(self, master, width, height):
		self.canvas = Canvas(master, width = width, height = height)
		self.canvas.place(relwidth = 0.99, relheight = 0.99, relx = 0.005, rely = 0.005)
		self.BarPadding = 2
		self.BarWidth = width/50
		self.width = width
		self.height = height
		self.yMax = 0
		self.yMin = 0

	def Draw(self):
		self.canvas.delete("all")
		self.ReScale()
		for i in range(len(self.bars)):
			self.DrawBar(self.bars[i], i)

	def DrawBar(self, bar, position):
		if(bar > 0):
			self.canvas.create_rectangle(position * self.BarWidth +self.BarPadding, self.height - (self.height * (bar/self.yMax)), self.BarWidth + (position * self.BarWidth), 420, fill = "green")

	def ReScale(self):
		self.BarWidth = (self.width + 500) / len(self.bars)

	def SetYMax(self, value):
		self.yMax = value

	def SetYMin(self, value):
		self.yMin = value
from tkinter import *
import numpy as np

class Graph:

	def __init__(self, master, width, height):
		self.canvas = Canvas(master, width = width, height = height)
		self.canvas.place(relwidth = 0.99, relheight = 0.99, relx = 0.005, rely = 0.005)
		self.bars = [0]
		self.BarPadding = 2
		self.BarWidth = width
		self.width = width
		self.height = height
		self.yMax = 3000

	def Draw(self):
		self.canvas.delete("all")
		self.ReScale()
		for i in range(len(self.bars)):
			self.DrawBar(self.bars[i], i)

	def AddBar(self):
		self.bars.append(0)

	def SetBarValue(self, xValue, yValue):
		if(len(self.bars) == 0):
			self.AddBar()
		if(yValue > self.yMax):
			yMax = yValue
		self.bars[xValue] = (self.bars[xValue] + yValue) / 2

	def Reset(self):
		self.bars.clear()
		self.bars.append(0)

	def DrawBar(self, bar, position):
		if(bar > 0):
			self.canvas.create_rectangle(position * self.BarWidth +self.BarPadding, self.height - (self.height * (bar/self.yMax)), self.BarWidth + (position * self.BarWidth), 410, fill = "green")

	def ReScale(self):
		self.BarWidth = (self.width + 500) / len(self.bars)
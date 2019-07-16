from tkinter import *
import numpy as np

class ScoreGraph:

	def __init__(self, master, width, height):
		self.canvas = Canvas(master, width = width, height = height)
		self.canvas.place(relwidth = 0.99, relheight = 0.99, relx = 0.005, rely = 0.005)

		self.width = width
		self.height = height

		self.BarPadding = 2
		self.BarWidth = width/50

		self.yMax = 3000
		self.yMin = 0


	def Update(self, scores):
		if(len(scores) * self.BarWidth > self.width):
			self.ReScale(len(scores))
		self.Draw(scores)

	def Reset(self):
		self.canvas.delete("all")
		self.BarWidth = self.width/50
		self.yMax = 3000
		self.yMin = 0

	def Draw(self, bars):
		self.canvas.delete("all")
		for i in range(len(bars)):
			if(self.BarWidth > 5):
				self.DrawBar(bars[i], i)
			else:
				self.DrawLine(bars[i], i)

	def DrawBar(self, bar, position):
		if(bar > 0):
			self.canvas.create_rectangle(position * self.BarWidth +self.BarPadding, self.height - (self.height * (bar/self.yMax)), self.BarWidth + (position * self.BarWidth), 420, fill = "green")

	def DrawLine(self, line, position):
		if(line > 0):
			self.canvas.create_line(position, self.height - (self.height * (line/self.yMax)), position, 420, fill = "green")

	def ReScale(self, num):
		self.BarWidth = (self.width / num)
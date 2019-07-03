
class EventBus():

	def __init__(self):
		self.events = []
		self.listeners = []
	
	def Notify(self):
		for event in self.events:
			for listener in self.listeners:
				listener.OnEvent(event)
		self.events.clear()
		
	def AddListener(self, listener):
		self.listeners.append(listener)

	def PostEvent(self, event):
		self.events.append(event)

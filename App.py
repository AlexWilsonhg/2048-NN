from Simulator import Simulator
from Messaging.EventBus import EventBus
from UI.UI import UI

class Application():

	def __init__(self):
		self.bus = EventBus()
		self.simulator = Simulator(self.bus)
		self.ui = UI(self.bus)

	def Update(self, deltaTime):
		self.ui.Update(deltaTime)
		self.simulator.Update(deltaTime)
		self.bus.NotifyListeners()
		
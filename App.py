from Simulator import Simulator
from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048

from Messaging.EventBus import EventBus
from UI.UI import UI

class Application():

	def __init__(self):
		self.bus = EventBus()
		self.simulator = Simulator(self.bus)
		self.ui = UI(self.bus)

	def Update(self, deltaTime):
		self.simulator.Update(deltaTime)
		self.bus.NotifyListeners()
		self.ui.Update()

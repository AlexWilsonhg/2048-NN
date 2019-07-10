from Messaging.BusNode import BusNode
from Messaging.Events import *

class Application(BusNode):

	def __init__(self, eventBus):
		super().__init__(eventBus)


	def OnEvent(self, event):
		print("test")
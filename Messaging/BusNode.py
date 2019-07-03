from abc import ABC, abstractmethod
from Messaging.EventBus import EventBus

class BusNode(ABC):

	def __init__(self, messageBus):
		self.messageBus = messageBus
		self.messageBus.AddListener(self)

	@abstractmethod
	def OnEvent(self, event):
		pass

	def SendEvent(self, event):
		self.messageBus.PostEvent(event)

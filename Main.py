from Simulator import Simulator
from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048
from Messaging.EventBus import EventBus
from App import Application
from UI.UI import UI
import time

bus = EventBus()
#sim = Simulator(2, Web2048, 1, 5, bus)
ui = UI(bus)
app = Application(bus)

def main():
    deltaTime = 0
    while(True):
        start = time.time()
        #sim.Update(deltaTime)
        bus.NotifyListeners()
        ui.Update()
        end = time.time()
        deltaTime = end - start

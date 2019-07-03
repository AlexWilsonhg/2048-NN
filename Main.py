from Simulator import Simulator
from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048
from Messaging.EventBus import EventBus
import time

bus = EventBus()
sim = Simulator(2, Web2048, 1, 5, bus)

def main():
    deltaTime = 0
    while(True):
        start = time.time()
        sim.Update(deltaTime)
        bus.Notify()
        end = time.time()
        deltaTime = end - start

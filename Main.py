from Simulator import Simulator
from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048
from Messaging.EventBus import EventBus
from App import Application
from UI.UI import UI
import time


app = Application()

if __name__ == "__main__":
    deltaTime = 0
    while(True):
        start = time.time()
        app.Update(deltaTime)
        end = time.time()
        deltaTime = end - start

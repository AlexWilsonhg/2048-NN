from Simulator import Simulator
from Web2048 import Web2048
from Mock2048 import Mock2048
import time

sim = Simulator(4, Web2048, 1, 5)

def main():
    deltaTime = 0
    while(True):
        start = time.time()
        sim.Update(deltaTime)
        end = time.time()
        deltaTime = end - start

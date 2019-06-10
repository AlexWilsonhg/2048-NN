
from Simulator import Simulator
from Web2048 import Web2048
from Mock2048 import Mock2048
import time

sim = Simulator(1, Web2048(), 1, 5)

def main():
    deltaTime = time.time()
    while(True):
        sim.Update(deltaTime)
        ##sim.EvolveGamePlayers()

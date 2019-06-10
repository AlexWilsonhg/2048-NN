
from Simulator import Simulator
from GenerationTimer import GenerationTimer
from Web2048 import Web2048
from Mock2048 import Mock2048
import time

sim = Simulator(1, Web2048(), 1, 5)
timer = GenerationTimer()

def main():
    deltaTime = 0
    while(True):
        start = time.time()
        sim.Update(deltaTime)
        timer.Update(sim, deltaTime)
        print(timer.GetTimeRemaining())
        end = time.time()
        deltaTime = end - start
        ##sim.EvolveGamePlayers()

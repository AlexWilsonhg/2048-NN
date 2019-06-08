
from Simulator import Simulator
from Web2048 import Web2048

sim = Simulator(1, Web2048(), 1, 5)

def main():
    while(sim.hasEpochsRemaining()):
        sim.RunEpoch()
        sim.EvolveGamePlayers()
        sim.ResetGameplayers()

    


from Simulator import Simulator

sim = Simulator(1, 1, 5)

def main():
    while(sim.hasEpochsRemaining()):
        sim.RunEpoch()
        sim.EvolveGamePlayers()
        sim.ResetGameplayers()

    

from GamePlayer import GamePlayer
from Brains.NeuralNetBrain import NeuralNet
from Genetics import Genetics
import numpy as np
import time

class Simulator:

    def __init__(self, numPlayers, epochs, gamesPerEpoch):
        self.activePlayers = []
        self.inactivePlayers =[]
        self.avgScores = []
        self.epochs = epochs
        self.gamesPerEpoch = gamesPerEpoch
        self.genetics = Genetics(0.1,0.05)
        for i in range(numPlayers):
            self.activePlayers.append(GamePlayer(NeuralNet([16,32,4], 0.01), 0.0125))


    def ResetGameplayers(self):
        for i in self.inactivePlayers:
            self.activePlayers.append(i)
        self.inactivePlayers.clear()
                                

    def AverageScore(self):
        avg = 0
        scoresSum = 0
        for i in self.inactivePlayers:
            scoresSum += np.mean(i.scores)
        return scoresSum / len(self.inactivePlayers)


    def Step(self, deltaTime):
        for i in reversed(self.activePlayers):
            i.Update(deltaTime)
            if i.numGames == 0:
                self.inactivePlayers.append(i)
                self.activePlayers.remove(i)

                               
    def RunEpoch(self):
        for player in self.activePlayers:
            player.numGames = self.gamesPerEpoch
            player.scores = []

        deltaTime = time.time()
        while(len(self.activePlayers) > 0):
            start = time.time()
            self.Step(deltaTime)
            end = time.time()
            deltaTime = end-start
        self.epochs -= 1
        self.avgScores.append(self.AverageScore())

                                 
    def hasEpochsRemaining(self):
        return self.epochs > 0
                                 

    def EvolveGamePlayers(self):
        newWeights = self.genetics.Evolve(self.inactivePlayers)
        for i in range(len(self.inactivePlayers)):
            inactivePlayers[i].brain.weights = newWeights[i]

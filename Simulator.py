from GamePlayer import GamePlayer
from Brains.NeuralNetBrain import NeuralNet
from Genetics import Genetics
import numpy as np
import time

class Simulator:

    def __init__(self, numPlayers, gameSource, epochs, gamesPerEpoch):
        self.activePlayers = []
        self.inactivePlayers = []
        self.avgScores = []
        self.epochs = epochs
        self.gamesPerEpoch = gamesPerEpoch
        self.genetics = Genetics(0.1,0.05)
        
        for i in range(numPlayers):
            self.inactivePlayers.append(GamePlayer(NeuralNet([16,32,4], 0.01), gameSource))
        self.ResetGamePlayers()


    def ResetGamePlayers(self):
        for i in self.inactivePlayers:
            i.numGames = self.gamesPerEpoch
            i.scores = []
            self.activePlayers.append(i)
        self.inactivePlayers.clear()

                   
    def AverageScore(self):
        avg = 0
        scoresSum = 0
        for i in self.inactivePlayers:
            scoresSum += np.mean(i.scores)
        return scoresSum / len(self.inactivePlayers)


    def UpdateGamePlayers(self, deltaTime):
        for i in reversed(self.activePlayers):
            i.Update(deltaTime)
            if i.numGames == 0:
                self.inactivePlayers.append(i)
                self.activePlayers.remove(i)

                         
    def Update(self, deltaTime):
        if(self.hasEpochsRemaining()):
            if(self.hasActivePlayers()):
                self.UpdateGamePlayers(deltaTime)
            else:
                self.epochs -= 1
                self.avgScores.append(self.AverageScore())

                    
    def hasEpochsRemaining(self):
        return self.epochs > 0

    def hasActivePlayers(self):
        return len(self.activePlayers) > 0


    def EvolveGamePlayers(self):
        newWeights = self.genetics.Evolve(self.inactivePlayers)
        for i in range(len(self.inactivePlayers)):
            inactivePlayers[i].brain.weights = newWeights[i]

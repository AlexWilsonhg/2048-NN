from GamePlayer import GamePlayer
from Brains.NeuralNetBrain import NeuralNet
from Genetics import Genetics
import numpy as np

class Simulator:

    def __init__(self, numPlayers, gameSource, generations, gamesPerGeneration):
        self.activePlayers = []
        self.inactivePlayers = []
        self.avgScores = []
        self.generations = generations
        self.gamesPerGeneration = gamesPerGeneration
        self.genetics = Genetics(0.1,0.05)
        
        for i in range(numPlayers):
            self.inactivePlayers.append(GamePlayer(NeuralNet([16,32,4], 0.01), gameSource))
        self.ResetGamePlayers()


    def ResetGamePlayers(self):
        for i in self.inactivePlayers:
            i.numGames = self.gamesPerGeneration
            i.scores = []
            self.activePlayers.append(i)
        self.inactivePlayers.clear()

                   
    def GetAverageScore(self):
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
        if(self.HasGenerationsRemaining()):
            if(self.HasActivePlayers()):
                self.UpdateGamePlayers(deltaTime)
            else:
                self.generations -= 1
                self.avgScores.append(self.GetAverageScore())

                    
    def HasGenerationsRemaining(self):
        return self.generations > 0


    def HasActivePlayers(self):
        return len(self.activePlayers) > 0


    def EvolveGamePlayers(self):
        newWeights = self.genetics.Evolve(self.inactivePlayers)
        for i in range(len(self.inactivePlayers)):
            inactivePlayers[i].brain.weights = newWeights[i]


    def EstimateGenerationEnd(self):
        highestDurationAverage = 0
        slowestPlayer = None
        for i in self.activePlayers:
            average = i.GetAverageGameDuration()
            if average >= highestDurationAverage:
                highestDurationAverage = average
                slowestPlayer = i

        gamesLeft = slowestPlayer.GetGamesRemaining()
        estimatedTimeLeft = average * gamesLeft
        return estimatedTimeLeft
from GamePlayer import GamePlayer
from Brains.NeuralNetBrain import NeuralNet
from Genetics import Genetics

from GameSource.Web2048 import Web2048
from GameSource.Mock2048 import Mock2048
from GameSource.Desktop2048 import Desktop2048

from Messaging.BusNode import BusNode
from Messaging.Events import *

import numpy as np

class Simulator(BusNode):

    def __init__(self, eventBus):
        self.activePlayers = []
        self.inactivePlayers = []
        self.avgScores = []
        self.generations = 0
        self.gamesPerGeneration = 0
        self.genetics = Genetics(0.1,0.05)
        self.running = False

        super().__init__(eventBus)
        self.bus = eventBus


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
        if(self.running):
            if(self.HasActivePlayers()):
                self.UpdateGamePlayers(deltaTime)
            elif(self.HasGenerationsRemaining()):
                super().SendEvent(NEW_GENERATION())
                self.generations -= 1
                self.avgScores.append(self.GetAverageScore())
                self.EvolveGamePlayers()
                self.ResetGamePlayers()
                    
    def HasGenerationsRemaining(self):
        return self.generations > 0


    def HasActivePlayers(self):
        return len(self.activePlayers) > 0


    def EvolveGamePlayers(self):
        newWeights = self.genetics.Evolve(self.inactivePlayers)
        for i in range(len(self.inactivePlayers)):
            self.inactivePlayers[i].brain.weights = newWeights[i]
            self.inactivePlayers[i].generation += 1

    def Pause(self):
        self.running = False

    def Play(self):
        self.running = True

    def NewSimulation(self, gameSource, numPlayers, generations, gamesPerGeneration):
        self.activePlayers = []
        self.inactivePlayers = []
        self.avgScores = []
        self.generations = generations
        self.gamesPerGeneration = gamesPerGeneration
        for i in range(numPlayers):
            game = gameSource()
            self.inactivePlayers.append(GamePlayer(NeuralNet([16,32,4], 0.01), game, self.bus))
        self.ResetGamePlayers()

    def CloseSimulation(self):
        self.Pause()
        self.ResetGamePlayers()
        self.generations = 0
        self.avgScores = []
        for player in self.activePlayers:
            player.Close()
        self.activePlayers.clear()

    def OnEvent(self, event):
        if(type(event) == NEW_SIMULATION):
            self.CloseSimulation()
            self.NewSimulation(event.gameSource, event.numPlayers, event.generations, event.gamesPerGeneration)

        elif(type(event) == PLAY_SIMULATION):
            self.Play()

        elif(type(event) == PAUSE_SIMULATION):
            self.Pause()

        elif(type(event) == CLOSE_SIMULATION):
            self.CloseSimulation()

        elif(type(event) == SHUTDOWN):
            self.CloseSimulation()
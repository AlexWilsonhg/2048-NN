from selenium import webdriver
from GamePlayer import GamePlayer
from Brains.NeuralNetBrain import NeuralNet
from Genetics import Genetics
import numpy as np
import time

activePlayers = []
inactivePlayers = []
avgScores = []
genetics = Genetics(0.1, 0.05)

activePlayers.append(GamePlayer(NeuralNet([16,32, 4],0.01), 0.125))
activePlayers.append(GamePlayer(NeuralNet([16,32, 4],0.01), 0.125))
activePlayers.append(GamePlayer(NeuralNet([16,32, 4],0.01), 0.125))
activePlayers.append(GamePlayer(NeuralNet([16,32, 4],0.01), 0.125))
activePlayers.append(GamePlayer(NeuralNet([16,32, 4],0.01), 0.125))
activePlayers.append(GamePlayer(NeuralNet([16,32, 4],0.01), 0.125))

def Step(deltaTime):
    for i in reversed(activePlayers):
        i.Update(deltaTime)
        if i.numGames == 0:
            inactivePlayers.append(i)
            activePlayers.remove(i)

def Epoch(numGames):
    for player in activePlayers:
        player.numGames = numGames
        player.scores = []

    deltaTime = time.time()
    while(len(activePlayers) > 0):
        start = time.time()
        Step(deltaTime)
        end = time.time()
        deltaTime = end-start

def Reset():
    for i in inactivePlayers:
        activePlayers.append(i)
    inactivePlayers.clear()

def AverageScore(gameplayers):
    avg = 0
    scoresSum = 0
    for i in gameplayers:
        scoresSum += np.mean(i.scores)
    return scoresSum / len(gameplayers)
    
def Simulate(numEpochs, gamesPerEpoch):
    epochsRemaining = numEpochs
    while(epochsRemaining > 0):
        Epoch(gamesPerEpoch)
        newWeights = genetics.Evolve(inactivePlayers)
        for i in range(len(inactivePlayers)):
            inactivePlayers[i].brain.weights = newWeights[i]

        avgScores.append(AverageScore(inactivePlayers))
        epochsRemaining -= 1
        Reset()



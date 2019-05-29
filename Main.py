from selenium import webdriver
from GamePlayer import GamePlayer
from Brains.NeuralNetBrain import NeuralNet
import time

activePlayers = []
inactivePlayers = []


activePlayers.append(GamePlayer(NeuralNet([16,32,32,16,4],0.01), 500, 0.125))
activePlayers.append(GamePlayer(NeuralNet([16,32,4],0.01), 500, 0.125))
activePlayers.append(GamePlayer(NeuralNet([16,32,32,16,4],0.01), 500, 0.125))



def Step(deltaTime):
    for i in activePlayers:
        i.Update(deltaTime)
        
def Run():
    deltaTime = time.time()
    while(len(activePlayers) > 0):
        start = time.time()
        Step(deltaTime)
        end = time.time()
        deltaTime = end-start


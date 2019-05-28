from selenium import webdriver
from GamePlayer import GamePlayer
from Brains.RandomBrain import RandomBrain
import time

activePlayers = []
inactivePlayers = []


activePlayers.append(GamePlayer(RandomBrain(), 2, 1))
activePlayers.append(GamePlayer(RandomBrain(), 5, 1))

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


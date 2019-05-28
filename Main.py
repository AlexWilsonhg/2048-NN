from selenium import webdriver
from GamePlayer import GamePlayer
from Brains.RandomBrain import RandomBrain

players = []


players.append(GamePlayer(RandomBrain(), 2))


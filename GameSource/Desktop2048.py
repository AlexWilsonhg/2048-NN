from .iGame import iGame
import os

class Desktop2048(iGame):

    def __init__(self):
        pass

    def IsGameOver(self):
        return True

    def GetScore(self):
        return 0

    def GetTiles(self):
        tiles = [0] * 16

    def NewGame(self):
        pass

    def DoMove(self, moves):
        pass

    def Close(self):
        pass

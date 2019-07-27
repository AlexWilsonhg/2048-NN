from .iGame import iGame
import os
import subprocess
import pymem

from ctypes import *
from ctypes.wintypes import *

OpenProcess = windll.kernel32.OpenProcess
ReadProcessMemory = windll.kernel32.ReadProcessMemory

class Desktop2048(iGame):

    def __init__(self):
        pass

    def IsGameOver(self):
        return True

    def GetScore(self):
        pass

    def GetTiles(self):
        tiles = [0] * 16
        return tiles

    def NewGame(self):
        pass

    def DoMove(self, moves):
        pass

    def Close(self):
        pass
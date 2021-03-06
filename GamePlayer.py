from Messaging.BusNode import BusNode
from Messaging.Events import *

class GamePlayer(BusNode):

    def __init__(self, brain, game, eventBus, moveDelay = 0):
        self.game = game
        self.brain = brain
        self.scores = []
        self.moveDelay = moveDelay
        self.timeSinceLastMove = 0
        self.fitness = 0
        self.currentGameDuration = 0
        self.gameDurations = []
        self.numGames = 0
        self.generation = 1

        super().__init__(eventBus)
        self.bus = eventBus

    def Update(self, deltaTime):

        if(self.numGames == 0):
            return

        self.timeSinceLastMove += deltaTime
        self.currentGameDuration += deltaTime

        if(self.timeSinceLastMove < self.moveDelay):
            return
        else:
            self.timeSinceLastMove = 0.0
            if(self.game.IsGameOver()):
                super().SendEvent(GAME_OVER(self.game.GetScore()))
                self.gameDurations.append(self.currentGameDuration)
                self.Reset()
            else:
                self.TakeTurn()
      
    def Reset(self):
        self.scores.append(self.game.GetScore())
        self.currentGameDuration = 0
        self.game.NewGame()
        self.numGames -= 1

    def TakeTurn(self):
        tiles = self.game.GetTiles()
        moves = self.brain.GetMoves(tiles)
        self.game.DoMove(moves)
        
    def GetAverageGameDuration(self):
        if(len(self.gameDurations) == 0):
            return 0
        durationSum = sum(self.gameDurations)
        durationAverage = durationSum / len(self.gameDurations)
        return durationAverage

    def GetGamesRemaining(self):
        return self.numGames

    def OnEvent(self, event):
        pass

    def Close(self):
        self.game.Close()

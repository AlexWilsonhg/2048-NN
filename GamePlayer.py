class GamePlayer:

    def __init__(self, brain, game, moveDelay = 0.125):
        self.game = game
        self.brain = brain
        self.scores = []
        self.moveDelay = moveDelay
        self.timeSinceLastMove = 0
        self.fitness = 0
        self.currentGameDuration = 0
        self.gameDurations = []
        self.numGames = 0

    def Update(self, deltaTime):

        if(self.numGames == 0):
            return

        self.timeSinceLastMove += deltaTime
        self.currentGameDuration += deltaTime

        if(self.timeSinceLastMove < self.moveDelay):
            return
        else:
            self.timeSinceLastMove = 0.0
            if(self.game.GameOver()):
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
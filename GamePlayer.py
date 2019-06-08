class GamePlayer:

    def __init__(self, brain, game, moveDelay = 0.125):
        self.game = game
        self.brain = brain
        self.scores = []
        self.moveDelay = moveDelay
        self.timeSinceLastMove = 0
        self.fitness = 0

    def Update(self, deltaTime):

        if(self.numGames == 0):
                return

        self.timeSinceLastMove += deltaTime
        if(self.timeSinceLastMove < self.moveDelay):
            return
        else:
            self.timeSinceLastMove = 0.0
            if(self.game.GameOver()):
                self.Reset()
            else:
                self.TakeTurn()
      
    def Reset(self):
        self.scores.append(self.game.GetScore())
        self.game.NewGame()
        self.numGames -= 1

    def TakeTurn(self):
        tiles = self.game.GetTiles()
        moves = self.brain.GetMoves(tiles)
        self.game.DoMove(moves)
        

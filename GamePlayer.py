from selenium import webdriver
from BoardReader import BoardReader
from Mover import Mover

class GamePlayer:

    def __init__(self, brain, moveDelay):
        self.driver = webdriver.Chrome('C:\\Users\\wat\\Desktop\\chromedriver')
        if(self.driver):
            self.driver.get('https://play2048.co/')
        self.brain = brain
        self.boardReader = BoardReader(self.driver)
        self.mover = Mover(self.driver)
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
            if(self.boardReader.GameOver()):
                self.Reset()
                
            else:
                self.TakeTurn()
      
    def Reset(self):
        self.scores.append(self.boardReader.GetScore())
        self.boardReader.NewGame()
        self.boardReader.Reset()
        self.numGames -= 1

    def TakeTurn(self):
        tiles = self.boardReader.GetTiles()
        moves = self.brain.GetMoves(tiles)
        self.mover.DoMove(moves, self.boardReader)
        

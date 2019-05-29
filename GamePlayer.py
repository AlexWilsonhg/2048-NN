from selenium import webdriver
from BoardReader import BoardReader
from Mover import Mover

class GamePlayer:

    def __init__(self, brain, numGames, moveDelay):
        self.driver = webdriver.Chrome('C:\\Users\\wat\\Desktop\\chromedriver')
        if(self.driver):
            self.driver.get('https://play2048.co/')
        self.brain = brain
        self.numGames = numGames
        self.boardReader = BoardReader(self.driver)
        self.mover = Mover(self.driver)
        self.scores = []
        self.moveDelay = moveDelay
        self.timeSinceLastMove = 0


    def Update(self, deltaTime):
        self.timeSinceLastMove += deltaTime
        if(self.timeSinceLastMove < self.moveDelay):
            return
        else:
            self.timeSinceLastMove = 0.0
            if(self.boardReader.GameOver()):
                self.scores.append(self.boardReader.GetScore())
                self.boardReader.NewGame()
                self.boardReader.Reset()
                self.mover.Reset()
                self.numGames -= 1

            if(self.numGames == 0):
                return
                
            else:
                tiles = self.boardReader.GetTiles()
                moves = self.brain.GetMoves(tiles)
                self.mover.DoMove(moves, self.boardReader)
            

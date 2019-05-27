from selenium import webdriver
from BoardReader import BoardReader
from Mover import Mover

class GamePlayer:

    def __init__(self, brain, numGames):
        self.driver = webdriver.Chrome('C:\\Users\\wat\\Desktop\\chromedriver')
        if(self.driver):
            self.driver.get('https://play2048.co/')
        self.brain = brain
        self.numGames = numGames
        self.boardReader = BoardReader(self.driver)
        self.mover = Mover(self.driver)



    def TakeTurn(self):
        tiles = self.boardReader.GetTiles()
        moves = self.brain.GetMoves(tiles)
        self.mover.DoMove(moves, self.boardReader)
            

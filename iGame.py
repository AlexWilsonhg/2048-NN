from abc import ABC, abstractmethod

class iGame(ABC):

    def HasChanged(self):
        tiles = self.GetTiles()
        if(tiles == self.cachedTiles):
            return False
        else:
            self.cachedTiles = tiles
            return True
        
    @abstractmethod
    def GameOver(self):
        pass

    @abstractmethod
    def GetScore(self):
        pass

    @abstractmethod
    def GetTiles(self):
        pass

    @abstractmethod
    def NewGame(self):
        pass

    @abstractmethod
    def DoMove(self, moves):
        pass

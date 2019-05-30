class BoardReader:

    def __init__(self, driver):
        self.driver = driver
        self.cachedTiles = self.GetTiles()


    def HasChanged(self):
        tiles = self.GetTiles()
        if(tiles == self.cachedTiles):
            return False
        else:
            self.cachedTiles = tiles
            return True


    def GameOver(self):
        try:
            if(self.driver.find_element_by_class_name('game-over')):
                return True

            else:
                return False
        except:
            return False


    def Reset(self):
        self.cachedTiles = self.GetTiles()


    def GetScore(self):
        return int(self.driver.find_element_by_class_name('score-container').text.split('\n')[0])


    def GetTiles(self):
        tiles = [0] * 16
        tileDivs = self.driver.find_elements_by_class_name('tile')
        for div in tileDivs:
            try:
                divString = div.get_attribute('class')
                divString = divString.split(' ')
                tileValue = divString[1].split('-')[1]

                tilePos = divString[2].split('-')
                tileX = int(tilePos[2]) - 1
                tileY = int(tilePos[3]) - 1
                tilePos = tileX + (tileY * 4)

                tiles[tilePos] = int(tileValue)
            except:
                break
        return tiles


    def NewGame(self):
        try:
            self.driver.find_element_by_class_name('retry-button').click()
        except:
            return

class MoveValidator:
    
    def __init__(self):
        self.cachedTiles = []

    def ValidMove(self, driver):
        newTiles = self.GetTiles(driver)
        if(self.cachedTiles != newTiles):
            self.cachedTiles = newTiles
            return True
        else:
            return False
    
    def GetTiles(self, driver):
        tiles = [0] * 16
        tileDivs = driver.find_elements_by_class_name('tile')
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

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from .iGame import iGame

keypress = [Keys.ARROW_DOWN,
            Keys.ARROW_RIGHT,
            Keys.ARROW_UP,
            Keys.ARROW_LEFT]

class Web2048(iGame):

    def __init__(self):
        self.driver = webdriver.Chrome('C:\\Users\\wat\\Desktop\\chromedriver')
        if(self.driver):
            self.driver.get('https://play2048.co/')
        self.actions = ActionChains(self.driver)
        self.tileContainer = self.driver.find_element_by_class_name('tile-container')
        self.cachedTiles = self.GetTiles()
        
    def IsGameOver(self):
        try:
            if(self.driver.find_element_by_class_name('game-over')):
                return True
            else:
                return False
        except:
            return False


    def GetScore(self):
        return int(self.driver.find_element_by_class_name('score-container').text.split('\n')[0])


    def GetTiles(self):
        tiles = [0] * 16
        tileDivs = self.tileContainer.find_elements_by_css_selector('div.tile')
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
            self.cachedTiles = self.GetTiles()
        except:
            return

    def DoMove(self, moves):
        self.actions.reset_actions()
        for i in range(len(moves)):
            index = moves.index(max(moves))
            moves[index] = 0
            self.actions.send_keys(keypress[index])
            self.actions.perform()
            if(self.HasChanged()):
                break

    def Close(self):
        self.driver.quit()

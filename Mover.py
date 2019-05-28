from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

keypress = [Keys.ARROW_DOWN,
            Keys.ARROW_RIGHT,
            Keys.ARROW_UP,
            Keys.ARROW_LEFT]

class Mover:

        def __init__(self,driver):
                self.actions = ActionChains(driver)
                self.driver = driver

        def DoMove(self, moves, boardReader):
                for i in range(len(moves)):
                        index = moves.index(max(moves))
                        move = moves.pop(index)
                        print(move)
                        self.actions.send_keys(keypress[index])
                        self.actions.perform()
                        if(boardReader.HasChanged()):
                                break
                return

        def Reset(self):
                ## no clear method for actionchains, so we have to just make a new one.
                self.actions = ActionChains(self.driver) 
                                                                                

        

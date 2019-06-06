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
                self.actions.reset_actions()
                for i in range(len(moves)):
                        index = moves.index(max(moves))
                        moves[index] = 0
                        self.actions.send_keys(keypress[index])
                        self.actions.perform()
                        if(boardReader.HasChanged()):
                                break
                return

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import random

keypress = [Keys.ARROW_DOWN,
            Keys.ARROW_LEFT,
            Keys.ARROW_RIGHT,
            Keys.ARROW_UP]

driver = webdriver.Chrome('C:\\Users\\wat\\Desktop\\chromedriver')
if(driver):
    actions = ActionChains(driver)
    driver.get('https://play2048.co/')
    actions.send_keys(random.choice(keypress))
    actions.perform()

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))
    

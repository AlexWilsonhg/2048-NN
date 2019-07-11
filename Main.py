from App import Application
import time


app = Application()

if __name__ == "__main__":
    deltaTime = 0
    while(True):
        start = time.time()
        app.Update(deltaTime)
        end = time.time()
        deltaTime = end - start

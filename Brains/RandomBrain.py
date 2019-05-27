import random

class RandomBrain:

    def __init__(self):
        return


    def GetMoves(self, tiles):
        return [random.uniform(0.0, 0.99) for c in range(4)]

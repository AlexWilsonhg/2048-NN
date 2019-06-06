import numpy as np
import MyMath as m

class NeuralNet:

    def __init__(self, sizes, learningRate):
        self.numLayers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        self.learningRate = learningRate
        self.activations = []

    def ForwardPropagation(self, inparam):
        self.activations.clear()
        for i in range(len(self.sizes)):
            if(i == 0):
                self.activations.append(inparam)
            else:
                z = np.dot(self.activations[i-1], self.weights[i-1].transpose() ) + self.biases[i-1].transpose()
                g = m.relu(z)
                self.activations.append(g)
        return m.softmax(self.activations[-1])

    def GetMoves(self, tiles):
        tiles = m.normalize(tiles)
        return self.ForwardPropagation(tiles).tolist()[0]

    

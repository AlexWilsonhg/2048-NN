import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    return np.exp(x) / (np.sum(np.exp(x) + 0.000000000001))

def relu(x):
    return np.maximum(0, x)

def normalize(x):
    normalized = []
    valueRange = np.max(x) - np.min(x)
    valueMean = np.mean(x)
    for i in x:
        normalized.append((i - valueMean) / valueRange)
    return normalized
    
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
                g = relu(z)
                self.activations.append(g)
        return softmax(self.activations[-1])

    def GetMoves(self, tiles):
        tiles = normalize(tiles)
        return self.ForwardPropagation(tiles).tolist()[0]

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    return (np.exp(x) / np.sum(np.exp(x)))

class NeuralNet:

    def __init__(self, sizes, learningRate):
        self.numLayers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        self.learningRate = learningRate

    def ForwardPropagation(self, inparam):
        A = []
        for i in range(len(self.sizes)):
            if(i == 0):
                A.append(inparam)
            else:
                z = np.dot(A[i-1], self.weights[i-1].transpose() ) + self.biases[i-1].transpose()
                g = sigmoid(z)
                A.append(g)
        return softmax(A[-1])

    def GetMoves(self, tiles):
        return self.ForwardPropagation(tiles).tolist()[0]

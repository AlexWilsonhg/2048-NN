class NeuralNet:

    def __init__(self, sizes, learningRate):
        self.numLayers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        self.learningRate = learningRate

    def ForwardPropagation(self, inparam):
        return
        
    def FeedForward(self, a):
        return
            
    def BackwardProp(self):
        return

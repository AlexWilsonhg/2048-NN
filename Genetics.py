import numpy as np

class Genetics:

    def __init__(self, mutationRate, mutationSize):
        self.mutationRate = 1-mutationRate
        self.mutationSize = mutationSize

    def Evolve(self, gameplayers):
        self.EvaluateFitness(gameplayers)
        parentA = gameplayers[0]
        parentB = gameplayers[1]

        newBrains = []

        for i in range(len(gameplayers)):
            weights = []
            for i in range(len(parentA.brain.weights)):
                weightA = parentA.brain.weights[i]
                weightB = parentB.brain.weights[i]
                crossover = self.Crossover(weightA, weightB)
                mutate = self.Mutate(crossover)
                weights.append(mutate)
            newBrains.append(weights)

        return newBrains

    def Crossover(self, A, B):
        assert(A.shape == B.shape)
        mask = np.random.randn(A.shape[0], A.shape[1]) > 0
        return np.where(mask, A, B)

    def Mutate(self, A):
        mask = np.random.randn(A.shape[0], A.shape[1]) > self.mutationRate
        mutations = np.random.uniform(low = 0, high = self.mutationSize, size =(A.shape[0],A.shape[1]))
        return np.where(mask, A+mutations, A)

    def EvaluateFitness(self, gameplayers):
        for i in gameplayers:
            mean = np.mean(i.scores)
            std = np.std(i.scores)
            i.fitness = mean - std
        gameplayers.sort(key=lambda x: x.fitness, reverse=True)

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

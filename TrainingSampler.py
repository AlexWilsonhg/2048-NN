class TrainingSampler:

    def __init__(self):
        self.samples = []
        
    def SaveSample(self, sample):
        self.samples.append(sample)

    def ValidateSamples(self):
        ## sum the individual samples.
        ## sort the array based on sums.
        ## array elements must be either 2 or 4 greater than the
        ## previous element to be valid.
        return

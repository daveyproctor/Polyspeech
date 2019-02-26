import time

class ProgressTracker(object):
    def __init__(self, maxCount, everyPercent=5):
        self.maxCount = maxCount
        self.soFar = 0
        self.everyPercent = everyPercent
        self.start = time.time()
        self.internalI = 0
        
    def update(self, i=None):
        if i is None:
            # can call wo argument
            self.internalI += 1
            i = self.internalI
        percentDone = (i/self.maxCount * 100)
        if self.soFar + self.everyPercent < percentDone:
            self.soFar += self.everyPercent
            print("{} percent done. i: {}. Time Elapsed: {}".format(self.soFar, i, time.time()-self.start))

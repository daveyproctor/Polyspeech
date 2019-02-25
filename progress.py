class ProgressTracker(object):
    def __init__(self, maxCount, everyPercent=5):
        self.maxCount = maxCount
        self.soFar = 0
        self.everyPercent = everyPercent
        
    def update(self, i):
        percentDone = (i/self.maxCount * 100)
        if self.soFar + self.everyPercent < percentDone:
            self.soFar += self.everyPercent
            print("{} percent done. i: {}".format(self.soFar, i))

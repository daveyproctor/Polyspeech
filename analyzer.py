import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        def genSet(filename):
            """read lines of file into a set"""
            with open(filename, "r") as f_in:
                text = f_in.read()      
                return set(text.splitlines())

        self.pos = genSet(positives)
        self.neg = genSet(negatives)

    def analyze(self, text):
        """analyze text for sentiment, returning its score."""

        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        pos_count = sum(1 for word in tokens if word in self.pos) 
        neg_count = sum(1 for word in tokens if word in self.neg)
        return pos_count - neg_count


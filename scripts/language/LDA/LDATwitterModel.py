import gensim
from gensim import corpora
import logging
import sys
import pandas as pd
from ast import literal_eval

globalPrefix = "/Users/daveyproctor/Documents/Polyspeech/"
print(globalPrefix)
outPrefix = globalPrefix + "data/tweets/analysis/LDA/"
dataPrefix = globalPrefix + "data/tweets/processed/LDA/"

# Set up log per https://miningthedetails.com/blog/python/lda/GensimLDA/
logPath = globalPrefix + 'logs/lda_model.log'
print(logPath)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class LDATwitterModel(object):
    def __init__(self, text_data=None, docNum=None, NUM_TOPICS=5, grouped=True, passes=15):
        """ tweetsDF should have a preppedTweets field """
        helperPrefix = outPrefix + "LDAHelpers/"
        helperSuffix = f".docNum={docNum}.grouped={grouped}"
        self.modelPrefix = outPrefix + "LDAModels/"
        self.modelSuffix = helperSuffix + f".NUM_TOPICS={NUM_TOPICS}.gensim"
        self.modelPath = self.modelPrefix + "model" + self.modelSuffix
        
        # Params
        self.NUM_TOPICS = NUM_TOPICS
        self.passes = passes
        
        # Get documents
        sys.stdout.write("Getting Documents...")
        if text_data is None:
            if grouped:
                dfPath = dataPrefix + "GroupedLDA.csv"
            else:
                dfPath = dataPrefix + "TweetsLDA.csv"
            sys.stdout.write(f"path {dfPath}...")
            self.tweetsDF = pd.read_csv(dfPath)
            self.text_data = self.tweetsDF.loc[:docNum,"preppedTweets"].apply(lambda x: literal_eval(x))
        else:
            # self.tweetsDF = tweetsDF
            self.text_data = text_data


        print(self.text_data[:10])
        print("Done.")

        sys.stdout.write("Getting Dictionary...")
        # try:
        #     dictPath = helperPrefix + "dictionary" + helperSuffix + ".gensim"
        #     self.dictionary = corpora.Dictionary.load(dictPath)
        #     print(f"Reloaded from {dictPath}")
        # except FileNotFoundError:
        self.dictionary = corpora.Dictionary(self.text_data)
        #    self.dictionary.save(dictPath)
        print("Done.")
        
        sys.stdout.write("Getting Corpus...")
        # try:
        #     corpPath = helperPrefix + "corpus" + helperSuffix + ".pkl"
        #     self.corpus = pickle.load(open(corpPath, "rb"))
        #     print(f"Reloaded from {corpPath}")
        # except FileNotFoundError:
        self.corpus = [self.dictionary.doc2bow(text) for text in self.text_data]
        #     pickle.dump(corpus, open(corpPath, 'wb'))
        print("Done.")
        
    def train(self):
        try:
            self.ldamodel = gensim.models.ldamodel.LdaModel.load(self.modelPath)
            print(f"Found pretrained model {self.modelPath}")
            return
        except FileNotFoundError:
            pass
        self.ldamodel = gensim.models.ldamodel.LdaModel(self.corpus, num_topics = self.NUM_TOPICS, id2word=self.dictionary, passes=self.passes)
        self.ldamodel.save(self.modelPath)

#         lda_display = pyLDAvis.gensim.prepare(self.ldamodel, self.corpus, self.dictionary, sort_topics=False)
#         pyLDAvis.display(lda_display)

if __name__ == "__main__":
    model = LDATwitterModel(docNum = 10, grouped=False)
    model.train()



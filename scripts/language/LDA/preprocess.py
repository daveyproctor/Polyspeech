# https://github.com/susanli2016/Machine-Learning-with-Python
globalPrefix="/Users/daveyproctor/Documents/Polyspeech/"
dataPath = globalPrefix + "data/tweets/raw/tweetsDFMinReadable.csv"
processedPath = globalPrefix + "data/tweets/processed"

import csv
from progress import ProgressTracker
import pandas as pd
import numpy as np
import pickle
import json
import spacy
from spacy.lang.en import English
import nltk
from progress import ProgressTracker

spacy.load('en')
parser = English()

def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

nltk.download('wordnet')

from nltk.corpus import wordnet as wn
def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
from nltk.stem.wordnet import WordNetLemmatizer
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))

def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

tweetsDF = pd.read_csv(dataPath)

print("Start processing")
tracker = ProgressTracker(len(rawTweets), 1)
preppedTweets = []
for i, text in enumerate(rawTweets):
    preppedTweets.append(prepare_text_for_lda(text))
    tracker.update(i)

tweetsDF["preppedTweets"] = np.nan
tweetsDF = tweetsDF.loc[:, ("twitter_account", "preppedTweets")]
tweetsDF["preppedTweets"] = preppedTweets
tweetsDF.to_csv(processedPath + "tweets/processed/LDA/TweetsLDA1.csv", index=False)

print("Start group operation")
groupedDF = tweetsDF.groupby("twitter_account").sum().reset_index()
groupedDF.to_csv(processedPath + "tweets/processed/LDA/GroupedLDA1.csv", index=False)










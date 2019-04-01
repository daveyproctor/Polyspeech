import numpy as np

class Scraper(object):
    def __init__(self, analyzer):
        self.keys = ["tweet_id", "time_created", "full_text", "is_retweet", "retweet_count", "favorite_count", "hashtag_count"] + [f"hashtags{i}" for i in range(5)] + ["user_mentions_count"] + [f"user_mentions{i}" for i in range(5)] + ["in_reply_to_screen_name", "in_reply_to_status_id"] + [f"vader_{type}" for type in ("pos", "neg", "neu", "compound")]
        self.analyzer = analyzer
        self.last_score = {}

    def getKey(self, tweet,key):
        if key in tweet:
            return tweet[key]
        return np.nan

    def gettweet_id(self, tweet):
        return self.getKey(tweet, "id_str")

    def gettime_created(self, tweet):
        return self.getKey(tweet, "created_at")

    def getfull_text(self, tweet):
        return self.getKey(tweet, "full_text")

    def getis_retweet(self, tweet):
        if "retweeted_status" in tweet:
            return True
        return False

    def getretweet_count(self, tweet):
        return self.getKey(tweet, "retweet_count")

    def getfavorite_count(self, tweet):
        return self.getKey(tweet, "favorite_count")

    def gethashtag_count(self, tweet):
        if "hashtags" in tweet:
                return len(tweet["hashtags"])
        return np.nan
    def gethashtags(self, tweet, i):
        if "hashtags" in tweet:
            if len(tweet["hashtags"]) > i:
                return tweet["hashtags"][i]["text"]
        return np.nan
    def gethashtags0(self, tweet):
        return self.gethashtags(tweet, 0)
    def gethashtags1(self, tweet):
        return self.gethashtags(tweet, 1)
    def gethashtags2(self, tweet):
        return self.gethashtags(tweet, 2)
    def gethashtags3(self, tweet):
        return self.gethashtags(tweet, 3)
    def gethashtags4(self, tweet):
        return self.gethashtags(tweet, 4)

    def getuser_mentions_count(self, tweet):
        if "user_mentions" in tweet:
            return len(tweet["user_mentions"])
        return np.nan
    def getuser_mentions(self, tweet, i):
        if "user_mentions" in tweet:
            if len(tweet["user_mentions"]) > i:
                return tweet["user_mentions"][i]["screen_name"]
        return np.nan
    def getuser_mentions0(self, tweet):
        return self.getuser_mentions(tweet, 0)
    def getuser_mentions1(self, tweet):
        return self.getuser_mentions(tweet, 1)
    def getuser_mentions2(self, tweet):
        return self.getuser_mentions(tweet, 2)
    def getuser_mentions3(self, tweet):
        return self.getuser_mentions(tweet, 3)
    def getuser_mentions4(self, tweet):
        return self.getuser_mentions(tweet, 4)

    def getin_reply_to_screen_name(self, tweet):
        return self.getKey(tweet, "in_reply_to_screen_name")
    def getin_reply_to_status_id(self, tweet):
        return self.getKey(tweet, "in_reply_to_status_id")

    def getvader_pos(self, tweet):
        self.last_score = self.analyzer.polarity_scores(self.getKey(tweet, "full_text"))
        return self.last_score["pos"]
    def getvader_neg(self, tweet):
        return self.last_score["neg"]
    def getvader_neu(self, tweet):
        return self.last_score["neu"]
    def getvader_compound(self, tweet):
        return self.last_score["compound"]











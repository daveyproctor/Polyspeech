import numpy as np

def getKey(tweet,key):
    if key in tweet:
        return tweet[key]
    return np.nan

def gettweet_id(tweet):
    return getKey(tweet, "id_str")

def gettime_created(tweet):
    return getKey(tweet, "created_at")

def getfull_text(tweet):
    return getKey(tweet, "full_text")

def getis_retweet(tweet):
    if "retweeted_status" in tweet:
    	return True
    return False

def getretweet_count(tweet):
    return getKey(tweet, "retweet_count")

def getfavorite_count(tweet):
    return getKey(tweet, "favorite_count")

def gethashtag_count(tweet):
	if "hashtags" in tweet:
		return len(tweet["hashtags"])
	return np.nan
def gethashtags(tweet, i):
	if "hashtags" in tweet:
		if len(tweet["hashtags"]) > i:
			return tweet["hashtags"][i]["text"]
	return np.nan
def gethashtags0(tweet):
	return gethashtags(tweet, 0)
def gethashtags1(tweet):
	return gethashtags(tweet, 1)
def gethashtags2(tweet):
	return gethashtags(tweet, 2)
def gethashtags3(tweet):
	return gethashtags(tweet, 3)
def gethashtags4(tweet):
	return gethashtags(tweet, 4)

def getuser_mentions_count(tweet):
	if "user_mentions" in tweet:
		return len(tweet["user_mentions"])
	return np.nan
def getuser_mentions(tweet, i):
	if "user_mentions" in tweet:
		if len(tweet["user_mentions"]) > i:
			return tweet["user_mentions"][i]["screen_name"]
	return np.nan
def getuser_mentions0(tweet):
	return getuser_mentions(tweet, 0)
def getuser_mentions1(tweet):
	return getuser_mentions(tweet, 1)
def getuser_mentions2(tweet):
	return getuser_mentions(tweet, 2)
def getuser_mentions3(tweet):
	return getuser_mentions(tweet, 3)
def getuser_mentions4(tweet):
	return getuser_mentions(tweet, 4)

def getin_reply_to_screen_name(tweet):
	return getKey(tweet, "in_reply_to_screen_name")
def getin_reply_to_status_id(tweet):
	return getKey(tweet, "in_reply_to_status_id")

keys = ["tweet_id", "time_created", "full_text", "is_retweet", "retweet_count", "favorite_count", "hashtag_count"] + [f"hashtags{i}" for i in range(5)] + ["user_mentions_count"] + [f"user_mentions{i}" for i in range(5)] + ["in_reply_to_screen_name", "in_reply_to_status_id"]














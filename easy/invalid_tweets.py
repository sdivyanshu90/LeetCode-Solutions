import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweet_ids = tweets[tweets['content'].str.len() > 15]
    return invalid_tweet_ids[['tweet_id']]
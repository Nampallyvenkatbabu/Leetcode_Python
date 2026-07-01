import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[
        tweets["content"].str.len() > 15
    ][["tweet_id"]]
    
""" Without function

tweets = pd.DataFrame({
    "tweet_id": [1, 2],
    "content": [
        "Let us Code",
        "More than fifteen chars are here!"
    ]
})

result = tweets[tweets["content"].str.len() > 15][["tweet_id"]]

print(result)



"""
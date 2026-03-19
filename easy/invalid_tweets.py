import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweet_ids = tweets[tweets['content'].str.len() > 15]
    return invalid_tweet_ids[['tweet_id']]

def test_invalid_tweets():
    # Test case 1
    tweets = pd.DataFrame({
        'tweet_id': [1, 2, 3, 4],
        'content': ['Hello World', 'This is a test tweet', 'Short', 'Another long tweet that exceeds the limit']
    })
    expected_output = pd.DataFrame({
        'tweet_id': [2, 4]
    })
    output = invalid_tweets(tweets)
    print(output.equals(expected_output)) # Expected output: False

    # Test case 2
    tweets = pd.DataFrame({
        'tweet_id': [1, 2, 3],
        'content': ['Short tweet', 'Another short one', 'This one is way too long and should be flagged as invalid']
    })
    expected_output = pd.DataFrame({
        'tweet_id': [3]
    })
    output = invalid_tweets(tweets)
    print(output.equals(expected_output)) # Expected output: False

    # Test case 3
    tweets = pd.DataFrame({
        'tweet_id': [1, 2, 3],
        'content': ['All good here', 'Nothing to see', 'Just a normal tweet']
    })
    expected_output = pd.DataFrame({
        'tweet_id': []
    })
    output = invalid_tweets(tweets)
    print(output.equals(expected_output)) # Expected output: False

    # Test case 4
    tweets = pd.DataFrame({
        'tweet_id': [1, 2, 3, 4],
        'content': ['This is fine', 'This is also fine', 'This one is too long and should be invalid', 'Another valid tweet']
    })
    expected_output = pd.DataFrame({
        'tweet_id': [3]
    })
    output = invalid_tweets(tweets)
    print(output.equals(expected_output)) # Expected output: False

    # Test case 5
    tweets = pd.DataFrame({
        'tweet_id': [1, 2, 3],
        'content': ['Short', 'This is a very long tweet that should be invalid', 'Another short one']
    })
    expected_output = pd.DataFrame({
        'tweet_id': [2]
    })
    output = invalid_tweets(tweets)
    print(output.equals(expected_output)) # Expected output: False

test_invalid_tweets()
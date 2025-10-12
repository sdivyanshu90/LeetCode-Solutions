import pandas as pd
import numpy as np

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if scores.empty:
        return pd.DataFrame({'score': [], 'rank': []})

    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    
    scores = scores.sort_values(by='score', ascending=False)
    
    return scores[['score','rank']]

def test_order_scores():
    s = order_scores

    # Test Case 1: Standard case with ties and unique scores
    df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'score': [3.50, 3.65, 4.00, 3.85]})
    print(s(df1))
    # Expected Output:
    #   score  rank
    # 2   4.00     1
    # 3   3.85     2
    # 1   3.65     3
    # 0   3.50     4

    # Test Case 2: Empty DataFrame
    df2 = pd.DataFrame({'id': [], 'score': []})
    print(s(df2))
    # Expected Output:
    # Empty DataFrame
    # Columns: [score, rank]
    # Index: []

    # Test Case 3: All scores are the same (a three-way tie)
    df3 = pd.DataFrame({'id': [1, 2, 3], 'score': [4.00, 4.00, 4.00]})
    print(s(df3))
    # Expected Output:
    #   score  rank
    # 0   4.00     1
    # 1   4.00     1
    # 2   4.00     1
    
    # Test Case 4: Complex ties
    df4 = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'score': [4.0, 3.8, 4.0, 3.8, 3.5]})
    print(s(df4))
    # Expected Output:
    #   score  rank
    # 0   4.00     1
    # 2   4.00     1
    # 1   3.80     2
    # 3   3.80     2
    # 4   3.50     3

    # Test Case 5: DataFrame with a single row
    df5 = pd.DataFrame({'id': [1], 'score': [3.99]})
    print(s(df5))
    # Expected Output:
    #   score  rank
    # 0   3.99     1

    # Test Case 6: Negative scores
    df6 = pd.DataFrame({'id': [1, 2, 3], 'score': [-1.5, -0.5, -2.5]})
    print(s(df6))
    # Expected Output:
    #   score  rank
    # 1  -0.50     1
    # 0  -1.50     2
    # 2  -2.50     3

    # Test Case 7: All scores are unique and unordered
    df7 = pd.DataFrame({'id': [1, 2, 3], 'score': [10, 30, 20]})
    print(s(df7))
    # Expected Output:
    #   score  rank
    # 1     30     1
    # 2     20     2
    # 0     10     3

    # Test Case 8: Scores are integers
    df8 = pd.DataFrame({'id': [1, 2, 3, 4], 'score': [100, 200, 100, 300]})
    print(s(df8))
    # Expected Output:
    #   score  rank
    # 3    300     1
    # 1    200     2
    # 0    100     3
    # 2    100     3
    
    # Test Case 9: Input is already sorted
    df9 = pd.DataFrame({'id': [1, 2, 3], 'score': [4.0, 3.9, 3.8]})
    print(s(df9))
    # Expected Output:
    #   score  rank
    # 0   4.00     1
    # 1   3.90     2
    # 2   3.80     3
    
    # Test Case 10: Critical Failure Case - NaN value
    df10 = pd.DataFrame({'id': [1, 2, 3], 'score': [3.5, np.nan, 4.0]})
    print("--- Testing Failure Case with NaN ---")
    try:
        s(df10)
    except Exception as e:
        print(f"Function failed as expected. Error: {e}")
    # Expected Output: A ValueError, because of .astype(int) on a series containing NaN.

test_order_scores()
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['first_login'] = pd.to_datetime(activity['event_date'])
    first_login_dates = activity.groupby('player_id')['first_login'].min().reset_index()
    return first_login_dates

def test_game_analysis():
    # Test Case 1
    data = {
        'player_id': [1, 2, 1, 3, 2, 1],
        'event_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-04', '2023-01-02']
    }
    activity_df = pd.DataFrame(data)
    result = game_analysis(activity_df)
    print(result)

test_game_analysis()
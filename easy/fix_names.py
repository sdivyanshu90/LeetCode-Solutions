import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(users)
    df['name'] = df['name'].str.capitalize()
    return df.sort_values(by='user_id')

def test_fix_names():
    users = pd.DataFrame({
        'user_id': [1, 2, 3],
        'name': ['alice', 'BOB', 'CHARLIE']
    })
    expected_output = pd.DataFrame({
        'user_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie']
    })
    output = fix_names(users)
    print(output.equals(expected_output)) # Expected output: True

test_fix_names()
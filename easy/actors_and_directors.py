import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    result = counts[counts['cooperation_count'] >= 3][['actor_id', 'director_id']]
    return result

def test_actors_and_directors():
    data = {
        'actor_id': [1, 1, 1, 2, 2, 3, 1, 2, 1],
        'director_id': [10, 10, 10, 20, 20, 30, 10, 20, 10]
    }
    df = pd.DataFrame(data)
    expected_data = {
        'actor_id': [1, 2],
        'director_id': [10, 20]
    }
    expected_df = pd.DataFrame(expected_data)
    
    result_df = actors_and_directors(df)
    
    print("Result DataFrame:")
    print(result_df)

test_actors_and_directors()
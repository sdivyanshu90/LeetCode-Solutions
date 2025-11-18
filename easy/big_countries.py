import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
  filtered_countries = world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
  return filtered_countries[['name','population','area']]

def test_big_countries():
    data = {
        'name': ['CountryA', 'CountryB', 'CountryC', 'CountryD', 'CountryE'],
        'population': [10000000, 30000000, 5000000, 40000000, 20000000],
        'area': [2000000, 4000000, 3500000, 2500000, 500000]
    }
    world_df = pd.DataFrame(data)
    
    result_df = big_countries(world_df)
    print(result_df)

test_big_countries()
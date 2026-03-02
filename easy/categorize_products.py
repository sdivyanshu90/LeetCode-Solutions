import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    result = activities.groupby('sell_date')['product'].agg(
        num_sold='nunique',
        products=lambda x: ','.join(sorted(set(x)))
    ).reset_index()

    return result

def test_categorize_products():
    data = {
        'sell_date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
        'product': ['A', 'B', 'A', 'C', 'B']
    }
    activities = pd.DataFrame(data)

    expected_output = pd.DataFrame({
        'sell_date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'num_sold': [2, 2, 1],
        'products': ['A,B', 'A,C', 'B']
    })

    result = categorize_products(activities)
    print(result)
    print(expected_output)
    print(result.equals(expected_output))

test_categorize_products()
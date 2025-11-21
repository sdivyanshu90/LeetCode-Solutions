import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_sales_id = company.loc[company['name']=='RED', 'com_id']
    red_salesmen = orders.loc[orders['com_id'].isin(red_sales_id)]['sales_id'].unique()
    result = sales_person.loc[~sales_person['sales_id'].isin(red_salesmen)][['name']]
    return result

def test_sales_person():
    sales_person_df = pd.DataFrame({
        'sales_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David']
    })

    company_df = pd.DataFrame({
        'com_id': [10, 20],
        'name': ['RED', 'BLUE']
    })

    orders_df = pd.DataFrame({
        'order_id': [100, 101, 102, 103],
        'com_id': [10, 20, 10, 20],
        'sales_id': [1, 2, 3, 4]
    })

    result = sales_person(sales_person_df, company_df, orders_df)
    print(result)  # Expected output: DataFrame with only Bob and David

test_sales_person()
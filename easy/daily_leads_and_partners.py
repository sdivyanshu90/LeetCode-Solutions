import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group the data by 'date_id' and 'make_name' and calculate the number of unique 'lead_id' and 'partner_id'
    result = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()

    return result

def test_daily_leads_and_partners():

    # Test Case 1
    data1 = {
        'date_id': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
        'make_name': ['Toyota', 'Toyota', 'Honda', 'Honda'],
        'lead_id': [1, 2, 3, 4],
        'partner_id': [10, 20, 30, 40]
    }
    df1 = pd.DataFrame(data1)
    print(daily_leads_and_partners(df1)) # Expected Output:
    #   date_id      make_name  unique_leads  unique_partners
    # 0 2021-01-01    Toyota          2             2
    # 1 2021-01-02     Honda          2             2

    # Test Case 2
    data2 = {
        'date_id': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
        'make_name': ['Toyota', 'Honda', 'Toyota', 'Honda'],
        'lead_id': [1, 2, 3, 4],
        'partner_id': [10, 20, 30, 40]
    }
    df2 = pd.DataFrame(data2)
    print(daily_leads_and_partners(df2)) # Expected Output:
    #   date_id     make_name     unique_leads     unique_partners
    # 0 2021-01-01    Honda             1                1
    # 1 2021-01-01    Toyota            1                1
    # 2 2021-01-02    Honda             1                1
    # 3 2021-01-02    Toyota            1                1

    # Test Case 3
    data3 = {
        'date_id': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
        'make_name': ['Toyota', 'Toyota', 'Honda', 'Honda'],
        'lead_id': [1, 1, 2, 2],
        'partner_id': [10, 10, 20, 20]
    }
    df3 = pd.DataFrame(data3)
    print(daily_leads_and_partners(df3)) # Expected Output:
    #   date_id     make_name      unique_leads  unique_partners
    # 0 2021-01-01    Toyota             1                1
    # 1 2021-01-02     Honda             1                1

    # Test Case 4
    data4 = {
        'date_id': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
        'make_name': ['Toyota', 'Honda', 'Toyota', 'Honda'],
        'lead_id': [1, 2, 3, 4],
        'partner_id': [10, 20, 30, 40]
    }
    df4 = pd.DataFrame(data4)
    print(daily_leads_and_partners(df4)) # Expected Output:
    #   date_id      make_name     unique_leads  unique_partners
    # 0 2021-01-01    Honda             1                1
    # 1 2021-01-01    Toyota            1                1
    # 2 2021-01-02    Honda             1                1
    # 3 2021-01-02    Toyota            1                1

    # Test Case 5
    data5 = {
        'date_id': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
        'make_name': ['Toyota', 'Toyota', 'Honda', 'Honda'],
        'lead_id': [1, 2, 3, 4],
        'partner_id': [10, 20, 30, 40]
    }
    df5 = pd.DataFrame(data5)
    print(daily_leads_and_partners(df5)) # Expected Output:
    #   date_id make_name  unique_leads  unique_partners
    # 0 2021-01-01    Toyota             2                2
    # 1 2021-01-02     Honda             2                2

test_daily_leads_and_partners()
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(total_time=employees['out_time'] - employees['in_time']) \
                   .rename(columns={'event_day': 'day'}) \
                   .groupby(['day', 'emp_id'])['total_time'].sum() \
                   .reset_index()


def test_total_time():
    # Test case 1
    employees = pd.DataFrame({
        'emp_id': [1, 1, 2, 2],
        'event_day': [1, 1, 1, 1],
        'in_time': [9, 13, 10, 14],
        'out_time': [12, 17, 12, 18]
    })
    print(total_time(employees))
    # Expected output:
    #    day  emp_id  total_time
    # 0    1       1           7
    # 1    1       2           6

    # Test case 2
    employees = pd.DataFrame({
        'emp_id': [1, 1, 2, 2, 3, 3],
        'event_day': [1, 2, 1, 2, 1, 2],
        'in_time': [9, 9, 10, 10, 11, 11],
        'out_time': [17, 17, 18, 18, 19, 19]
    })
    print(total_time(employees))
    # Expected output:
    #    day  emp_id  total_time
    # 0    1       1           8
    # 1    1       2           8
    # 2    1       3           8
    # 3    2       1           8
    # 4    2       2           8
    # 5    2       3           8

    # Test case 3
    employees = pd.DataFrame({
        'emp_id': [1, 2, 3],
        'event_day': [1, 1, 1],
        'in_time': [9, 10, 11],
        'out_time': [17, 18, 19]
    })
    print(total_time(employees))
    # Expected output:
    #    day  emp_id  total_time
    # 0    1       1           8
    # 1    1       2           8
    # 2    1       3           8

    # Test case 4
    employees = pd.DataFrame({
        'emp_id': [1, 1, 1],
        'event_day': [1, 1, 1],
        'in_time': [9, 13, 17],
        'out_time': [12, 17, 21]
    })
    print(total_time(employees))
    # Expected output:
    #    day  emp_id  total_time
    # 0    1       1          11

    # Test case 5
    employees = pd.DataFrame({
        'emp_id': [1, 2, 3],
        'event_day': [1, 2, 3],
        'in_time': [9, 10, 11],
        'out_time': [17, 18, 19]
    })
    print(total_time(employees))
    # Expected output:
    #    day  emp_id  total_time
    # 0    1       1           8
    # 1    2       2           8
    # 2    3       3           8

test_total_time()
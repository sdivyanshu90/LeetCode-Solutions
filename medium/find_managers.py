import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    direct_reports_count = employee.groupby('managerId').size().reset_index(name='report_count')
    managers_with_at_least_five_reports = direct_reports_count[direct_reports_count['report_count'] >= 5]
    result = employee[employee['id'].isin(managers_with_at_least_five_reports['managerId'])][['name']]
    return result

def test_find_managers():
    data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
        'managerId': [None, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    }
    employee_df = pd.DataFrame(data)
    
    result_df = find_managers(employee_df)
    print(result_df)

test_find_managers()
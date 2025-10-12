import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Handles the case where the dataframe is empty or doesn't have a 'salary' column
    if 'salary' not in employee.columns or employee.empty:
        return pd.DataFrame({'SecondHighestSalary': [None]})
        
    sorted_employee = employee.sort_values(by='salary', ascending=False)

    unique_salaries = sorted_employee['salary'].drop_duplicates()

    if len(unique_salaries) >= 2:
        second_highest = unique_salaries.iloc[1]
    else:
        # Using np.nan is more idiomatic for missing numerical data in pandas
        return pd.DataFrame({'SecondHighestSalary': [np.nan]})

    return pd.DataFrame({'SecondHighestSalary': [second_highest]})

def test_second_highest_salary():
    s = second_highest_salary

    # Test Case 1: Standard case with multiple distinct salaries
    df1 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print(s(df1)) # Expected Output: DataFrame with SecondHighestSalary 200

    # Test Case 2: Empty DataFrame
    df2 = pd.DataFrame({'id': [], 'salary': []})
    print(s(df2)) # Expected Output: DataFrame with SecondHighestSalary NaN

    # Test Case 3: DataFrame with only one employee
    df3 = pd.DataFrame({'id': [1], 'salary': [100]})
    print(s(df3)) # Expected Output: DataFrame with SecondHighestSalary NaN

    # Test Case 4: All employees have the same salary
    df4 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 100, 100]})
    print(s(df4)) # Expected Output: DataFrame with SecondHighestSalary NaN
    
    # Test Case 5: Two distinct salaries
    df5 = pd.DataFrame({'id': [1, 2], 'salary': [100, 200]})
    print(s(df5)) # Expected Output: DataFrame with SecondHighestSalary 100

    # Test Case 6: Duplicates of the highest and second highest salaries
    df6 = pd.DataFrame({'id': [1, 2, 3, 4], 'salary': [300, 200, 300, 200]})
    print(s(df6)) # Expected Output: DataFrame with SecondHighestSalary 200
    
    # Test Case 7: Unordered salaries
    df7 = pd.DataFrame({'id': [1, 2, 3], 'salary': [250, 500, 150]})
    print(s(df7)) # Expected Output: DataFrame with SecondHighestSalary 250

    # Test Case 8: DataFrame with other columns
    df8 = pd.DataFrame({'id': [1, 2, 3], 'name': ['A', 'B', 'C'], 'salary': [50, 100, 75]})
    print(s(df8)) # Expected Output: DataFrame with SecondHighestSalary 75

    # Test Case 9: Salaries include zero
    df9 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 0, 200]})
    print(s(df9)) # Expected Output: DataFrame with SecondHighestSalary 100

    # Test Case 10: Only two employees with the same salary
    df10 = pd.DataFrame({'id': [1, 2], 'salary': [500, 500]})
    print(s(df10)) # Expected Output: DataFrame with SecondHighestSalary NaN

test_second_highest_salary()
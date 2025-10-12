import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # A robust check for invalid N and empty dataframes
    if N <= 0 or 'salary' not in employee.columns or employee.empty:
        # Using np.nan is more idiomatic for missing numerical data in pandas
        return pd.DataFrame({f'getNthHighestSalary({N})': [np.nan]})

    unique_salaries = employee['salary'].unique()

    if len(unique_salaries) < N:
        nth_highest_salary = np.nan
    else:
        # Using np.sort is efficient for numpy arrays
        sorted_salaries = np.sort(unique_salaries)[::-1] # Descending sort
        nth_highest_salary = sorted_salaries[N-1]

    result_df = pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest_salary]})
    return result_df

def test_nth_highest_salary():
    s = nth_highest_salary
    
    # Test Case 1: Standard case (N=2)
    df1 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print(s(df1, 2)) # Expected Output: DataFrame with getNthHighestSalary(2) 200

    # Test Case 2: N=1 (find the highest salary)
    df2 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print(s(df2, 1)) # Expected Output: DataFrame with getNthHighestSalary(1) 300
    
    # Test Case 3: N equals the number of unique salaries
    df3 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print(s(df3, 3)) # Expected Output: DataFrame with getNthHighestSalary(3) 100

    # Test Case 4: N is greater than the number of unique salaries
    df4 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print(s(df4, 4)) # Expected Output: DataFrame with getNthHighestSalary(4) NaN

    # Test Case 5: Empty DataFrame
    df5 = pd.DataFrame({'id': [], 'salary': []})
    print(s(df5, 1)) # Expected Output: DataFrame with getNthHighestSalary(1) NaN
    
    # Test Case 6: All salaries are the same
    df6 = pd.DataFrame({'id': [1, 2, 3], 'salary': [500, 500, 500]})
    print(s(df6, 2)) # Expected Output: DataFrame with getNthHighestSalary(2) NaN

    # Test Case 7: Critical Edge Case (N=0)
    df7 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print(s(df7, 0)) # Expected Output: DataFrame with getNthHighestSalary(0) NaN
    
    # Test Case 8: Critical Edge Case (Negative N)
    df8 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print(s(df8, -1)) # Expected Output: DataFrame with getNthHighestSalary(-1) NaN

    # Test Case 9: DataFrame with duplicate salaries
    df9 = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'salary': [100, 200, 200, 300, 100]})
    print(s(df9, 2)) # Expected Output: DataFrame with getNthHighestSalary(2) 200
    
    # Test Case 10: DataFrame with just enough unique salaries
    df10 = pd.DataFrame({'id': [1, 2, 3, 4], 'salary': [50, 100, 100, 50]})
    print(s(df10, 2)) # Expected Output: DataFrame with getNthHighestSalary(2) 50

test_nth_highest_salary()
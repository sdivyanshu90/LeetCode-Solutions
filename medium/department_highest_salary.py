import pandas as pd
import numpy as np

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame({'Department': [], 'Employee': [], 'salary': []})

    merged_data = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    
    merged_data['max_salary'] = merged_data.groupby('name_y')['salary'].transform('max')
    highest_salary_employees = merged_data[merged_data['salary'] == merged_data['max_salary']]
    
    highest_salary_employees = highest_salary_employees.rename(
        columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}
    )
    
    return highest_salary_employees[['Department', 'Employee', 'Salary']]

def test_department_highest_salary():
    s = department_highest_salary
    
    # Departments DataFrame used for most tests
    departments = pd.DataFrame([
        {'id': 1, 'name': 'IT'},
        {'id': 2, 'name': 'Sales'}
    ])
    
    # Test Case 1: Standard case with unique highest earner in each department
    print("--- Test Case 1: Standard Case ---")
    employees1 = pd.DataFrame([
        {'id': 1, 'name': 'Joe', 'salary': 70000, 'departmentId': 1},
        {'id': 2, 'name': 'Jim', 'salary': 90000, 'departmentId': 1},
        {'id': 3, 'name': 'Henry', 'salary': 80000, 'departmentId': 2},
        {'id': 4, 'name': 'Sam', 'salary': 60000, 'departmentId': 2}
    ])
    print(s(employees1, departments))
    # Expected Output: DataFrame with (IT, Jim, 90000) and (Sales, Henry, 80000)

    # Test Case 2: Tie for the highest salary in a department
    print("\n--- Test Case 2: Tie for Highest Salary ---")
    employees2 = pd.DataFrame([
        {'id': 1, 'name': 'Max', 'salary': 90000, 'departmentId': 1},
        {'id': 2, 'name': 'Janet', 'salary': 90000, 'departmentId': 1},
        {'id': 3, 'name': 'Randy', 'salary': 85000, 'departmentId': 1}
    ])
    print(s(employees2, departments))
    # Expected Output: DataFrame with (IT, Max, 90000) and (IT, Janet, 90000)

    # Test Case 3: Empty Employee DataFrame
    print("\n--- Test Case 3: Empty Employee DataFrame ---")
    employees3 = pd.DataFrame(columns=['id', 'name', 'salary', 'departmentId'])
    print(s(employees3, departments))
    # Expected Output: Empty DataFrame with columns [Department, Employee, Salary]

    # Test Case 4: Employee with a non-existent departmentId
    print("\n--- Test Case 4: Employee with non-existent Department ---")
    employees4 = pd.DataFrame([
        {'id': 1, 'name': 'Alice', 'salary': 75000, 'departmentId': 1},
        {'id': 2, 'name': 'Bob', 'salary': 80000, 'departmentId': 3} # Dept 3 doesn't exist
    ])
    print(s(employees4, departments))
    # Expected Output: DataFrame with (IT, Alice, 75000) and (NaN, Bob, 80000)

    # Test Case 5: Department with no employees
    print("\n--- Test Case 5: Department with no Employees ---")
    departments5 = pd.DataFrame([
        {'id': 1, 'name': 'IT'},
        {'id': 2, 'name': 'Sales'},
        {'id': 3, 'name': 'Marketing'} # Marketing has no employees
    ])
    employees5 = pd.DataFrame([
        {'id': 1, 'name': 'Joe', 'salary': 80000, 'departmentId': 1},
        {'id': 2, 'name': 'Henry', 'salary': 70000, 'departmentId': 2}
    ])
    print(s(employees5, departments5))
    # Expected Output: DataFrame with (IT, Joe, 80000) and (Sales, Henry, 70000)

    # Test Case 6: All employees in one department
    print("\n--- Test Case 6: All Employees in One Department ---")
    employees6 = pd.DataFrame([
        {'id': 1, 'name': 'Will', 'salary': 60000, 'departmentId': 1},
        {'id': 2, 'name': 'Grace', 'salary': 70000, 'departmentId': 1}
    ])
    print(s(employees6, departments))
    # Expected Output: DataFrame with (IT, Grace, 70000)

    # Test Case 7: Each department has only one employee
    print("\n--- Test Case 7: Each Department has one Employee ---")
    employees7 = pd.DataFrame([
        {'id': 1, 'name': 'Zoe', 'salary': 95000, 'departmentId': 1},
        {'id': 2, 'name': 'Phil', 'salary': 85000, 'departmentId': 2}
    ])
    print(s(employees7, departments))
    # Expected Output: DataFrame with (IT, Zoe, 95000) and (Sales, Phil, 85000)

    # Test Case 8: Empty Department DataFrame
    print("\n--- Test Case 8: Empty Department DataFrame ---")
    departments8 = pd.DataFrame(columns=['id', 'name'])
    print(s(employees1, departments8)) # Using employees from Test Case 1
    # Expected Output: Empty DataFrame with columns [Department, Employee, Salary]
    
    # Test Case 9: Single employee in a single department
    print("\n--- Test Case 9: Minimal Data ---")
    employees9 = pd.DataFrame([{'id': 1, 'name': 'Eve', 'salary': 100000, 'departmentId': 1}])
    departments9 = pd.DataFrame([{'id': 1, 'name': 'Executive'}])
    print(s(employees9, departments9))
    # Expected Output: DataFrame with (Executive, Eve, 100000)

    # Test Case 10: Complex mix with ties and unique winners
    print("\n--- Test Case 10: Complex Mix ---")
    departments10 = pd.DataFrame([
        {'id': 1, 'name': 'IT'},
        {'id': 2, 'name': 'Sales'},
        {'id': 3, 'name': 'HR'}
    ])
    employees10 = pd.DataFrame([
        {'id': 1, 'name': 'IT_A', 'salary': 90000, 'departmentId': 1},
        {'id': 2, 'name': 'IT_B', 'salary': 90000, 'departmentId': 1}, # Tie in IT
        {'id': 3, 'name': 'Sales_A', 'salary': 80000, 'departmentId': 2}, # Unique winner in Sales
        {'id': 4, 'name': 'Sales_B', 'salary': 70000, 'departmentId': 2},
        {'id': 5, 'name': 'HR_A', 'salary': 75000, 'departmentId': 3} # Single employee in HR
    ])
    print(s(employees10, departments10))
    # Expected Output: DataFrame showing IT_A, IT_B, Sales_A, and HR_A with their respective salaries.

test_department_highest_salary()
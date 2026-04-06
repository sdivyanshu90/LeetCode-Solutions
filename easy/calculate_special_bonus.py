def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    eligible_employees = (employees['employee_id'] % 2 == 1) & (employees['name'].str[0] != 'M')
    employees.loc[eligible_employees, 'bonus'] = employees['salary']
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')

def test_calculate_special_bonus():
    # Test case 1
    data1 = {
        'employee_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'salary': [50000, 60000, 55000, 70000]
    }
    df1 = pd.DataFrame(data1)
    print(calculate_special_bonus(df1)) # Expected output:
    #    employee_id  bonus
    # 0            1  50000
    # 1            2      0
    # 2            3  55000
    # 3            4      0

    # Test case 2
    data2 = {
        'employee_id': [5, 6, 7, 8],
        'name': ['Megan', 'Michael', 'Molly', 'Mark'],
        'salary': [80000, 90000, 75000, 85000]
    }
    df2 = pd.DataFrame(data2)
    print(calculate_special_bonus(df2)) # Expected output:
    #    employee_id  bonus
    # 0            5      0
    # 1            6      0
    # 2            7      0
    # 3            8      0

    # Test case 3
    data3 = {
        'employee_id': [9, 10, 11, 12],
        'name': ['Anna', 'Mark', 'Mia', 'John'],
        'salary': [45000, 55000, 60000, 65000]
    }
    df3 = pd.DataFrame(data3)
    print(calculate_special_bonus(df3)) # Expected output:
    #    employee_id  bonus
    # 0            9  45000
    # 1           10      0
    # 2           11      0
    # 3           12      0

    # Test case 4
    data4 = {
        'employee_id': [13, 14, 15, 16],
        'name': ['Emily', 'Michael', 'Mia', 'John'],
        'salary': [70000, 80000, 75000, 65000]
    }
    df4 = pd.DataFrame(data4)
    print(calculate_special_bonus(df4)) # Expected output:
    #    employee_id  bonus
    # 0           13  70000
    # 1           14      0
    # 2           15      0
    # 3           16      0

    # Test case 5
    data5 = {
        'employee_id': [17, 18, 19, 20],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'salary': [50000, 60000, 55000, 70000]
    }
    df5 = pd.DataFrame(data5)
    print(calculate_special_bonus(df5)) # Expected output:
    #    employee_id  bonus
    # 0           17  50000
    # 1           18      0
    # 2           19  55000
    # 3           20      0

test_calculate_special_bonus()
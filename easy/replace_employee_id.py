import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = employees.merge(employee_uni, on='id', how='left')
    return result[['unique_id', 'name']]

def test_replace_employee_id():
    # Test case 1
    employees1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
    employee_uni1 = pd.DataFrame({'id': [1, 2, 3], 'unique_id': ['A123', 'B456', 'C789']})
    print(replace_employee_id(employees1, employee_uni1))
    # Expected output:
    #   unique_id     name
    # 0      A123    Alice
    # 1      B456      Bob
    # 2      C789  Charlie

    # Test case 2
    employees2 = pd.DataFrame({'id': [4, 5], 'name': ['David', 'Eve']})
    employee_uni2 = pd.DataFrame({'id': [4, 5], 'unique_id': ['D012', 'E345']})
    print(replace_employee_id(employees2, employee_uni2))
    # Expected output:
    #   unique_id   name
    # 0      D012  David
    # 1      E345    Eve

    # Test case 3
    employees3 = pd.DataFrame({'id': [6], 'name': ['Frank']})
    employee_uni3 = pd.DataFrame({'id': [6], 'unique_id': ['F678']})
    print(replace_employee_id(employees3, employee_uni3))
    # Expected output:
    #   unique_id   name
    # 0      F678  Frank

    # Test case 4
    employees4 = pd.DataFrame({'id': [7, 8], 'name': ['Grace', 'Heidi']})
    employee_uni4 = pd.DataFrame({'id': [7, 8], 'unique_id': ['G901', 'H234']})
    print(replace_employee_id(employees4, employee_uni4))
    # Expected output:
    #   unique_id   name
    # 0      G901  Grace
    # 1      H234  Heidi

    # Test case 5
    employees5 = pd.DataFrame({'id': [9], 'name': ['Ivan']})
    employee_uni5 = pd.DataFrame({'id': [9], 'unique_id': ['I567']})
    print(replace_employee_id(employees5, employee_uni5))
    # Expected output:
    #   unique_id  name
    # 0      I567  Ivan

test_replace_employee_id()
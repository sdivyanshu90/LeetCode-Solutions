import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].str.startswith("DIAB1") | patients["conditions"].str.contains(" DIAB1", regex=False)]

def test_find_patients():
    # Test case 1
    data1 = {
        'id': [1, 2, 3, 4, 5],
        'conditions': ['DIAB1', 'DIAB1, HYPER', 'HYPER, DIAB1', 'HYPER', 'DIAB2']
    }
    df1 = pd.DataFrame(data1)
    result1 = find_patients(df1)
    print(result1)  # Expected output:    id     conditions
                                        # 0   1         DIAB1
                                        # 1   2  DIAB1, HYPER
                                        # 2   3  HYPER, DIAB1

    # Test case 2
    data2 = {
        'id': [6, 7, 8, 9, 10],
        'conditions': ['DIAB2', 'HYPER', 'DIAB1', 'HYPER, DIAB2', 'DIAB1, HYPER']
    }
    df2 = pd.DataFrame(data2)
    result2 = find_patients(df2)
    print(result2)  # Expected output:     id     conditions
                                        # 2   8         DIAB1
                                        # 4  10  DIAB1, HYPER

test_find_patients()
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    salary_categories = {
        "Low Salary": accounts['income'] < 20000,
        "Average Salary": (accounts['income'] >= 20000) & (accounts['income'] <= 50000),
        "High Salary": accounts['income'] > 50000
    }

    count_per_category = {category: accounts[condition]['income'].count() for category, condition in salary_categories.items()}
    result = pd.DataFrame(list(count_per_category.items()), columns=['category', 'accounts_count'])    
    return result

def test_count_salary_categories():
    # Test case 1
    accounts = pd.DataFrame({
        'account_id': [1, 2, 3, 4, 5],
        'income': [15000, 25000, 30000, 60000, 10000]
    })
    print(count_salary_categories(accounts))  # Expected output:
    #       category  accounts_count
    # 0   Low Salary               2
    # 1   Average Salary           2
    # 2   High Salary              1

    # Test case 2
    accounts = pd.DataFrame({
        'account_id': [1, 2, 3, 4],
        'income': [5000, 15000, 25000, 55000]
    })
    print(count_salary_categories(accounts))  # Expected output:
    #       category  accounts_count
    # 0   Low Salary               2
    # 1   Average Salary           1
    # 2   High Salary              1

    # Test case 3
    accounts = pd.DataFrame({
        'account_id': [1, 2, 3],
        'income': [10000, 20000, 50000]
    })
    print(count_salary_categories(accounts))  # Expected output:
    #       category  accounts_count
    # 0   Low Salary               1
    # 1   Average Salary           2
    # 2   High Salary              0

    # Test case 4
    accounts = pd.DataFrame({
        'account_id': [1, 2, 3, 4, 5],
        'income': [60000, 70000, 80000, 90000, 100000]
    })
    print(count_salary_categories(accounts))  # Expected output:
    #       category  accounts_count
    # 0   Low Salary               0
    # 1   Average Salary           0
    # 2   High Salary              5

    # Test case 5
    accounts = pd.DataFrame({
        'account_id': [1, 2, 3, 4],
        'income': [15000, 15000, 15000, 15000]
    })
    print(count_salary_categories(accounts))  # Expected output:
    #       category  accounts_count
    # 0   Low Salary               4
    # 1   Average Salary           0
    # 2   High Salary              0

test_count_salary_categories()
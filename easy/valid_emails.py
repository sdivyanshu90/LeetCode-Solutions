import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    mask = users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$')
    
    valid_users = users[mask]
    
    return valid_users

def test_valid_emails():
    # Test case 1
    data1 = {
        'id': [1, 2, 3, 4, 5],
        'mail': ['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com', 'd@leetcode.com', 'e@leetcode.com']
    }
    df1 = pd.DataFrame(data1)
    result1 = valid_emails(df1)
    print(result1)  # Expected output: All rows

    # Test case 2
    data2 = {
        'id': [1, 2, 3, 4, 5],
        'mail': ['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com', 'd@leetcode.com', 'e@leetcode.com']
    }
    df2 = pd.DataFrame(data2)
    result2 = valid_emails(df2)
    print(result2)  # Expected output: All rows

test_valid_emails()
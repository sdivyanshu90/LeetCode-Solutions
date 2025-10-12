import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    if 'id' not in customers.columns or 'name' not in customers.columns:
        return pd.DataFrame({'Customers': []})

    merged_df = customers.merge(orders, how='left', left_on='id', right_on='customerId', indicator=True)
    filtered_customers = merged_df[merged_df['_merge'] == 'left_only']
    result = filtered_customers[['name']].rename(columns={'name': "Customers"})
    return result

def test_find_customers():
    s = find_customers

    # --- Test Case 1: Standard Case (Mix of customers with and without orders) ---
    print("--- Test Case 1: Standard Case ---")
    customers1 = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']})
    orders1 = pd.DataFrame({'id': [1, 2], 'customerId': [3, 1]})
    print(s(customers1, orders1))
    # Expected Output:
    #   Customers
    # 1     Henry
    # 3       Max

    # --- Test Case 2: All customers have placed at least one order ---
    print("\n--- Test Case 2: All Customers Have Orders ---")
    customers2 = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})
    orders2 = pd.DataFrame({'id': [1, 2], 'customerId': [1, 2]})
    print(s(customers2, orders2))
    # Expected Output: Empty DataFrame with column 'Customers'

    # --- Test Case 3: No customers have placed any orders ---
    print("\n--- Test Case 3: No Customers Have Orders ---")
    customers3 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Eve', 'Frank', 'Grace']})
    orders3 = pd.DataFrame(columns=['id', 'customerId'])
    print(s(customers3, orders3))
    # Expected Output:
    #   Customers
    # 0       Eve
    # 1     Frank
    # 2     Grace

    # --- Test Case 4: A customer with multiple orders ---
    print("\n--- Test Case 4: Customer With Multiple Orders ---")
    customers4 = pd.DataFrame({'id': [1, 2], 'name': ['Ivy', 'Jack']})
    orders4 = pd.DataFrame({'id': [1, 2, 3], 'customerId': [1, 1, 1]}) # Ivy has 3 orders
    print(s(customers4, orders4))
    # Expected Output:
    #   Customers
    # 1      Jack

    # --- Test Case 5: Empty customers DataFrame ---
    print("\n--- Test Case 5: Empty Customers DataFrame ---")
    customers5 = pd.DataFrame(columns=['id', 'name'])
    orders5 = pd.DataFrame({'id': [1], 'customerId': [1]})
    print(s(customers5, orders5))
    # Expected Output: Empty DataFrame with column 'Customers'

    # --- Test Case 6: Both DataFrames are empty ---
    print("\n--- Test Case 6: Both DataFrames Empty ---")
    customers6 = pd.DataFrame(columns=['id', 'name'])
    orders6 = pd.DataFrame(columns=['id', 'customerId'])
    print(s(customers6, orders6))
    # Expected Output: Empty DataFrame with column 'Customers'

    # --- Test Case 7: Orders exist, but for non-listed customers ---
    print("\n--- Test Case 7: No Overlapping Customers ---")
    customers7 = pd.DataFrame({'id': [1, 2], 'name': ['Ken', 'Leo']})
    orders7 = pd.DataFrame({'id': [1, 2], 'customerId': [3, 4]}) # Orders for customers 3 & 4
    print(s(customers7, orders7))
    # Expected Output:
    #   Customers
    # 0       Ken
    # 1       Leo

    # --- Test Case 8: Duplicate customer names (with different IDs) ---
    print("\n--- Test Case 8: Duplicate Customer Names ---")
    customers8 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Mia', 'Noah', 'Mia']})
    orders8 = pd.DataFrame({'id': [1], 'customerId': [2]}) # Only Noah has an order
    print(s(customers8, orders8))
    # Expected Output:
    #   Customers
    # 0       Mia
    # 2       Mia

    # --- Test Case 9: Single customer with no order ---
    print("\n--- Test Case 9: Single Customer, No Order ---")
    customers9 = pd.DataFrame({'id': [1], 'name': ['Omar']})
    orders9 = pd.DataFrame(columns=['id', 'customerId'])
    print(s(customers9, orders9))
    # Expected Output:
    #   Customers
    # 0      Omar

    # --- Test Case 10: Single customer with an order ---
    print("\n--- Test Case 10: Single Customer, With Order ---")
    customers10 = pd.DataFrame({'id': [1], 'name': ['Pria']})
    orders10 = pd.DataFrame({'id': [1], 'customerId': [1]})
    print(s(customers10, orders10))
    # Expected Output: Empty DataFrame with column 'Customers'

test_find_customers()
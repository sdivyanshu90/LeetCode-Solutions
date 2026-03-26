import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered_product = products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return filtered_product[['product_id']]

def test_find_products():

    # Test Case 1
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'low_fats': ['Y', 'N', 'Y', 'Y', 'N'],
        'recyclable': ['Y', 'Y', 'N', 'Y', 'N']
    }
    products = pd.DataFrame(data)
    print(find_products(products)) # Expected Output: DataFrame with product_id 1 and 4

    # Test Case 2
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'low_fats': ['N', 'N', 'N', 'N', 'N'],
        'recyclable': ['Y', 'Y', 'Y', 'Y', 'Y']
    }
    products = pd.DataFrame(data)
    print(find_products(products)) # Expected Output: Empty DataFrame

    # Test Case 3
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'low_fats': ['Y', 'Y', 'Y', 'Y', 'Y'],
        'recyclable': ['N', 'N', 'N', 'N', 'N']
    }
    products = pd.DataFrame(data)
    print(find_products(products)) # Expected Output: Empty DataFrame

    # Test Case 4
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'low_fats': ['Y', 'Y', 'Y', 'Y', 'Y'],
        'recyclable': ['Y', 'Y', 'Y', 'Y', 'Y']
    }
    products = pd.DataFrame(data)
    print(find_products(products)) # Expected Output: DataFrame with product_id 1, 2, 3, 4, 5

    # Test Case 5
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'low_fats': ['N', 'N', 'N', 'N', 'N'],
        'recyclable': ['N', 'N', 'N', 'N', 'N']
    }
    products = pd.DataFrame(data)
    print(find_products(products)) # Expected Output: Empty DataFrame

test_find_products()
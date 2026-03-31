import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melted_products = pd.melt(products, id_vars='product_id', var_name='store', value_name='price')
    rearranged_products = melted_products.dropna()
    return rearranged_products

def test_rearrange_products_table():
    # Test case 1
    products1 = pd.DataFrame({
        'product_id': [1, 2, 3],
        'store_a': [10.0, 20.0, None],
        'store_b': [None, 15.0, 25.0]
    })
    print(rearrange_products_table(products1)) # Expected output:
        #     product_id    store  price
        # 0           1  store_a   10.0
        # 1           2  store_a   20.0
        # 4           2  store_b   15.0
        # 5           3  store_b   25.0

    # Test case 2
    products2 = pd.DataFrame({
        'product_id': [1, 2],
        'store_a': [5.0, None],
        'store_b': [None, 10.0]
    })
    print(rearrange_products_table(products2)) # Expected output:
        #     product_id    store  price
        # 0           1  store_a    5.0
        # 1           2  store_b   10.0

    # Test case 3
    products3 = pd.DataFrame({
        'product_id': [1],
        'store_a': [None],
        'store_b': [None]
    })
    print(rearrange_products_table(products3)) # Expected output: Empty DataFrame with columns ['product_id', 'store', 'price']

    # Test case 4
    products4 = pd.DataFrame({
        'product_id': [1, 2, 3],
        'store_a': [10.0, 20.0, 30.0],
        'store_b': [15.0, 25.0, 35.0]
    })
    print(rearrange_products_table(products4)) # Expected output:
        #     product_id    store  price
        # 0           1  store_a   10.0
        # 1           2  store_a   20.0
        # 2           3  store_a   30.0
        # 3           1  store_b   15.0
        # 4           2  store_b   25.0
        # 5           3  store_b   35.0


    # Test case 5
    products5 = pd.DataFrame({
        'product_id': [1, 2, 3],
        'store_a': [None, None, None],
        'store_b': [None, None, None]
    })
    print(rearrange_products_table(products5)) # Expected output: Empty DataFrame with columns ['product_id', 'store', 'price']

test_rearrange_products_table()
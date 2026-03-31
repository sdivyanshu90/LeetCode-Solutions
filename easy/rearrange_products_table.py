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
    print(rearrange_products_table(products1))

    # Test case 2
    products2 = pd.DataFrame({
        'product_id': [1, 2],
        'store_a': [5.0, None],
        'store_b': [None, 10.0]
    })
    print(rearrange_products_table(products2))

    # Test case 3
    products3 = pd.DataFrame({
        'product_id': [1],
        'store_a': [None],
        'store_b': [None]
    })
    print(rearrange_products_table(products3))

    # Test case 4
    products4 = pd.DataFrame({
        'product_id': [1, 2, 3],
        'store_a': [10.0, 20.0, 30.0],
        'store_b': [15.0, 25.0, 35.0]
    })
    print(rearrange_products_table(products4))

    # Test case 5
    products5 = pd.DataFrame({
        'product_id': [1, 2, 3],
        'store_a': [None, None, None],
        'store_b': [None, None, None]
    })
    print(rearrange_products_table(products5))

test_rearrange_products_table()
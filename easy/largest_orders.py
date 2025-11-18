import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()

def test_largest_orders():
    data = {
        'order_id': [1, 2, 3, 4, 5, 6, 7, 8],
        'customer_number': [101, 102, 101, 103, 102, 101, 104, 102],
        'amount': [250, 150, 300, 200, 100, 400, 350, 150]
    }
    orders_df = pd.DataFrame(data)
    
    result_df = largest_orders(orders_df)
    print(result_df)

test_largest_orders()
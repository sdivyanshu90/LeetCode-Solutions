# Sales Person (SQL/Pandas)

## Problem Summary

Given three DataFrames (`sales_person`, `company`, `orders`), find all salespersons who did not have any orders related to the company with the name "RED".

## Current Implementation

The solution uses pandas DataFrame operations to filter out salespersons who have orders with RED company:

```python
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_sales_id = company.loc[company['name']=='RED', 'com_id']
    red_salesmen = orders.loc[orders['com_id'].isin(red_sales_id)]['sales_id'].unique()
    result = sales_person.loc[~sales_person['sales_id'].isin(red_salesmen)][['name']]
    return result
```

## How It Works

The algorithm performs a series of filtering operations:

1. **Find RED company**: `company.loc[company['name']=='RED', 'com_id']` gets the company ID for RED
2. **Find salespeople with RED orders**: Filter orders table for RED's company ID, extract unique salesperson IDs
3. **Exclude those salespeople**: Use negation (`~`) with `isin()` to find salespeople NOT in the red_salesmen list
4. **Return names only**: Select just the `name` column

**SQL equivalent**:

```sql
SELECT name
FROM sales_person
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM orders
    WHERE com_id IN (SELECT com_id FROM company WHERE name = 'RED')
)
```

## Why This Works

- **Negative filtering**: Identifies who NOT to include rather than who to include
- **isin() for membership**: Efficiently checks if values exist in another list
- **unique()**: Prevents double-counting salespeople with multiple RED orders
- **Chained filtering**: Each step narrows down the result set

## Time Complexity

O(n + m + k) where n, m, k are the sizes of sales_person, company, and orders tables respectively. Each operation (filtering, isin) is linear.

## Space Complexity

O(m) for storing intermediate results (red_sales_id and red_salesmen lists).

## Trade-offs

- **Readable**: Clear step-by-step logic easy to understand
- **Pandas idioms**: Uses standard DataFrame operations
- **Performance**: For very large datasets, SQL database queries might be more optimized
- **Alternative approach**: Could use merge/join operations instead of isin(), potentially more efficient for very large datasets

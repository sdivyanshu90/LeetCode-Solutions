# Find Customers Who Never Order — Explanation, Approach, Complexity

Problem summary

- Given two DataFrames:
  - `customers`: columns [id, name]
  - `orders`: columns [id, customerId]
- Find the names of all customers who never placed any order.
- Return a DataFrame with column name 'Customers'.

Approach (left join with indicator)

- Perform a left outer join of customers with orders on customers.id = orders.customerId.
- Use the `indicator=True` parameter to mark which rows came from the left-only (unmatched) set.
- Filter for rows where `_merge == 'left_only'` (customers with no matching orders).
- Extract the 'name' column and rename it to 'Customers'.
- Return the resulting DataFrame.

Why this works (thought process)

- A left join preserves all customers and adds order information where it exists.
- The indicator column tracks which rows have no matching orders (`left_only`).
- Filtering for `left_only` gives us customers with no orders by definition.
- This approach is intuitive and leverages pandas built-in functionality.

Time and space complexity

- Time: O(n + m) average, where n = len(customers) and m = len(orders). The join operation is typically O(n + m) on average with hash-based joins.
- Space: O(n + m) for the merged DataFrame intermediate; O(k) for the result, where k = number of customers without orders.

Implementation details and robustness

- Column validation: check that 'id' and 'name' exist in customers before processing.
- Return an empty DataFrame with the correct column name if columns are missing or no customers match.
- Handles edge cases: empty DataFrames, all customers having orders, no customers having orders.
- The left join handles duplicate customerId values naturally (one customer with many orders produces multiple rows, all filtered out if present).

Edge cases

- Empty customers DataFrame → return empty result with 'Customers' column.
- Empty orders DataFrame → return all customers (none have orders).
- All customers have orders → return empty DataFrame with 'Customers' column.
- Missing columns (id or name in customers) → return empty DataFrame as safety check.
- Duplicate order entries for the same customer → doesn't affect the result (still filtered as `left_only` → no).

Example testcases (from repository)

- customers = [(1,'Joe'), (2,'Henry'), (3,'Sam'), (4,'Max')], orders = [(3,), (1,)] → output: Henry, Max
- customers = [(1,'Alice'), (2,'Bob')], orders = [(1,), (2,)] → output: empty
- customers = [(1,'Eve'), (2,'Frank'), (3,'Grace')], orders = [] → output: Eve, Frank, Grace
- customers = [(1,'Ivy'), (2,'Jack')], orders = [(1,), (1,), (1,)] → output: Jack

Alternative approaches

- SQL-style anti-join: use `merge(..., how='left', indicator=True)` then filter (current approach).
- Set difference: customers_set - orders_set (requires extracting names, less direct).
- isin() with negation: filter(~customers['id'].isin(orders['customerId'])) → also works, slightly more concise.
- SQL query if using SQLite backend: `SELECT name FROM customers WHERE id NOT IN (SELECT DISTINCT customerId FROM orders)`.

Thought process / design choices

- The left join + indicator approach is explicit and readable.
- Alternative: use `isin()` with negation for a one-liner but merge + indicator is more standard and scalable.
- Renaming 'name' to 'Customers' matches expected output format.

Notes

- The solution is straightforward and leverages pandas idioms.
- For very large datasets, consider filtering orders first (distinct customerId) to reduce join size before merging.
- If you prefer SQL-style clarity, equivalent SQL is: `SELECT c.name FROM customers c LEFT JOIN orders o ON c.id = o.customerId WHERE o.customerId IS NULL`.

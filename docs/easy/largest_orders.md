# Customer Placing the Largest Number of Orders

Problem summary

- Given a DataFrame orders with customer orders, find the customer who placed the most orders.
- Return DataFrame with customer_number of the customer with most orders.
- If tie, return any one.

Current implementation (in repository)

- Implementation uses pandas mode() function:
  - Calls `.mode()` on customer_number column to find most frequent value.
  - Converts result to DataFrame format.
  - Returns the customer_number.
- Example code:
  ```python
  return orders['customer_number'].mode().to_frame()
  ```

Why this works

- `.mode()` finds the most frequently occurring value(s) in a series.
- For order counts, mode gives customer(s) with most orders.
- `.to_frame()` converts Series back to DataFrame format.
- Handles ties: mode() returns all values with highest frequency.

Time complexity

- Let n = number of rows.
- mode() internally counts occurrences: O(n).
- Overall time complexity: O(n).

Space complexity

- Mode calculation may create internal frequency counter: O(k) where k is unique customers.
- Result DataFrame: O(1) typically (one or few customers).
- Overall space complexity: O(k).

Thought process and trade-offs

- Pandas mode(): concise one-liner leveraging built-in statistics.
- Alternative: use value_counts() and take max - more explicit, same complexity.
- Alternative: groupby and count, then filter max - verbose but clear logic.
- Current approach: most concise for this specific problem.
- SQL equivalent: `SELECT customer_number FROM orders GROUP BY customer_number ORDER BY COUNT(*) DESC LIMIT 1`.

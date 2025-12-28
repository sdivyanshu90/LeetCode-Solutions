# Lemonade Change

Problem summary

- At lemonade stand, lemonade costs $5. Customers pay with $5, $10, or $20 bills.
- Start with no change. For each customer, provide correct change if possible.
- Return true if can provide change to all customers, false otherwise.
- Example: [5,5,5,10,20] -> True (can provide change for all).

Current implementation (in repository)

- Implementation tracks available bills:
  - Maintains counters for $5 and $10 bills.
  - For $5: accept it, increment counter.
  - For $10: give one $5 change, increment $10 counter.
  - For $20: prefer giving one $10 + one $5, otherwise three $5s.
  - Return false immediately if unable to provide change.
- Example code:
  ```python
  if customer_bill == 5:
      five_dollar_bills += 1
  elif customer_bill == 10:
      if five_dollar_bills > 0:
          five_dollar_bills -= 1
          ten_dollar_bills += 1
  else:  # 20
      if ten_dollar_bills > 0 and five_dollar_bills > 0:
          five_dollar_bills -= 1
          ten_dollar_bills -= 1
  ```

Why this works

- Simulates cash register: track bills received as change.
- $5 bills are most valuable for change (needed for both $10 and $20).
- For $20, prefer using $10+$5 to conserve $5 bills (greedy strategy).
- Early return on failure: impossible to recover if can't provide change once.

Time complexity

- Let n = number of customers.
- Process each customer once: O(1) per customer.
- Overall time complexity: O(n).

Space complexity

- Only storing two counters.
- Space complexity: O(1).

Thought process and trade-offs

- Greedy approach: prioritize conserving $5 bills for $20 transactions.
- Key insight: $5 bills are critical (needed for all change scenarios).
- For $20, using $10+$5 is better than three $5s (preserves more $5s).
- Simulation: straightforward modeling of real-world scenario.
- No backtracking needed: greedy choice is always optimal here.

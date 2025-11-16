# Climb Stairs

Problem summary

- Given n steps, you can climb either 1 or 2 steps at a time. Return the number of distinct ways to reach the top (step n).
- This is the classic Fibonacci / dynamic programming counting problem: ways(n) = ways(n-1) + ways(n-2), with base ways(0)=1, ways(1)=1.

Approach in repository

- The solution builds a small DP list that effectively computes Fibonacci numbers.
- It initializes dp = [0, 1] and appends dp[i-2] + dp[i-1] for i from 2 to n+1, then returns dp[n+1].
- This produces ways(n) = Fibonacci(n+1) which matches the required count: e.g., n=2 -> 2, n=3 -> 3.

Why this works (thought process)

- For any position k>1, any valid path to k must come from either k-1 (a 1-step) or k-2 (a 2-step). Summing those possibilities yields the recurrence.
- The recurrence is exactly the Fibonacci recurrence; computing iteratively is straightforward and avoids recursion overhead.

Time and space complexity

- Time complexity: O(n) — a single loop of length ~n, each step O(1).
- Space complexity: O(n) for the current implementation because it stores the DP list up to index n+1.
- Optimized space: O(1) is possible by keeping only the last two Fibonacci values (rolling variables), e.g.:
  - prev, curr = 1, 1
  - for \_ in range(2, n+1): prev, curr = curr, prev+curr
  - return curr (with appropriate base handling)

Edge cases

- n = 0: there is one way (do nothing) → function returns 1.
- Small inputs (n=1,2) are handled by base values.
- Very large n: algorithm is linear time; if n is huge you may prefer matrix exponentiation or fast doubling to achieve O(log n).

Alternative approaches

- Recursive with memoization: conceptually simple but uses recursion and similar complexity to iterative DP.
- Mathematical / fast doubling (Fibonacci fast doubling): O(log n) time for very large n when needed.
- Closed-form (Binet's formula): requires floating point and careful rounding; not recommended for exact integer results on large n.

Notes

- If you prefer constant extra memory, replace the DP list with two variables to track the last two counts.

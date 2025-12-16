# Fibonacci Number — Explanation, Approach, Complexity

Problem summary

- Given an integer `n`, return the n-th Fibonacci number.
- The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

Approach (iterative dynamic programming)

- Initialize a DP array `dp` of size `n + 1` to store Fibonacci numbers from 0 to n.
- Set base cases: `dp[0] = 0`, `dp[1] = 1`.
- Iteratively fill the array from index 2 to n using the recurrence: `dp[i] = dp[i-2] + dp[i-1]`.
- Return `dp[n]`.

Why this works (thought process)

- The problem is a classic dynamic programming recurrence. By storing previously computed values, we avoid redundant recalculations.
- Building bottom-up from base cases ensures each value is computed only once.
- This avoids the exponential time complexity of naive recursion.

Time and space complexity

- Time: O(n) — single loop from 2 to n, each iteration performs constant work.
- Space: O(n) — the DP array stores n+1 values.
- Optimized space: O(1) is possible by keeping only two variables (the last two Fibonacci numbers) instead of an array, e.g.,
  ```python
  if n == 0: return 0
  prev, curr = 0, 1
  for _ in range(2, n + 1):
      prev, curr = curr, prev + curr
  return curr
  ```

Edge cases

- n = 0 → return 0.
- n = 1 → return 1.
- Large n (e.g., n = 50): algorithm remains linear and produces the correct result; Python integers are arbitrary-precision.

Alternatives

- Recursive with memoization: O(n) time and O(n) space (call stack + memo). More elegant but uses recursion.
- Matrix exponentiation: O(log n) time via fast exponentiation; useful for very large n.
- Closed-form (Binet's formula): O(1) time but requires careful floating-point rounding for exact results on large n.

Example testcases (from repository)

- fib(2) = 1
- fib(3) = 2
- fib(4) = 3
- fib(5) = 5
- fib(10) = 55

Notes

- The current implementation is clear and optimal for typical problem constraints.
- If space is a critical constraint and n is large, use the two-variable optimization.
- If n is extremely large (e.g., n > 10^6), matrix exponentiation or memoized recursion with larger call stack limits may be preferable.

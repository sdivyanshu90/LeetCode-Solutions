# Arrange Coins

Problem summary

- Given n coins, you form complete staircase rows: row 1 uses 1 coin, row 2 uses 2 coins, ..., row k uses k coins.
- Return the maximum k such that 1 + 2 + ... + k ≤ n.

Key observation

- The total coins needed for k full rows is S(k) = k\*(k+1)/2 (triangular number). We need the largest k with S(k) ≤ n.

Approach used (binary search)

- Search k in range [0, n].
- At mid = (left+right)//2 compute S(mid) = mid\*(mid+1)//2.
  - If S(mid) == n → return mid (exact fit).
  - If S(mid) > n → decrease right to mid-1.
  - If S(mid) < n → increase left to mid+1.
- When loop finishes return right (largest valid k).

Why binary search

- S(k) is strictly increasing in k for k ≥ 0, so we can apply binary search to find the boundary where S(k) crosses n.
- Binary search avoids floating point errors from solving quadratic equation and is robust for large n.

Proof sketch

- S(k) monotonic ⇒ the set {k | S(k) ≤ n} is a prefix [0 .. K]. Binary search finds the greatest element of this prefix.

Time and space complexity

- Time: O(log n) — each iteration halves the search interval and each step uses O(1) arithmetic.
- Space: O(1) — only a few integer variables used.

Edge cases

- n = 0 → return 0.
- n = 1 → return 1.
- Very large n (up to 64-bit limits): use integer arithmetic to avoid overflow; Python integers are arbitrary precision so formula is safe.

Alternatives

- Direct quadratic formula: solve k^2 + k − 2n ≤ 0 and take floor of positive root k = floor((-1 + sqrt(1+8n))/2). Requires careful handling of floating-point precision for very large n.
- Iterative subtraction: O(k) and inefficient for large n.

Thought process / design choices

- Chose binary search for simplicity and exact integer arithmetic.
- Avoided floating-point root due to potential precision pitfalls.
- Returning right after the loop yields the largest k with S(k) ≤ n.

Example

- n = 5 -> rows 1 + 2 = 3 (k=2), next row needs 3 coins (3+3=6>5) → output 2.
- n = 8 -> rows 1+2+3 = 6 (k=3), next row needs 4 coins (6+4=10>8) → output 3.

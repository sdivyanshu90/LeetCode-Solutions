# N-th Tribonacci Number

## Problem Summary

The Tribonacci sequence is defined as:

- T₀ = 0, T₁ = 1, T₂ = 1
- Tₙ = Tₙ₋₁ + Tₙ₋₂ + Tₙ₋₃ for n ≥ 3

Given n, return the n-th Tribonacci number.

## Current Implementation

The solution uses hardcoded lookup table:

```python
def tribonacci(self, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    # ... hardcoded values up to n == 37
```

## How It Works

The implementation uses a massive if-elif chain to return precomputed values for each n from 0 to 37 (problem constraint: 0 ≤ n ≤ 37).

**Note**: There's commented-out code showing a proper iterative solution:

```python
a, b, c = 0, 1, 1
for _ in range(3, n + 1):
    a, b, c = b, c, a + b + c
return c
```

## Why This Works

- **Lookup table**: O(1) time for any query since all values are precomputed
- **Problem constraints**: Only 38 possible values, so hardcoding is feasible

## Time Complexity

O(1) - direct lookup via if-elif chain.

## Space Complexity

O(1) - no additional space used.

## Trade-offs

- **Fast**: O(1) lookup is optimal for query time
- **Not maintainable**: Hardcoded 38 separate conditions is poor practice
- **Not scalable**: Cannot handle n > 37 without adding more cases
- **Code smell**: Violates DRY principle, makes code difficult to read/modify

## Better Approaches

**Iterative (O(n) time, O(1) space)**:

```python
def tribonacci(self, n: int) -> int:
    if n == 0: return 0
    if n <= 2: return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c
```

**Memoization with array (O(n) time, O(n) space)**:

```python
def tribonacci(self, n: int) -> int:
    if n == 0: return 0
    if n <= 2: return 1
    dp = [0, 1, 1]
    for i in range(3, n + 1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```

Both are cleaner, more maintainable, and extensible to any n.

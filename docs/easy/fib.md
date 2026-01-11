# Fibonacci Number

## Problem Summary

Given an integer `n`, return the n-th Fibonacci number.

The Fibonacci sequence is defined as: `F(0) = 0`, `F(1) = 1`, and `F(n) = F(n-1) + F(n-2)` for n > 1.

## Approach: Dynamic Programming (Implemented)

### Strategy

The solution uses iterative dynamic programming to build Fibonacci numbers bottom-up:

1. Initialize a DP array `dp` of size `n + 1` to store Fibonacci numbers from 0 to n
2. Set base cases: `dp[0] = 0`, `dp[1] = 1`
3. Iteratively fill the array from index 2 to n using the recurrence: `dp[i] = dp[i-2] + dp[i-1]`
4. Return `dp[n]`

### How It Works

**Example**: n = 5

```
Initialize: dp = [0, 1] (base cases)

i=2: dp[2] = dp[0] + dp[1] = 0 + 1 = 1
     dp = [0, 1, 1]

i=3: dp[3] = dp[1] + dp[2] = 1 + 1 = 2
     dp = [0, 1, 1, 2]

i=4: dp[4] = dp[2] + dp[3] = 1 + 2 = 3
     dp = [0, 1, 1, 2, 3]

i=5: dp[5] = dp[3] + dp[4] = 2 + 3 = 5
     dp = [0, 1, 1, 2, 3, 5]

Return dp[5] = 5 ✓
```

**Sequence**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

**Edge cases**:

- n = 0 → returns 0
- n = 1 → returns 1
- Large n (e.g., n = 50): Algorithm remains linear and produces correct result (Python integers are arbitrary-precision)

### Why Dynamic Programming Works

- **Optimal substructure**: F(n) can be computed from smaller subproblems F(n-1) and F(n-2)
- **Avoids redundant calculations**: By storing previously computed values, we avoid the exponential time complexity of naive recursion
- **Bottom-up approach**: Building from base cases ensures each value is computed only once
- **Classic DP problem**: Fibonacci is one of the fundamental examples of dynamic programming

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single loop from 2 to n
  - Each iteration performs constant work
- **Space Complexity**: O(n)
  - DP array stores n+1 values
  - Can be optimized to O(1) by keeping only two variables

### Advantages

- **Clear and straightforward**: Direct translation of recurrence relation
- **Efficient**: Linear time complexity
- **Handles large n**: Python's arbitrary-precision integers work for any n
- **Easy to debug**: Can inspect intermediate values in DP array

### Disadvantages

- **Uses O(n) space**: Not space-optimal
- **Could be more efficient**: O(1) space and O(log n) time solutions exist

## Alternative Approach 1: Space-Optimized DP (O(1) Space)

Keep only the last two Fibonacci numbers:

```python
def fib(self, n: int) -> int:
    if n == 0:
        return 0

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

### How It Works

- Instead of storing entire array, track only `prev` and `curr`
- Roll forward: update `prev = curr`, `curr = prev + curr`
- Same recurrence, but constant space

### Complexity

- **Time**: O(n) - same as array approach
- **Space**: O(1) - only two variables

### Advantages

- **Space efficient**: Constant extra space
- **Same time complexity**: No performance degradation
- **Cleaner**: Fewer variables to manage

### Disadvantages

- **Less intuitive**: May be harder to understand initially

## Alternative Approach 2: Matrix Exponentiation (O(log n))

For very large n, use matrix exponentiation:

```python
def fib(self, n: int) -> int:
    def matrix_mult(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def matrix_pow(M, p):
        if p == 1:
            return M
        if p % 2 == 0:
            half = matrix_pow(M, p // 2)
            return matrix_mult(half, half)
        return matrix_mult(M, matrix_pow(M, p - 1))

    if n == 0:
        return 0
    if n == 1:
        return 1

    M = [[1, 1], [1, 0]]
    result = matrix_pow(M, n)
    return result[0][1]
```

### Complexity

- **Time**: O(log n) - binary exponentiation
- **Space**: O(log n) - recursion depth

### Advantages

- **Fastest for very large n**: Logarithmic time
- **Mathematically elegant**: Uses properties of Fibonacci matrix

### Disadvantages

- **Complex**: Much more code and harder to understand
- **Overkill**: Not necessary for typical constraints

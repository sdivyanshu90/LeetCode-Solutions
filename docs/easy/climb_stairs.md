# Climbing Stairs

## Problem Summary

Given `n` steps, you can climb either 1 or 2 steps at a time. Return the number of distinct ways to reach the top (step n).

This is the classic Fibonacci / dynamic programming counting problem: `ways(n) = ways(n-1) + ways(n-2)`, with base cases `ways(0)=1`, `ways(1)=1`.

## Approach: Dynamic Programming (Implemented)

### Strategy

The solution builds a DP list that effectively computes Fibonacci numbers:

1. Initialize `dp = [0, 1]` to handle base cases
2. For each step from 2 to n+1, append `dp[i-2] + dp[i-1]`
3. Return `dp[n+1]` which contains the count for n steps

This produces `ways(n) = Fibonacci(n+1)` which matches the required count (e.g., n=2 → 2, n=3 → 3).

### How It Works

**Recurrence relation**: For any position k > 1, any valid path to k must come from either:

- Position k-1 (taking a 1-step)
- Position k-2 (taking a 2-step)

Summing these possibilities yields the recurrence: `ways(k) = ways(k-1) + ways(k-2)`

**Example**: n = 4

```
Initial: dp = [0, 1]

i=2: dp.append(0 + 1) → dp = [0, 1, 1]
i=3: dp.append(1 + 1) → dp = [0, 1, 1, 2]
i=4: dp.append(1 + 2) → dp = [0, 1, 1, 2, 3]
i=5: dp.append(2 + 3) → dp = [0, 1, 1, 2, 3, 5]

Return dp[5] = 5 ways to climb 4 steps
```

**The 5 ways to climb 4 steps**:

1. 1+1+1+1
2. 1+1+2
3. 1+2+1
4. 2+1+1
5. 2+2

**Edge cases**:

- n=0: Returns 1 (one way: do nothing)
- n=1: Returns 1 (one way: single 1-step)
- n=2: Returns 2 (two ways: 1+1 or 2)

### Why Dynamic Programming Works

- **Optimal substructure**: The solution to problem n depends on solutions to smaller problems (n-1 and n-2)
- **No redundant computation**: Each subproblem is solved exactly once and stored
- **Fibonacci recurrence**: The climbing stairs problem has the same recurrence as Fibonacci numbers
- **Bottom-up approach**: Building from base cases ensures all dependencies are satisfied

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single loop of length ~n
  - Each iteration performs O(1) work
- **Space Complexity**: O(n)
  - Stores DP list up to index n+1
  - Can be optimized to O(1) by keeping only last two values

### Advantages

- **Straightforward**: Clear iterative implementation
- **No recursion overhead**: Avoids stack space and function call overhead
- **Easy to understand**: Direct translation of recurrence relation
- **Handles all cases**: Works correctly for all non-negative n

### Disadvantages

- **Uses O(n) space**: Current implementation stores entire DP array
- **Could be optimized**: Only need last two values, not entire array
- **Not optimal for very large n**: Better algorithms exist (matrix exponentiation, closed form)

## Alternative Approach 1: Space-Optimized DP (O(1) Space)

Use only two variables to track last two Fibonacci values:

```python
def climbStairs(self, n: int) -> int:
    if n <= 1:
        return 1

    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

### How It Works

- Keep only `prev` and `curr` to track the last two counts
- Roll forward by updating: `prev = curr`, `curr = prev + curr`
- Same recurrence, but constant space

### Complexity

- **Time**: O(n) - same as DP array approach
- **Space**: O(1) - only two variables

### Advantages

- **Space efficient**: Only uses constant extra space
- **Same time complexity**: No performance loss
- **Cleaner**: Fewer variables to manage

### Disadvantages

- **Less obvious**: May be less intuitive than full DP array

## Alternative Approach 2: Matrix Exponentiation (O(log n))

For very large n, use matrix exponentiation to compute Fibonacci in O(log n):

```python
def climbStairs(self, n: int) -> int:
    def matrix_mult(A, B):
        return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

    def matrix_pow(M, p):
        if p == 1:
            return M
        if p % 2 == 0:
            half = matrix_pow(M, p // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(M, matrix_pow(M, p - 1))

    if n <= 1:
        return 1

    M = [[1, 1], [1, 0]]
    result = matrix_pow(M, n)
    return result[0][0]
```

### Complexity

- **Time**: O(log n) - binary exponentiation
- **Space**: O(log n) - recursion depth

### Advantages

- **Fastest for large n**: Logarithmic time complexity
- **Mathematically elegant**: Uses properties of Fibonacci

### Disadvantages

- **Complex**: Much more code and harder to understand
- **Overkill**: Not necessary for typical LeetCode constraints

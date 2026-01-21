# Sqrt(x)

## Problem Summary

Given a non-negative integer `x`, return the square root of `x` **rounded down to the nearest integer**. The returned integer should also be non-negative.

You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

**LeetCode Problem**: [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

**LeetCode Problem**: [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

## Approach: Binary Search (Implemented)

### Strategy

The solution uses binary search to solve the problem efficiently.

```python
def mySqrt(self, x: int) -> int:
    if x == 0:
        return 0

    left, right = 1, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        if mid <= x // mid:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### How It Works

**Example 1**: `x = 8`

```
Find largest integer k where k² ≤ 8

Initial: left=1, right=8, result=0

Iteration 1:
  mid = 1 + (8-1)//2 = 4
  4 <= 8//4? → 4 <= 2? No
  right = 4 - 1 = 3

Iteration 2:
  mid = 1 + (3-1)//2 = 2
  2 <= 8//2? → 2 <= 4? Yes
  result = 2
  left = 2 + 1 = 3

Iteration 3:
  mid = 3 + (3-3)//2 = 3
  3 <= 8//3? → 3 <= 2? No
  right = 3 - 1 = 2

left > right, exit loop
Return result = 2 ✓
```

**Example 2**: `x = 4`

```
Find k where k² ≤ 4

Initial: left=1, right=4, result=0

Iteration 1:
  mid = 1 + (4-1)//2 = 2
  2 <= 4//2? → 2 <= 2? Yes
  result = 2
  left = 3

Iteration 2:
  mid = 3 + (4-3)//2 = 3
  3 <= 4//3? → 3 <= 1? No
  right = 2

left > right, exit loop
Return result = 2 ✓
```

### Why Binary Search Works

The binary search approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: - Natural fit for "find value in range" - Avoids multiplication overflow **Why use `mid <= x // mid` instead of `mid * mid <= x`?** - Multiplication: mid\*mid could overflow for large mid - Division: x // mid is always safe in integer math - Equivalent: mid ≤ x/mid ⟺ mid² ≤ x **Why Newton's method?** - Even faster theoretically - Natural mathematical approach - But more iterations due to integer rounding The binary search approach is the standard, reliable solution for this problem!
- **Space Complexity**: O(1)

### Advantages

- Efficient binary search solution
- Clear and maintainable code

### Disadvantages

- May require additional space

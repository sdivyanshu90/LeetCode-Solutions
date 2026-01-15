# Power of Three

## Problem Summary

Given an integer `n`, return `true` if it is a power of three (i.e., if there exists an integer `x` such that `n == 3^x`). Otherwise, return `false`.

**LeetCode Problem**: [326. Power of Three](https://leetcode.com/problems/power-of-three/)

**LeetCode Problem**: [Power of Three](https://leetcode.com/problems/power-of-three/)

## Approach: Stack (Implemented)

### Strategy

The solution uses stack to solve the problem efficiently.

```python
def isPowerOfThree(self, n: int) -> bool:
    return n > 0 and 1162261467 % n == 0
```

### How It Works

Since 3 is a prime number, the only divisors of 3^19 are powers of 3:

- Divisors of 3¹⁹: 3⁰, 3¹, 3², 3³, ..., 3¹⁹
- Any other number will not divide 3¹⁹ evenly

### Why Stack Works

The stack approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient stack solution
- Clear and maintainable code

### Disadvantages

- May require additional space

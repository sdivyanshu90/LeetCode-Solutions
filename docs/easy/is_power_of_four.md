# Power of Four

## Problem Summary

Given an integer `n`, return `true` if it is a power of four (i.e., if there exists an integer `x` such that `n == 4^x`). Otherwise, return `false`.

**LeetCode Problem**: [342. Power of Four](https://leetcode.com/problems/power-of-four/)

**LeetCode Problem**: [Power of Four](https://leetcode.com/problems/power-of-four/)

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
def isPowerOfFour(self, n: int) -> bool:
    if n < 1:
        return False

    while n > 1:
        if n % 4 != 0:
            return False
        n //= 4
    return True
```

### How It Works

- For `n = 16`: 16 → 4 → 1 (all divisible by 4) ✓
- For `n = 8`: 8 → 2 (not divisible by 4) ✗
- For `n = 1`: Already 1, which is 4⁰ = 1 ✓

### Why Iteration Works

Powers of 4 are powers of 2 where the exponent is even:

- 4⁰ = 2⁰ = 1 (bit at position 0)
- 4¹ = 2² = 4 (bit at position 2)
- 4² = 2⁴ = 16 (bit at position 4)
- 4³ = 2⁶ = 64 (bit at position 6)

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space

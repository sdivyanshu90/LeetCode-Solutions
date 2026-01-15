# Power of Two

## Problem Summary

Given an integer `n`, return `true` if it is a power of two (i.e., if there exists an integer `x` such that `n == 2^x`). Otherwise, return `false`.

**LeetCode Problem**: [231. Power of Two](https://leetcode.com/problems/power-of-two/)

**LeetCode Problem**: [Power of Two](https://leetcode.com/problems/power-of-two/)

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

```python
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False

    return (n & (n - 1)) == 0
```

### How It Works

Powers of 2 have **exactly one bit set** in their binary representation:

- 1 = 2⁰ = `0b1`
- 2 = 2¹ = `0b10`
- 4 = 2² = `0b100`
- 8 = 2³ = `0b1000`
- 16 = 2⁴ = `0b10000`

The trick: When you subtract 1 from a power of 2, all bits after the single set bit become 1:

- 8 = `0b1000`, 7 = `0b0111`
- 16 = `0b10000`, 15 = `0b01111`
- 32 = `0b100000`, 31 = `0b011111`

The AND operation `n & (n-1)` will be 0 **only** if n is a power of 2:

```
    1000  (8)          10000  (16)
  & 0111  (7)        & 01111  (15)
  ------             -------
    0000  ✓            00000  ✓

    1001  (9)          01010  (10)
  & 1000  (8)        & 01001  (9)
  ------             -------
    1000  ✗            01000  ✗
```

### Why Hash Map Works

For a power of 2 (single bit set):

- `n` has one bit as 1, rest as 0
- `n - 1` flips that bit to 0 and all lower bits to 1
- `n & (n - 1)` has no overlapping 1 bits → result is 0

For non-powers of 2 (multiple bits set):

- `n` has multiple bits as 1
- `n - 1` flips the rightmost 1 to 0 and sets lower bits to 1
- `n & (n - 1)` still has some 1 bits from the higher positions → result is non-zero

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space

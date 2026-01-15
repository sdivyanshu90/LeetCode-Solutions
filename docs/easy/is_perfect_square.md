# Valid Perfect Square

## Problem Summary

Given a positive integer `num`, determine if it is a perfect square (i.e., if there exists an integer `x` such that `x * x == num`). Return `true` if `num` is a perfect square, `false` otherwise.

**LeetCode Problem**: [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

**LeetCode Problem**: [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

## Approach: Binary Search (Implemented)

### Strategy

The solution uses binary search to solve the problem efficiently.

```python
def isPerfectSquare(self, num: int) -> bool:
    ans = int(num ** 0.5)
    return ans * ans == num
```

### How It Works

- For `num = 16`: `int(16 ** 0.5) = 4`, and `4 * 4 = 16` ✓
- For `num = 14`: `int(14 ** 0.5) = 3`, and `3 * 3 = 9 ≠ 14` ✗
- The truncation via `int()` ensures we only check the integer part

### Why Binary Search Works

The binary search approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient binary search solution
- Clear and maintainable code

### Disadvantages

- May require additional space

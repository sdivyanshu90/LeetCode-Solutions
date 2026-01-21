# Missing Number

## Problem Summary

Given an array `nums` containing `n` distinct numbers taken from the range `[0, n]`, return the only number in the range that is missing from the array.

**LeetCode Problem**: [268. Missing Number](https://leetcode.com/problems/missing-number/)

**Follow-up**: Could you do it in a single pass with O(1) extra space?

**LeetCode Problem**: [Missing Number](https://leetcode.com/problems/missing-number/)

## Approach: Sorting (Implemented)

### Strategy

The solution uses sorting to solve the problem efficiently.

```python
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    total = n * (n + 1) // 2
    sum_of_nums = sum(nums)
    return total - sum_of_nums
```

### How It Works

**Example 1**: `nums = [3,0,1]`

```
n = 3
Expected sum of [0,1,2,3] = 3 * 4 / 2 = 6
Actual sum of [3,0,1] = 4
Missing number = 6 - 4 = 2
```

**Example 2**: `nums = [0,1]`

```
n = 2
Expected sum of [0,1,2] = 2 * 3 / 2 = 3
Actual sum of [0,1] = 1
Missing number = 3 - 1 = 2
```

**Example 3**: `nums = [9,6,4,2,3,5,7,0,1]`

```
n = 9
Expected sum of [0..9] = 9 * 10 / 2 = 45
Actual sum = 9+6+4+2+3+5+7+0+1 = 37
Missing number = 45 - 37 = 8
```

### Why Sorting Works

The formula `n * (n + 1) / 2` gives the sum of all integers from 0 to n.

**Derivation**:

```
Sum = 0 + 1 + 2 + ... + n
    = n * (n + 1) / 2  (Gauss's formula)

If we remove one number x:
Sum_of_array = (Sum of 0..n) - x

Therefore:
x = (Sum of 0..n) - Sum_of_array
```

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient sorting solution
- Clear and maintainable code

### Disadvantages

- May require additional space

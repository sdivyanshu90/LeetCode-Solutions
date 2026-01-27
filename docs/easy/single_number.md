# Single Number

## Problem Summary

Given a non-empty array of integers `nums`, every element appears **twice except for one element which appears once**. Find that single element.

You must implement a solution with a linear runtime complexity O(n) and use only O(1) extra space.

**LeetCode Problem**: [136. Single Number](https://leetcode.com/problems/single-number/)

**LeetCode Problem**: [Single Number](https://leetcode.com/problems/single-number/)

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

```python
def singleNumber(self, nums: List[int]) -> int:
    num_count = {}

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count == 1:
            return num
```

### How It Works

**Example 1**: `nums = [2, 2, 1]`

```
Dictionary building:
  num=2: num_count = {2: 1}
  num=2: num_count = {2: 2}
  num=1: num_count = {2: 2, 1: 1}

Finding single number:
  (2, 2): count != 1, skip
  (1, 1): count == 1, return 1 ✓
```

**Example 2**: `nums = [4, 1, 2, 1, 2]`

```
Dictionary building:
  num=4: num_count = {4: 1}
  num=1: num_count = {4: 1, 1: 1}
  num=2: num_count = {4: 1, 1: 1, 2: 1}
  num=1: num_count = {4: 1, 1: 2, 2: 1}
  num=2: num_count = {4: 1, 1: 2, 2: 2}

Finding single number:
  (4, 1): count == 1, return 4 ✓
```

**Example 3**: `nums = [-1, -1, -2]`

```
Dictionary building:
  num=-1: num_count = {-1: 1}
  num=-1: num_count = {-1: 2}
  num=-2: num_count = {-1: 2, -2: 1}

Finding single number:
  (-1, 2): count != 1, skip
  (-2, 1): count == 1, return -2 ✓
```

### Why Hash Map Works

The hash map approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n) and use only O(1) extra space. **LeetCode Problem**: [136. Single Number](https://leetcode.com/problems/single-number/)
- **Space Complexity**: as dict**: O(n) - **Not as elegant as XOR**: Doesn't meet O(1) space requirement

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space

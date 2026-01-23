# Plus One

## Problem Summary

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i`-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

**LeetCode Problem**: [66. Plus One](https://leetcode.com/problems/plus-one/)

**LeetCode Problem**: [Plus One](https://leetcode.com/problems/plus-one/)

## Approach: Stack (Implemented)

### Strategy

The solution uses stack to solve the problem efficiently.

```python
def plusOne(self, digits: List[int]) -> List[int]:
    if digits[-1] <= 8:
        digits[-1] += 1
        return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1] = self.plusOne(digits[0:-1])
        return digits
```

### How It Works

**Example 1**: `digits = [1,2,3]`

```
Call plusOne([1,2,3])
  Last digit = 3 ≤ 8
  Increment: 3 + 1 = 4
  Return [1,2,4] ✓
```

**Example 2**: `digits = [1,2,9]`

```
Call plusOne([1,2,9])
  Last digit = 9 > 8
  Set last to 0: [1,2,0]
  Recurse on [1,2]:
    Call plusOne([1,2])
      Last digit = 2 ≤ 8
      Increment: 2 + 1 = 3
      Return [1,3]
  Replace first part: [1,3,0]
  Return [1,3,0] ✓
```

**Example 3**: `digits = [9,9,9]`

```
Call plusOne([9,9,9])
  Last digit = 9 > 8
  Set last to 0: [9,9,0]
  Recurse on [9,9]:
    Call plusOne([9,9])
      Last digit = 9 > 8
      Set last to 0: [9,0]
      Recurse on [9]:
        Call plusOne([9])
          Length = 1 and digit = 9
          Return [1,0]
      Replace: [1,0,0]
      Return [1,0,0]
  Replace: [1,0,0,0]
  Return [1,0,0,0] ✓
```

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

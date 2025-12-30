# Sort Array By Parity

## Problem Summary

Given an integer array `nums`, return an array where all even integers come before all odd integers. The relative order within even and odd groups doesn't matter.

**Example**: `[3,1,2,4]` → `[2,4,3,1]` or any arrangement with evens first

## Current Implementation

The solution uses list comprehension to separate and concatenate even and odd numbers:

```python
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 != 0]
```

## How It Works

The algorithm performs two passes and concatenation:

1. **First comprehension**: Extract all even numbers (`num % 2 == 0`)
2. **Second comprehension**: Extract all odd numbers (`num % 2 != 0`)
3. **Concatenate**: Join even list with odd list using `+`

**Example** for `[3,1,2,4]`:

```
Even numbers: [2, 4]
Odd numbers: [3, 1]
Result: [2, 4, 3, 1]
```

## Why This Works

- **Partitioning**: Separates elements based on parity
- **Preservation**: Maintains relative order within each group
- **Concatenation**: Places all evens before odds by construction

## Time Complexity

O(n) where n is array length. Two passes through the array (one for evens, one for odds).

## Space Complexity

O(n) for creating the new result array with two intermediate lists.

## Trade-offs

- **Readable**: Very clear and concise logic
- **Pythonic**: Idiomatic use of list comprehensions
- **Two passes**: Scans array twice (once for evens, once for odds)
- **Extra space**: Creates new arrays rather than in-place modification
- **Alternative O(1) space**: Two-pointer in-place swap approach:
  ```python
  i, j = 0, len(nums) - 1
  while i < j:
      if nums[i] % 2 > nums[j] % 2:
          nums[i], nums[j] = nums[j], nums[i]
      if nums[i] % 2 == 0: i += 1
      if nums[j] % 2 == 1: j -= 1
  return nums
  ```
  This modifies array in-place but is more complex.

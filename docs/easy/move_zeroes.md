# Move Zeroes

## Problem Summary

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the **relative order** of the non-zero elements.

**Note**: You must do this **in-place** without making a copy of the array.

**LeetCode Problem**: [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

**LeetCode Problem**: [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
```

### How It Works

**Example 1**: `nums = [0, 1, 0, 3, 12]`

```
Initial:      [0, 1, 0, 3, 12]
              i=0 j=0

j=0: nums[0]=0, skip
              [0, 1, 0, 3, 12]
              i=0 j=1

j=1: nums[1]=1 (non-zero)
  - Swap nums[0] and nums[1]
  - i becomes 1
              [1, 0, 0, 3, 12]
              i=1 j=2

j=2: nums[2]=0, skip
              [1, 0, 0, 3, 12]
              i=1 j=3

j=3: nums[3]=3 (non-zero)
  - Swap nums[1] and nums[3]
  - i becomes 2
              [1, 3, 0, 0, 12]
              i=2 j=4

j=4: nums[4]=12 (non-zero)
  - Swap nums[2] and nums[4]
  - i becomes 3
              [1, 3, 12, 0, 0]
              i=3

Final result: [1, 3, 12, 0, 0] ✓
```

**Example 2**: `nums = [0, 0, 0, 1, 2]`

```
Initial:      [0, 0, 0, 1, 2]
              i=0 j=0

j=0: nums[0]=0, skip
j=1: nums[1]=0, skip
j=2: nums[2]=0, skip

j=3: nums[3]=1 (non-zero)
  - Swap nums[0] and nums[3]
              [1, 0, 0, 0, 2]
              i=1

j=4: nums[4]=2 (non-zero)
  - Swap nums[1] and nums[4]
              [1, 2, 0, 0, 0]
              i=2

Final result: [1, 2, 0, 0, 0] ✓
```

### Why Two Pointers Works

**Key insight**: Pointer `i` always points to the position where the next non-zero element should be placed.

When we find a non-zero element at position `j`:

- If `i == j`: Elements already in correct position (no swap needed but still swaps - no harm)
- If `i < j`: There are zeroes between position `i` and `j`, so we swap to move non-zero forward

**Maintains relative order**: Non-zero elements are processed left-to-right, so their relative order is preserved.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space

# Remove Duplicates from Sorted Array

## Problem Summary

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
- The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**LeetCode Problem**: [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**LeetCode Problem**: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    for n in range(1, len(nums)):
        if nums[n] != nums[n - 1]:
            nums[i] = nums[n]
            i += 1
    return i
```

### How It Works

**Example 1**: `nums = [1,1,2]`

```
Initial:  [1, 1, 2]
          i=1, n=1

n=1: nums[1]=1, nums[0]=1
  1 == 1, skip

n=2: nums[2]=2, nums[1]=1
  2 != 1, found unique
  nums[1] = 2
  i = 2
  Result: [1, 2, 2]

Return i=2
First 2 elements: [1, 2] ✓
```

**Example 2**: `nums = [0,0,1,1,1,2,2,3,3,4]`

```
Initial:  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
          i=1

n=1: 0 == 0, skip
n=2: 1 != 0, nums[1]=1, i=2 → [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
n=3: 1 == 1, skip
n=4: 1 == 1, skip
n=5: 2 != 1, nums[2]=2, i=3 → [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
n=6: 2 == 2, skip
n=7: 3 != 2, nums[3]=3, i=4 → [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
n=8: 3 == 3, skip
n=9: 4 != 3, nums[4]=4, i=5 → [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]

Return i=5
First 5 elements: [0, 1, 2, 3, 4] ✓
```

### Why Two Pointers Works

**Key insight**: Since array is sorted, duplicates are adjacent.

- Pointer `i` always points to the next position for a unique element
- We only copy when we find a new value (nums[n] != nums[n-1])
- Elements after index `i` don't matter
- The comparison `nums[n] != nums[n-1]` catches each new unique value

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space

# Merge Sorted Array

## Problem Summary

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored **inside the array** `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**LeetCode Problem**: [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

**LeetCode Problem**: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

## Approach: Sorting (Implemented)

### Strategy

The solution uses sorting to solve the problem efficiently.

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m + n - 1  # Position to fill in nums1
    j, k = m - 1, n - 1  # Last elements of nums1 and nums2

    while j >= 0 and k >= 0:
        if nums1[j] > nums2[k]:
            nums1[i] = nums1[j]
            i -= 1
            j -= 1
        else:
            nums1[i] = nums2[k]
            i -= 1
            k -= 1

    # Copy remaining elements from nums2 if any
    while k >= 0:
        nums1[i] = nums2[k]
        i -= 1
        k -= 1
```

### How It Works

**Example**: `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`

```
Initial state:
nums1: [1, 2, 3, 0, 0, 0]
        j=2        i=5
nums2: [2, 5, 6]
        k=2

Step 1: Compare nums1[2]=3 vs nums2[2]=6
  - 6 > 3, place 6 at position 5
  nums1: [1, 2, 3, 0, 0, 6]
          j=2     i=4
  nums2: [2, 5, 6]
          k=1

Step 2: Compare nums1[2]=3 vs nums2[1]=5
  - 5 > 3, place 5 at position 4
  nums1: [1, 2, 3, 0, 5, 6]
          j=2  i=3
  nums2: [2, 5, 6]
          k=0

Step 3: Compare nums1[2]=3 vs nums2[0]=2
  - 3 > 2, place 3 at position 3
  nums1: [1, 2, 3, 3, 5, 6]
          j=1  i=2
  nums2: [2, 5, 6]
          k=0

Step 4: Compare nums1[1]=2 vs nums2[0]=2
  - 2 ≤ 2, place 2 (from nums2) at position 2
  nums1: [1, 2, 2, 3, 5, 6]
          j=1  i=1
  nums2: [2, 5, 6]
          k=-1

Step 5: k < 0, exit while loop
Result: [1, 2, 2, 3, 5, 6]
```

### Why Sorting Works

The sorting approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient sorting solution
- Clear and maintainable code

### Disadvantages

- May require additional space

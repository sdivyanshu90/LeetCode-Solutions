# Smallest Range I

## Problem Summary

Given an array `nums` and an integer `k`, you can change each element by adding any value in the range `[-k, k]`. Return the minimum possible difference between the maximum and minimum values in the modified array.

## Current Implementation

The solution uses a mathematical formula to determine the minimum achievable range:

```python
def smallestRangeI(self, nums: List[int], k: int) -> int:
    return max(0, max(nums) - min(nums) - 2*k)
```

## How It Works

**Key insight**: To minimize the range, we want to:

- Decrease the maximum element by as much as possible (subtract `k`)
- Increase the minimum element by as much as possible (add `k`)

The new range becomes:

- New max = `max(nums) - k`
- New min = `min(nums) + k`
- New difference = `(max(nums) - k) - (min(nums) + k)` = `max(nums) - min(nums) - 2k`

If this value is negative (we can overlap the ranges), return 0 (all elements can be made equal).

**Example 1**: `nums = [0,10]`, `k = 2`

- Original range: 10 - 0 = 10
- Modified: (10-2) - (0+2) = 8 - 2 = 6

**Example 2**: `nums = [1,3,6]`, `k = 3`

- Original range: 6 - 1 = 5
- Modified: (6-3) - (1+3) = 3 - 4 = -1 → return 0 (can make all equal)

## Why This Works

- **Optimal strategy**: The best we can do is move extremes toward each other
- **Mathematical simplification**: Formula directly computes the result
- **Zero lower bound**: Range cannot be negative (elements overlap)

## Time Complexity

O(n) for finding max and min of the array (assuming `max()` and `min()` scan the array).

## Space Complexity

O(1) - only uses constant extra space for computation.

## Trade-offs

- **Elegant**: One-line formula-based solution
- **Efficient**: Single pass to find max/min
- **Optimal**: Both time and space complexity are optimal
- **No iteration needed**: Mathematical insight eliminates need for element-by-element processing

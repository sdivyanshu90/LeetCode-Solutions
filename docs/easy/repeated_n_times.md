# N-Repeated Element in Size 2N Array

## Problem Summary

Given an integer array `nums` of size `2n` where there are `n+1` unique elements and exactly one element appears `n` times, return the element that is repeated `n` times.

**Example**: `[1,2,3,3]` → `3` (appears 2 times in array of size 4)

## Current Implementation

The solution uses a frequency counter and returns early once any element is seen more than once:

```python
def repeatedNTimes(self, nums: List[int]) -> int:
    freq = defaultdict(int)
    for i in range(len(nums)):
        freq[nums[i]] = freq[nums[i]] + 1
        if freq[nums[i]] > 1:
            return nums[i]
```

## How It Works

The algorithm leverages the constraint that only one element repeats:

1. Iterate through the array, counting occurrences in a hash map
2. As soon as any element's count exceeds 1, return it immediately
3. No need to scan entire array since we're guaranteed exactly one repeated element

**Example**: `nums = [2,1,2,5,3,2]`

```
i=0: freq={2:1}, count≤1, continue
i=1: freq={2:1, 1:1}, count≤1, continue
i=2: freq={2:2, 1:1}, count>1, return 2
```

## Why This Works

- **Problem guarantee**: Exactly one element appears n times, all others appear once
- **Early termination**: First element to appear twice must be the n-repeated element
- **Hash map efficiency**: O(1) lookup and increment per element

## Time Complexity

Average case: O(n) where n is the array length. Worst case also O(n) if repeated element is at end, but typically finds answer much earlier.

## Space Complexity

O(n) for the frequency hash map in worst case, though typically much less due to early return.

## Trade-offs

- **Early return optimization**: Exits as soon as answer found (doesn't scan full array)
- **Space usage**: Uses O(n) space for simplicity
- **Alternative O(1) space approach**: Could use randomized sampling or compare elements at specific positions (e.g., `nums[i]` vs `nums[i+1]` or `nums[i+2]`), exploiting the pigeonhole principle that in 2n elements with n copies of one element, duplicates must appear within distance 3

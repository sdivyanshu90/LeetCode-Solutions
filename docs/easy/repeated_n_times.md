# N-Repeated Element in Size 2N Array

## Problem Summary

Given an integer array `nums` of size `2n` where there are `n+1` unique elements and exactly one element appears `n` times, return the element that is repeated `n` times.

**Example**: `[1,2,3,3]` → `3` (appears 2 times in array of size 4)

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

```python
def repeatedNTimes(self, nums: List[int]) -> int:
    freq = defaultdict(int)
    for i in range(len(nums)):
        freq[nums[i]] = freq[nums[i]] + 1
        if freq[nums[i]] > 1:
            return nums[i]
```

### How It Works

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

### Why Hash Map Works

- **Problem guarantee**: Exactly one element appears n times, all others appear once
- **Early termination**: First element to appear twice must be the n-repeated element
- **Hash map efficiency**: O(1) lookup and increment per element

### Complexity Analysis

- **Time Complexity**: Average case: O(n) where n is the array length. Worst case also O(n) if repeated element is at end, but typically finds answer much earlier.
- **Space Complexity**: O(n) for the frequency hash map in worst case, though typically much less due to early return.

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space

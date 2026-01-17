# Majority Element

## Problem Summary

Given an array `nums` of size `n`, return the **majority element**. The majority element is the element that appears **more than ⌊n/2⌋ times**. You may assume that the majority element always exists in the array.

**LeetCode Problem**: [169. Majority Element](https://leetcode.com/problems/majority-element/)

**LeetCode Problem**: [Majority Element](https://leetcode.com/problems/majority-element/)

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

```python
def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    H = defaultdict(int)
    for i in range(n):
        H[nums[i]] += 1

        if H[nums[i]] > n / 2:
            return nums[i]
```

### How It Works

**Example**: `nums = [2, 2, 1, 1, 1, 2, 2]`

```
n = 7, threshold = 7/2 = 3.5

Index 0: nums[0]=2
  - H = {2: 1}
  - 1 > 3.5? No

Index 1: nums[1]=2
  - H = {2: 2}
  - 2 > 3.5? No

Index 2: nums[2]=1
  - H = {2: 2, 1: 1}
  - 1 > 3.5? No

Index 3: nums[3]=1
  - H = {2: 2, 1: 2}
  - 2 > 3.5? No

Index 4: nums[4]=1
  - H = {2: 2, 1: 3}
  - 3 > 3.5? No

Index 5: nums[5]=2
  - H = {2: 3, 1: 3}
  - 3 > 3.5? No

Index 6: nums[6]=2
  - H = {2: 4, 1: 3}
  - 4 > 3.5? Yes!
  - Return 2
```

### Why Hash Map Works

- If majority element appears > n/2 times, it occupies > n/2 positions
- In a sorted array, these positions must include the middle index
- Example with n=7: Element appears ≥4 times, so it spans the middle

### Complexity Analysis

- **Time Complexity**: O(n) - Best space complexity: O(1) - No sorting required - No hash map required - Elegant algorithm
- **Space Complexity**: O(1) - No sorting required - No hash map required - Elegant algorithm

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space

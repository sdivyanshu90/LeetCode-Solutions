# Relative Sort Array

## Problem Summary

Given two arrays `arr1` and `arr2`, sort `arr1` such that elements appearing in `arr2` come first in the order of `arr2`, followed by remaining elements in ascending order.

**Example**: `arr1=[2,3,1,3,2,4,6,7,9,2,19]`, `arr2=[2,1,4,3,9,6]` → `[2,2,2,1,4,3,3,9,6,7,19]`

## Current Implementation

The solution uses counting sort with custom ordering:

```python
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    max_element = max(arr1)
    count = [0] * (max_element + 1)

    for element in arr1:
        count[element] += 1

    result = []
    for value in arr2:
        while count[value] > 0:
            result.append(value)
            count[value] -= 1

    for num in range(max_element + 1):
        while count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result
```

## How It Works

The algorithm uses counting sort in two phases:

1. **Count frequencies**: Build frequency array for all elements in arr1
2. **Phase 1 - arr2 order**:
   - For each value in arr2 (in order)
   - Append it to result as many times as it appears in arr1
   - Decrement its count to zero
3. **Phase 2 - remaining elements**:
   - Iterate through frequency array in ascending order
   - Append any remaining elements (not in arr2)

**Example** for `arr1=[2,3,1,3,2]`, `arr2=[2,1]`:

```
Count: [0,1,2,2] (indices: 0→0, 1→1, 2→2, 3→2)

Phase 1 (arr2 order):
  value=2: append 2,2 → result=[2,2], count[2]=0
  value=1: append 1 → result=[2,2,1], count[1]=0

Phase 2 (ascending order of remaining):
  num=3: append 3,3 → result=[2,2,1,3,3]

Result: [2,2,1,3,3]
```

## Why This Works

- **Counting sort**: Efficiently handles range-constrained integers
- **Custom order**: First phase imposes arr2's order
- **Stable completion**: Second phase adds remaining elements in natural order
- **No sorting needed**: O(n) counting instead of O(n log n) comparison sort

## Time Complexity

O(n + m + k) where n = len(arr1), m = len(arr2), k = max(arr1). All linear operations.

## Space Complexity

O(k) for the counting array where k = max(arr1).

## Trade-offs

- **Efficient for small ranges**: Works well when max(arr1) is reasonable
- **No comparison sort**: Faster than general sorting for this problem
- **Space constraint**: If max(arr1) is very large, counting array becomes impractical
- **Alternative approach**: Use custom comparator with sorting:
  ```python
  rank = {v: i for i, v in enumerate(arr2)}
  return sorted(arr1, key=lambda x: (rank.get(x, len(arr2)), x))
  ```
  More general (handles large values) but O(n log n) time.

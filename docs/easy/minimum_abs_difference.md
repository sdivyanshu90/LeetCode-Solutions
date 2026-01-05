# Minimum Absolute Difference

## Problem Summary

Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference. Return the pairs in ascending order.

**Example**: `[4,2,1,3]` → `[[1,2],[2,3],[3,4]]` (min difference is 1)

## Current Implementation

The solution sorts the array and finds the minimum difference in a single pass:

```python
def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    min_diff = float("inf")

    res = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
            res = [[arr[i-1], arr[i]]]
        elif diff == min_diff:
            res.append([arr[i- 1], arr[i]])
    return res
```

## How It Works

The algorithm leverages sorting to efficiently find minimum differences:

1. **Sort the array**: After sorting, elements with minimum difference must be adjacent
2. **Track minimum**: Initialize `min_diff` to infinity
3. **Single pass**:
   - Compare each adjacent pair
   - If difference is smaller: update `min_diff`, reset result list
   - If difference equals current minimum: append to result list
4. **Return** all pairs with minimum difference

**Key insight**: In a sorted array, the minimum absolute difference between any two elements must be between adjacent elements.

**Example** for `[4,2,1,3]`:

```
After sort: [1,2,3,4]

i=1: diff=2-1=1, min_diff=inf → min_diff=1, res=[[1,2]]
i=2: diff=3-2=1, min_diff=1 → append, res=[[1,2],[2,3]]
i=3: diff=4-3=1, min_diff=1 → append, res=[[1,2],[2,3],[3,4]]

Result: [[1,2],[2,3],[3,4]]
```

**Example** for `[3,8,-10,23,19,17]`:

```
After sort: [-10,3,8,17,19,23]

i=1: diff=3-(-10)=13 → min_diff=13, res=[[-10,3]]
i=2: diff=8-3=5 → min_diff=5, res=[[3,8]]
i=3: diff=17-8=9 → no change
i=4: diff=19-17=2 → min_diff=2, res=[[17,19]]
i=5: diff=23-19=4 → no change

Result: [[17,19]]
```

## Why This Works

- **Sorted property**: Minimum difference must be between adjacent elements
- **Single scan**: After sorting, one pass finds all optimal pairs
- **Dynamic tracking**: Updates result when finding smaller differences
- **Accumulation**: Collects all pairs that tie for minimum

## Time Complexity

O(n log n) where n is the array length. Sorting dominates at O(n log n), and the scan is O(n).

## Space Complexity

O(1) auxiliary space if we don't count the output list. The sort is typically O(log n) for recursion stack (or O(1) for in-place sorts like heapsort).

## Trade-offs

- **Optimal approach**: Cannot avoid sorting since we need adjacent comparisons
- **Efficient**: Single pass after sorting
- **Clean logic**: Maintains only pairs with current minimum
- **Alternative (less efficient)**: Compute all O(n²) pairwise differences, find minimum, filter → O(n²) time and space

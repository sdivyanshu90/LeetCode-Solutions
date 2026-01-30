# Sort Array By Parity

## Problem Summary

Given an integer array `nums`, return an array where all even integers come before all odd integers. The relative order within even and odd groups doesn't matter.

**Example**: `[3,1,2,4]` → `[2,4,3,1]` or any arrangement with evens first

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 != 0]
```

### How It Works

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

### Why Two Pointers Works

- **Partitioning**: Separates elements based on parity
- **Preservation**: Maintains relative order within each group
- **Concatenation**: Places all evens before odds by construction

### Complexity Analysis

- **Time Complexity**: O(n) where n is array length. Two passes through the array (one for evens, one for odds).
- **Space Complexity**: O(n) for creating the new result array with two intermediate lists.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space

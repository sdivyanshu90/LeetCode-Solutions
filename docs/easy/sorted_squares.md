# Squares of a Sorted Array

## Problem Summary

Given a sorted integer array `nums` (in non-decreasing order), return an array of the squares of each number, also sorted in non-decreasing order.

**Example**: `[-4,-1,0,3,10]` → `[0,1,9,16,100]`

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    position = len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        position -= 1
    return result
```

### How It Works

**Key insight**: In a sorted array, the largest absolute values (and thus largest squares) are at the extremes (far left negative or far right positive).

The algorithm fills the result array from right to left (largest to smallest):

1. Start with pointers at both ends
2. Compare squares at left and right positions
3. Place the larger square at the current position (from right)
4. Move the pointer that contributed the larger square
5. Repeat until all elements processed

**Example** for `[-4,-1,0,3,10]`:

```
Initial: left=0(-4), right=4(10), position=4
16 vs 100: place 100 at position 4, right→3 → result=[0,0,0,0,100]
16 vs 9: place 16 at position 3, left→1 → result=[0,0,0,16,100]
1 vs 9: place 9 at position 2, right→2 → result=[0,0,9,16,100]
1 vs 0: place 1 at position 1, left→2 → result=[0,1,9,16,100]
0: place 0 at position 0 → result=[0,1,9,16,100]
```

### Why Two Pointers Works

- **Sorted input property**: Largest absolute values at extremes
- **Fill from largest**: Avoids needing to sort after squaring
- **Single pass**: Each element examined exactly once
- **No extra sorting**: O(n) instead of O(n log n)

### Complexity Analysis

- **Time Complexity**: O(n) where n is the array length. Single pass through the array.
- **Space Complexity**: O(n) for the result array. O(1) auxiliary space if we don't count the output.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space

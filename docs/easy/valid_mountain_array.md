# Valid Mountain Array

## Problem Summary

Given an integer array `arr`, return `true` if it's a valid mountain array. A mountain array has:

- At least 3 elements
- An index `i` (peak) where:
  - `arr[0] < arr[1] < ... < arr[i]` (strictly increasing)
  - `arr[i] > arr[i+1] > ... > arr[n-1]` (strictly decreasing)

**Example**: `[0,3,2,1]` → `true`, `[3,5,5]` → `false` (plateau)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
def validMountainArray(self, arr: List[int]) -> bool:
    n = len(arr)
    left = 0
    right = n - 1
    while left < n - 1 and arr[left] < arr[left + 1]:
        left += 1

    while right > 0 and arr[right - 1] > arr[right]:
        right -= 1

    if left > 0 and left == right and right < n - 1:
        return True
    else:
        return False
```

### How It Works

The algorithm climbs the mountain from both sides:

1. **Left climb**: Move `left` pointer up while strictly increasing
2. **Right climb**: Move `right` pointer up while strictly decreasing
3. **Valid mountain check**:
   - `left > 0`: Must have ascending slope (not start at peak)
   - `left == right`: Both pointers meet at same peak
   - `right < n - 1`: Must have descending slope (not end at peak)

**Example** for `[0,3,2,1]`:

```
Left climb: 0→1 (0<3), stop at index 1
Right climb: 3→2→1 (1<2<3), stop at index 1
left=1, right=1: left>0 ✓, left==right ✓, right<3 ✓ → True
```

**Example** for `[3,5,5]` (plateau):

```
Left climb: 0→1 (3<5), stop at index 1 (5 not < 5)
Right climb: 2→1 (5 not > 5), stop at index 2
left=1, right=2: left==right ✗ → False
```

### Why Two Pointers Works

- **Two-pointer convergence**: Valid mountain has both sides meeting at unique peak
- **Strict inequality**: Prevents plateaus (flat sections)
- **Boundary checks**: Ensure both ascending and descending sections exist
- **Single pass**: Each pointer scans at most n elements

### Complexity Analysis

- **Time Complexity**: O(n) where n is the array length. Each pointer traverses the array at most once.
- **Space Complexity**: O(1) - only uses two pointer variables.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space

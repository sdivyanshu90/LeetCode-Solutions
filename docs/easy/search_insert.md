# Search Insert Position

## Problem Summary

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**LeetCode Problem**: [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

## Approach: Binary Search (Implemented)

### Strategy

The implemented solution uses **binary search** to achieve O(log n) complexity:

1. Initialize `left = 0` and `right = len(nums) - 1`
2. While `left <= right`:
   - Calculate `mid = (left + right) // 2`
   - If `nums[mid]` equals target, return `mid`
   - If `nums[mid]` is less than target, search right half: `left = mid + 1`
   - If `nums[mid]` is greater than target, search left half: `right = mid - 1`
3. When loop exits, `left` points to the insertion position

**Code**:

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            left = m + 1
        else:
            right = m - 1
    return left
```

### How It Works

**Key insight**: After binary search completes, `left` always points to the correct insertion position.

**Example 1**: Target found - `nums = [1,3,5,6]`, `target = 5`

```
Initial: left=0, right=3, target=5

Iteration 1:
  mid = (0 + 3) // 2 = 1
  nums[1] = 3
  3 < 5? Yes
  left = 1 + 1 = 2

Iteration 2:
  mid = (2 + 3) // 2 = 2
  nums[2] = 5
  5 == 5? Yes
  Return 2 ✓
```

**Example 2**: Target not found, insert at end - `nums = [1,3,5,6]`, `target = 7`

```
Initial: left=0, right=3, target=7

Iteration 1:
  mid = (0 + 3) // 2 = 1
  nums[1] = 3
  3 < 7? Yes
  left = 1 + 1 = 2

Iteration 2:
  mid = (2 + 3) // 2 = 2
  nums[2] = 5
  5 < 7? Yes
  left = 2 + 1 = 3

Iteration 3:
  mid = (3 + 3) // 2 = 3
  nums[3] = 6
  6 < 7? Yes
  left = 3 + 1 = 4

Loop condition: left <= right → 4 <= 3? No
Exit loop

Return left = 4 ✓
(Insert at position 4 after 6)
```

**Example 3**: Target not found, insert at beginning - `nums = [1,3,5,6]`, `target = 0`

```
Initial: left=0, right=3, target=0

Iteration 1:
  mid = (0 + 3) // 2 = 1
  nums[1] = 3
  3 < 0? No, 3 > 0? Yes
  right = 1 - 1 = 0

Iteration 2:
  mid = (0 + 0) // 2 = 0
  nums[0] = 1
  1 < 0? No, 1 > 0? Yes
  right = 0 - 1 = -1

Loop condition: left <= right → 0 <= -1? No
Exit loop

Return left = 0 ✓
(Insert at position 0 before 1)
```

**Example 4**: Target in middle - `nums = [1,3,5,6]`, `target = 2`

```
Initial: left=0, right=3, target=2

Iteration 1:
  mid = (0 + 3) // 2 = 1
  nums[1] = 3
  3 < 2? No, 3 > 2? Yes
  right = 1 - 1 = 0

Iteration 2:
  mid = (0 + 0) // 2 = 0
  nums[0] = 1
  1 < 2? Yes
  left = 0 + 1 = 1

Loop condition: left <= right → 1 <= 0? No
Exit loop

Return left = 1 ✓
(Insert between 1 and 3)
```

### Why `left` is the Answer

**Invariant maintained**:

- All elements at indices < `left` are < `target`
- All elements at indices > `right` are >= `target`

**When loop exits** (`left > right`):

- `left` points to the first position where we should insert

**Visual representation**:

```
Array: [1, 3, 5, 6], target = 2

Step 1: left=0, right=3
  mid=1: nums[1]=3 > 2
  right=0

  Invariant: elements > target are at indices > 0

Step 2: left=0, right=0
  mid=0: nums[0]=1 < 2
  left=1

  Invariant: elements < target are at indices < 1
             elements > target are at indices > 0

Step 3: left=1, right=0
  left > right, exit

  left=1 is the position to insert 2
```

### Complexity Analysis

- **Time Complexity**: O(log n)
  - Binary search halves the search space each iteration
  - Maximum iterations = log₂(n)
  - n = length of array
- **Space Complexity**: O(1)
  - Only using two pointers (`left`, `right`)
  - No additional data structures

### Advantages

- **Optimal time complexity**: O(log n) is required by problem
- **Simple implementation**: Classic binary search pattern
- **No extra space**: O(1) space complexity
- **Handles all cases**: Found, insert at beginning, middle, end

### Disadvantages

- **Must be sorted**: Input must be sorted (problem guarantee)
- **Requires careful boundaries**: Off-by-one errors common

## Alternative: Leftmost Binary Search Template

Using the leftmost search template:

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    if not nums:
        return 0

    left = 0
    right = len(nums) - 1

    # Find leftmost position where nums[i] >= target
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

### How It Works

This variant searches for the leftmost position >= target.

**Example**: `nums = [1,3,5,6]`, `target = 5`

```
left=0, right=3

Iteration 1:
  mid=1, nums[1]=3 < 5
  left = 2

Iteration 2:
  mid = (2+3)//2 = 2
  nums[2]=5 >= 5
  right = 2

left == right, exit

Return 2 ✓
```

### Complexity

- **Time**: O(log n)
- **Space**: O(1)

### Advantages

- **Clean invariant**: Always finds position >= target
- **Simpler condition**: Just one comparison

### Disadvantages

- **Different termination**: `left < right` instead of `left <= right`
- **Less intuitive**: Requires understanding leftmost search

## Comparison of Approaches

| Approach                             | Time     | Space | Difficulty | Pros                                  | Cons                          |
| ------------------------------------ | -------- | ----- | ---------- | ------------------------------------- | ----------------------------- |
| Standard Binary Search (Implemented) | O(log n) | O(1)  | Easy       | Clear, finds exact or insertion point | Requires care with boundaries |
| Leftmost Binary Search               | O(log n) | O(1)  | Medium     | Clean invariant, elegant              | Less intuitive template       |
| Linear Search (Non-optimal)          | O(n)     | O(1)  | Easy       | Simple                                | Violates O(log n) requirement |

**Winner**: Standard binary search (implemented) - most straightforward

## Edge Cases & Considerations

1. **Empty array**:

   - `nums = []`, `target = 5` → `0`
   - Insert at position 0 ✓

2. **Single element, found**:

   - `nums = [1]`, `target = 1` → `0`
   - Return exact match ✓

3. **Single element, not found (larger)**:

   - `nums = [1]`, `target = 2` → `1`
   - Insert after the element ✓

4. **Single element, not found (smaller)**:

   - `nums = [1]`, `target = 0` → `0`
   - Insert before the element ✓

5. **Target at beginning**:

   - `nums = [1,3,5]`, `target = 1` → `0`
   - Match at first position ✓

6. **Target at end**:

   - `nums = [1,3,5]`, `target = 5` → `2`
   - Match at last position ✓

7. **Insert at beginning**:

   - `nums = [1,3,5]`, `target = 0` → `0`
   - Insert before all elements ✓

8. **Insert at end**:

   - `nums = [1,3,5]`, `target = 7` → `3`
   - Insert after all elements ✓

9. **Insert in middle**:

   - `nums = [1,3,5]`, `target = 2` → `1`
   - Insert between elements ✓

10. **Large array**:

    - `nums = [0,1,2,...,999]`, `target = 500` → `500`
    - Still O(log n) ✓

11. **Duplicates not tested**:
    - Problem: array contains distinct integers
    - No duplicate handling needed

## Common Pitfalls

1. **Wrong return value when not found**:

   ```python
   # WRONG: Returns -1 for not found
   def searchInsert(self, nums, target):
       # ... binary search ...
       return -1  # Wrong! Should return insertion position

   # CORRECT: Return left (insertion position)
   return left
   ```

2. **Incorrect mid calculation (overflow)**:

   ```python
   # WRONG: Can overflow in some languages
   m = (left + right) // 2
   # Actually fine in Python, but in Java/C++:
   m = left + (right - left) // 2  # Safer

   # This is a non-issue in Python
   ```

3. **Wrong loop condition**:

   ```python
   # WRONG: Using < instead of <=
   while left < right:  # Will miss exact matches
       # ...

   # CORRECT: Use <=
   while left <= right:
       if nums[m] == target:
           return m
   ```

4. **Off-by-one in pointer updates**:

   ```python
   # WRONG: Not updating correctly
   if nums[m] < target:
       left = m  # Should be m + 1

   # CORRECT: Update correctly
   if nums[m] < target:
       left = m + 1
   else:
       right = m - 1
   ```

5. **Returning wrong value**:

   ```python
   # WRONG: Returning right or mid
   if not found:
       return right  # Wrong position

   # CORRECT: Return left
   return left
   ```

6. **Negative indices**:

   ```python
   # WRONG: Returning negative
   return right  # Can be -1

   # CORRECT: left is always >= 0
   return left
   ```

## Optimization Notes

The implemented solution is **already optimal**:

- **Time**: O(log n) - required by problem
- **Space**: O(1) - cannot use less

**Interview tips**:

- Recognize this as a binary search problem
- Explain the invariant clearly
- Walk through an example step-by-step
- Discuss why `left` is the correct answer

**Key insight for interviews**:

```
After binary search fails to find target:
- left points to first element > target
- right points to last element < target
- left == right + 1 always
- left is the insertion position
```

**Performance analysis**:

```
Array size: 1,000,000
Linear search: ~500,000 comparisons
Binary search: ~20 comparisons

Massive difference!
```

## Visual Example

```
Array: [1, 3, 5, 6], target = 2

Binary Search Tree (visualization):

        1  3  5  6  target=2
            |
          m=1: nums[1]=3
        3 > 2, go left

      1  3 | 5  6
      |
    m=0: nums[0]=1
  1 < 2, go right

      1 | 3 | 5  6
         left position here

Return left = 1 ✓


Array: [1, 3, 5, 6], target = 7

        1  3  5  6  target=7
            |
          m=1: nums[1]=3
        3 < 7, go right

      1  3 | 5  6 |
              |
            m=2: nums[2]=5
          5 < 7, go right

      1  3 | 5 | 6 |
                |
              m=3: nums[3]=6
            6 < 7, go right

      1  3 | 5 | 6 | (left past end)
                    |
                  Return left = 4 ✓
```

## Test Cases

```python
# Target found
searchInsert([1,3,5,6], 5)          # 2

# Target not found, insert at end
searchInsert([1,3,5,6], 7)          # 4

# Target not found, insert at beginning
searchInsert([1,3,5,6], 0)          # 0

# Target not found, insert in middle
searchInsert([1,3,5,6], 2)          # 1
searchInsert([1,3,5,6], 4)          # 2
searchInsert([1,3,5,6], 6)          # 3

# Single element, found
searchInsert([1], 1)                # 0

# Single element, not found (larger)
searchInsert([1], 3)                # 1

# Single element, not found (smaller)
searchInsert([1], 0)                # 0

# Empty array
searchInsert([], 5)                 # 0

# Large array
searchInsert(list(range(1000)), 500)      # 500
searchInsert(list(range(1000)), 1001)     # 1000
searchInsert(list(range(1, 1001)), 0)     # 0

# Two elements
searchInsert([1, 3], 1)             # 0
searchInsert([1, 3], 2)             # 1
searchInsert([1, 3], 3)             # 1
searchInsert([1, 3], 4)             # 2
```

## Thought Process

**Problem analysis**:

- Sorted array, find target or insertion position
- Must be O(log n) - rules out linear search
- Binary search is the only O(log n) option

**Key observations**:

1. Array is sorted - perfect for binary search
2. Need to handle both found and not found cases
3. Insertion position is determined after search fails
4. `left` pointer naturally points to insertion position

**Algorithm insight**:

```
Binary search maintains invariant:
- Elements at indices < left are all < target
- Elements at indices > right are all >= target

When search ends (left > right):
- left is the first position where target could go
- This is the insertion position!
```

**Why this works**:

- If target found: return its index
- If target not found: left points to where it should go
  - All elements before left are < target
  - All elements from left onward are >= target
  - So left is exactly where to insert

**Optimal approach**:

- Binary search achieves O(log n) requirement
- Standard implementation is clean and reliable
- Handle all cases naturally through algorithm logic

**Interview strategy**:

1. Recognize O(log n) requirement means binary search
2. Implement standard binary search
3. Explain why `left` is insertion position
4. Walk through example with insertion needed
5. Discuss time/space complexity

This problem is a fundamental application of binary search, testing:

- Understanding of binary search algorithm
- Handling search variants (found vs not found)
- Pointer management in loops
- Recognition of O(log n) requirements

## Related Problems

- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [704. Binary Search](https://leetcode.com/problems/binary-search/)
- [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

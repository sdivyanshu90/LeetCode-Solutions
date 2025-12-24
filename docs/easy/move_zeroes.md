# Move Zeroes

## Problem Summary

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the **relative order** of the non-zero elements.

**Note**: You must do this **in-place** without making a copy of the array.

**LeetCode Problem**: [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## Approach 1: Two-Pointer Swap (Implemented)

### Strategy

The implemented solution uses a **two-pointer approach with swapping**:

1. Use pointer `i` to track the position where the next non-zero element should go
2. Use pointer `j` to scan through the array
3. When a non-zero element is found, swap it with the element at position `i`
4. Increment `i` to prepare for the next non-zero element
5. All zeroes will naturally accumulate at the end

**Code**:

```python
def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
```

### How It Works

**Example 1**: `nums = [0, 1, 0, 3, 12]`

```
Initial:      [0, 1, 0, 3, 12]
              i=0 j=0

j=0: nums[0]=0, skip
              [0, 1, 0, 3, 12]
              i=0 j=1

j=1: nums[1]=1 (non-zero)
  - Swap nums[0] and nums[1]
  - i becomes 1
              [1, 0, 0, 3, 12]
              i=1 j=2

j=2: nums[2]=0, skip
              [1, 0, 0, 3, 12]
              i=1 j=3

j=3: nums[3]=3 (non-zero)
  - Swap nums[1] and nums[3]
  - i becomes 2
              [1, 3, 0, 0, 12]
              i=2 j=4

j=4: nums[4]=12 (non-zero)
  - Swap nums[2] and nums[4]
  - i becomes 3
              [1, 3, 12, 0, 0]
              i=3

Final result: [1, 3, 12, 0, 0] ✓
```

**Example 2**: `nums = [0, 0, 0, 1, 2]`

```
Initial:      [0, 0, 0, 1, 2]
              i=0 j=0

j=0: nums[0]=0, skip
j=1: nums[1]=0, skip
j=2: nums[2]=0, skip

j=3: nums[3]=1 (non-zero)
  - Swap nums[0] and nums[3]
              [1, 0, 0, 0, 2]
              i=1

j=4: nums[4]=2 (non-zero)
  - Swap nums[1] and nums[4]
              [1, 2, 0, 0, 0]
              i=2

Final result: [1, 2, 0, 0, 0] ✓
```

### Why This Works

**Key insight**: Pointer `i` always points to the position where the next non-zero element should be placed.

When we find a non-zero element at position `j`:

- If `i == j`: Elements already in correct position (no swap needed but still swaps - no harm)
- If `i < j`: There are zeroes between position `i` and `j`, so we swap to move non-zero forward

**Maintains relative order**: Non-zero elements are processed left-to-right, so their relative order is preserved.

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass through the array with pointer j
  - Each element examined exactly once
  - Swaps are O(1)
- **Space Complexity**: O(1)
  - In-place modification, no extra space needed
  - Only two pointers used

### Edge Cases Handled

1. **All zeroes**: `nums = [0,0,0,0]` → No non-zero to swap, stays same
2. **No zeroes**: `nums = [1,2,3,4,5]` → No swaps needed, stays same
3. **Zeroes already at end**: `nums = [1,9,8,0,0]` → No swaps, stays same
4. **Empty array**: `nums = []` → No iterations, stays empty
5. **Single element**: Works for both zero and non-zero
6. **Negative numbers**: Treated as non-zero, moved forward

## Approach 2: Optimized Two-Pointer (No Unnecessary Swaps)

Only swap when necessary (when `i < j`):

```python
def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
```

### Advantages

- Avoids unnecessary swaps when `i == j`
- Faster for arrays with few zeroes
- Same time complexity, better practical performance

### Example

```
nums = [1, 2, 3, 0, 0]

j=0: nums[0]=1 (non-zero), i=0, i==j so no swap, i=1
j=1: nums[1]=2 (non-zero), i=1, i==j so no swap, i=2
j=2: nums[2]=3 (non-zero), i=2, i==j so no swap, i=3
j=3: nums[3]=0, skip
j=4: nums[4]=0, skip

Result: [1, 2, 3, 0, 0] (no swaps occurred)
```

### Complexity

- **Time**: O(n) - same as before
- **Space**: O(1)

## Approach 3: Shift Elements (Alternative)

Instead of swapping, shift and place zeros at end:

```python
def moveZeroes(self, nums: List[int]) -> None:
    # Count non-zero elements
    non_zero_count = sum(1 for num in nums if num != 0)

    # Collect non-zero elements
    non_zeros = [num for num in nums if num != 0]

    # Place non-zero elements at beginning
    for i in range(non_zero_count):
        nums[i] = non_zeros[i]

    # Fill remaining with zeros
    for i in range(non_zero_count, len(nums)):
        nums[i] = 0
```

### Analysis

- **Time**: O(n) - Multiple passes
- **Space**: O(n) - Extra space for non_zeros list
- **Not truly in-place** due to extra space
- **More readable** but less efficient

## Approach 4: Remove and Append

Simple approach using list operations:

```python
def moveZeroes(self, nums: List[int]) -> None:
    zero_count = 0

    # Remove zeros and count them
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            zero_count += 1
        else:
            i += 1

    # Append zeros at the end
    nums.extend([0] * zero_count)
```

### Analysis

- **Time**: O(n²) - pop is O(n) operation, done up to n times
- **Space**: O(n) - For appended zeros
- **Simple logic** but inefficient
- **Not optimal** - violates O(1) space in practical sense

## Comparison of Approaches

| Approach                       | Time  | Space | In-Place | Pros                 | Cons                  |
| ------------------------------ | ----- | ----- | -------- | -------------------- | --------------------- |
| Two-Pointer Swap (Implemented) | O(n)  | O(1)  | Yes      | Simple, optimal      | Unnecessary swaps     |
| Optimized Two-Pointer          | O(n)  | O(1)  | Yes      | Optimal, fewer swaps | Slightly more complex |
| Shift Elements                 | O(n)  | O(n)  | No       | Clean logic          | Extra space           |
| Remove and Append              | O(n²) | O(n)  | No       | Very simple          | Inefficient           |

**Winner**: Optimized Two-Pointer approach - O(n) time, O(1) space, minimal swaps

## Edge Cases & Considerations

1. **All zeros**:

   - `nums = [0,0,0,0]` → `[0,0,0,0]`
   - No non-zero to move, array stays the same

2. **No zeros**:

   - `nums = [1,2,3,4,5]` → `[1,2,3,4,5]`
   - No elements to move

3. **Zeros already at end**:

   - `nums = [1,9,8,0,0]` → `[1,9,8,0,0]`
   - No swaps needed (or no unnecessary swaps with optimized version)

4. **Zeros at beginning**:

   - `nums = [0,0,0,1,2]` → `[1,2,0,0,0]`
   - Requires full pass to move all non-zeros forward

5. **Empty array**:

   - `nums = []` → `[]`
   - No iterations, returns immediately

6. **Single element**:

   - `nums = [0]` → `[0]`
   - `nums = [42]` → `[42]`
   - Handles correctly

7. **Alternating zeros and non-zeros**:

   - `nums = [0,1,0,2,0,3]` → `[1,2,3,0,0,0]`
   - Relative order maintained

8. **Negative numbers**:

   - `nums = [-1,0,-3,5,0,0,8]` → `[-1,-3,5,8,0,0,0]`
   - Negative numbers treated as non-zero

9. **Large array with few zeros**:

   - Optimized version shines (fewer swaps)
   - Basic version still O(n)

10. **Large array with many zeros**:
    - All versions maintain O(n) time
    - Only space differs

## Common Pitfalls

1. **Creating a new array** (violates in-place requirement):

   ```python
   # WRONG: Not in-place
   def moveZeroes(self, nums):
       non_zeros = [x for x in nums if x != 0]
       return non_zeros + [0] * (len(nums) - len(non_zeros))

   # CORRECT: Modify nums in-place
   # Swap or shift elements within nums
   ```

2. **Using list.remove()** (O(n²) complexity):

   ```python
   # WRONG: O(n²) due to remove
   while 0 in nums:
       nums.remove(0)
       nums.append(0)

   # CORRECT: Two-pointer approach O(n)
   i = 0
   for j in range(len(nums)):
       if nums[j] != 0:
           nums[i], nums[j] = nums[j], nums[i]
           i += 1
   ```

3. **Modifying array while iterating with single pointer**:

   ```python
   # WRONG: Index issues when modifying
   for i in range(len(nums)):
       if nums[i] == 0:
           nums.pop(i)
           nums.append(0)

   # CORRECT: Two pointers for simultaneous iteration and modification
   j = 0
   for i in range(len(nums)):
       if nums[i] != 0:
           nums[j], nums[i] = nums[i], nums[j]
           j += 1
   ```

4. **Breaking relative order**:

   ```python
   # WRONG: Could break relative order if not careful
   # Two-pointer approach with left-to-right processing maintains it

   # CORRECT: Process elements left-to-right
   i = 0
   for j in range(len(nums)):
       if nums[j] != 0:
           nums[i], nums[j] = nums[j], nums[i]
           i += 1
   ```

5. **Returning the array** (when supposed to modify in-place):
   ```python
   # The problem says "Do not return anything"
   # But some solutions return nums anyway
   # Both work in LeetCode, but in-place is preferred
   ```

## Optimization Notes

The two-pointer approach is **optimal** for this problem:

- **Time**: O(n) - Can't do better, must examine all elements
- **Space**: O(1) - In-place modification achieves minimum possible

**Why two-pointer is best**:

- Single pass through array
- Constant extra space
- Maintains relative order naturally
- Handles all edge cases

**Optimization trick**: Check `if i != j` before swapping (Approach 2)

- Avoids unnecessary swaps
- Faster for arrays with few zeroes
- Same asymptotic complexity, better practical performance

## Visual Example

```
Original:     [0, 1, 0, 3, 12]

After j=0:    [0, 1, 0, 3, 12]  (skip zero)
              i=0

After j=1:    [1, 0, 0, 3, 12]  (swap with 1)
              i=1

After j=2:    [1, 0, 0, 3, 12]  (skip zero)
              i=1

After j=3:    [1, 3, 0, 0, 12]  (swap with 3)
              i=2

After j=4:    [1, 3, 12, 0, 0]  (swap with 12)
              i=3

Result:       [1, 3, 12, 0, 0] ✓


Another example: [0, 0, 0, 1, 2]

After j=0-2:  [0, 0, 0, 1, 2]   (skip zeros)
              i=0

After j=3:    [1, 0, 0, 0, 2]   (swap 1 with 0 at i=0)
              i=1

After j=4:    [1, 2, 0, 0, 0]   (swap 2 with 0 at i=1)
              i=2

Result:       [1, 2, 0, 0, 0] ✓
```

## Test Cases

```python
# Basic case
moveZeroes([0,1,0,3,12])           # [1,3,12,0,0]

# All zeros
moveZeroes([0,0,0,0])              # [0,0,0,0]

# No zeros
moveZeroes([1,2,3,4,5])            # [1,2,3,4,5]

# Zeros at end already
moveZeroes([1,9,8,0,0])            # [1,9,8,0,0]

# Zeros at beginning
moveZeroes([0,0,0,1,2])            # [1,2,0,0,0]

# Empty array
moveZeroes([])                     # []

# Single element
moveZeroes([0])                    # [0]
moveZeroes([42])                   # [42]

# With negative numbers
moveZeroes([-1,0,-3,5,0,0,8])      # [-1,-3,5,8,0,0,0]

# Alternating
moveZeroes([0,1,0,2,0,3])          # [1,2,3,0,0,0]

# Large array with few zeros
nums = list(range(1, 1001)) + [0, 0]
moveZeroes(nums)                   # [1,2,...,1000,0,0]
```

## Thought Process

**Problem analysis**:

- Move all zeroes to the end
- Maintain relative order of non-zero elements
- Must be in-place, O(1) extra space

**Key observations**:

1. We know where non-zero elements should go (at the front in order)
2. Everything else should be zeroes
3. Relative order requirement means we can't rearrange

**Approach considerations**:

**Naive approach** (not in-place):

- Copy all non-zeros: O(n)
- Copy all zeros: O(n)
- Not truly O(1) space

**Two-pointer approach**:

- `i` tracks next position for non-zero element
- `j` scans for non-zero elements
- Swap to maintain relative order
- Natural result: zeroes accumulate at end
- Truly in-place with O(1) space

**Why it works**:

- Every non-zero element is moved exactly to its correct final position
- `i` only advances when we place a non-zero
- All positions after last non-zero naturally become zeroes
- Processing left-to-right maintains relative order

This is the elegant O(n) time, O(1) space solution!

## Related Problems

- [27. Remove Element](https://leetcode.com/problems/remove-element/)
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
- [31. Next Permutation](https://leetcode.com/problems/next-permutation/)
- [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

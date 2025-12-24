# Remove Duplicates from Sorted Array

## Problem Summary

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
- The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**LeetCode Problem**: [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Repository File**: [easy/remove_element.py](../../easy/remove_element.py)

**Note**: The file is named `remove_element.py` but contains the solution for removing duplicates from a sorted array.

## Approach 1: Two Pointers (Implemented)

### Strategy

The implemented solution uses a **two-pointer approach**:

1. Use pointer `i` to track the position where the next unique element should go
2. Start `i` at index 1 (first position for potentially different element)
3. Iterate through array with pointer `n` starting from index 1
4. When `nums[n] != nums[n-1]`, we found a new unique element
5. Place it at position `i` and increment `i`
6. Return `i` which represents the count of unique elements

**Code**:

```python
def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    for n in range(1, len(nums)):
        if nums[n] != nums[n - 1]:
            nums[i] = nums[n]
            i += 1
    return i
```

### How It Works

**Example 1**: `nums = [1,1,2]`

```
Initial:  [1, 1, 2]
          i=1, n=1

n=1: nums[1]=1, nums[0]=1
  1 == 1, skip

n=2: nums[2]=2, nums[1]=1
  2 != 1, found unique
  nums[1] = 2
  i = 2
  Result: [1, 2, 2]

Return i=2
First 2 elements: [1, 2] ✓
```

**Example 2**: `nums = [0,0,1,1,1,2,2,3,3,4]`

```
Initial:  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
          i=1

n=1: 0 == 0, skip
n=2: 1 != 0, nums[1]=1, i=2 → [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
n=3: 1 == 1, skip
n=4: 1 == 1, skip
n=5: 2 != 1, nums[2]=2, i=3 → [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
n=6: 2 == 2, skip
n=7: 3 != 2, nums[3]=3, i=4 → [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
n=8: 3 == 3, skip
n=9: 4 != 3, nums[4]=4, i=5 → [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]

Return i=5
First 5 elements: [0, 1, 2, 3, 4] ✓
```

### Why This Works

**Key insight**: Since array is sorted, duplicates are adjacent.

- Pointer `i` always points to the next position for a unique element
- We only copy when we find a new value (nums[n] != nums[n-1])
- Elements after index `i` don't matter
- The comparison `nums[n] != nums[n-1]` catches each new unique value

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass through the array
  - Each element examined exactly once
- **Space Complexity**: O(1)
  - In-place modification
  - Only using two pointers (i and n)

### Edge Cases Handled

1. **Empty array**: `[]` → Returns 0 (loop doesn't run, but i=1 - potential bug!)
2. **Single element**: `[1]` → Returns 1 (i starts at 1, loop doesn't execute)
3. **No duplicates**: `[1,2,3]` → Returns 3 (all elements copied)
4. **All duplicates**: `[1,1,1,1,1]` → Returns 1 (only first kept)
5. **Two elements (same)**: `[1,1]` → Returns 1
6. **Two elements (different)**: `[1,2]` → Returns 2

## Approach 2: Two Pointers (Safer Alternative)

More robust version with explicit empty check:

```python
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    i = 1
    for n in range(1, len(nums)):
        if nums[n] != nums[n - 1]:
            nums[i] = nums[n]
            i += 1

    return i
```

### Advantages

- Handles empty array explicitly
- Same logic as implemented solution
- More defensive programming

### Complexity

- **Time**: O(n)
- **Space**: O(1)

## Approach 3: Two Pointers (Slow/Fast Pattern)

Classic slow/fast pointer pattern:

```python
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
```

### How It Works

```
nums = [1, 1, 2]

slow=0, fast=1: nums[1]=1 == nums[0]=1, skip
slow=0, fast=2: nums[2]=2 != nums[0]=1
  slow=1, nums[1]=2
  Result: [1, 2, 2]

Return slow+1 = 2 ✓
```

### Differences

- Uses `slow` and `fast` naming
- `slow` points to last unique element (not next position)
- Returns `slow + 1` (count = index + 1)
- More intuitive for some developers

### Complexity

- **Time**: O(n)
- **Space**: O(1)

## Approach 4: Using Set (Not Optimal)

Non-optimal approach using extra space:

```python
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    unique = []
    seen = set()

    for num in nums:
        if num not in seen:
            unique.append(num)
            seen.add(num)

    # Copy back
    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique)
```

### Analysis

- **Time**: O(n)
- **Space**: O(n) - Extra set and list
- **Not optimal**: Violates O(1) space constraint
- Works but unnecessary given sorted property

## Comparison of Approaches

| Approach                   | Time | Space | Pros                      | Cons                  |
| -------------------------- | ---- | ----- | ------------------------- | --------------------- |
| Two Pointers (Implemented) | O(n) | O(1)  | Optimal, minimal code     | No empty check        |
| Two Pointers (Safer)       | O(n) | O(1)  | Optimal, safer            | Slightly more code    |
| Slow/Fast Pattern          | O(n) | O(1)  | Optimal, intuitive naming | Returns slow+1        |
| Set-based                  | O(n) | O(n)  | Clear logic               | Extra space, overkill |

**Winner**: Two-pointer approach - O(n) time, O(1) space

## Edge Cases & Considerations

1. **Empty array**:

   - `nums = []` → `0`
   - Implemented solution returns 1 (bug!), needs check

2. **Single element**:

   - `nums = [1]` → `1`
   - Works correctly

3. **All same elements**:

   - `nums = [5,5,5,5]` → `1`
   - Only first element kept

4. **No duplicates**:

   - `nums = [0,1,2,3,4]` → `5`
   - All elements copied

5. **Alternating duplicates**:

   - `nums = [1,1,2,2,3,3,4,4]` → `4`
   - One from each group

6. **Negative numbers**:

   - `nums = [-1,-1,0,0,1,1]` → `3`
   - Works with any integers

7. **Large arrays with duplicates**:

   - `nums = [1]*1000 + [2]*500` → `2`
   - Still O(n) efficient

8. **Duplicates at end**:
   - `nums = [1,2,3,4,5,5,5,5]` → `5`
   - Works correctly

## Common Pitfalls

1. **Not starting i at correct index**:

   ```python
   # WRONG: i starts at 0
   i = 0
   for n in range(1, len(nums)):
       if nums[n] != nums[n-1]:
           nums[i] = nums[n]  # Overwrites first!
           i += 1

   # CORRECT: i starts at 1
   i = 1
   ```

2. **Comparing with wrong element**:

   ```python
   # WRONG: Comparing with nums[i]
   if nums[n] != nums[i]:

   # CORRECT: Compare with previous
   if nums[n] != nums[n-1]:
   ```

3. **Missing empty array check**:

   ```python
   # RISKY: Returns 1 for empty array
   i = 1
   for n in range(1, len(nums)):  # Doesn't execute
   return i  # Returns 1!

   # BETTER: Add check
   if not nums:
       return 0
   ```

4. **Off-by-one in return**:

   ```python
   # WRONG: Depends on implementation
   return i - 1  # Wrong for i starting at 1

   # CORRECT: Return i directly
   return i
   ```

5. **Not maintaining order**:

   ```python
   # WRONG: Using set loses order
   nums[:] = list(set(nums))
   return len(nums)

   # CORRECT: Two-pointer maintains order
   ```

## Optimization Notes

The two-pointer approach is **optimal**:

- **Time**: O(n) - Must examine all elements
- **Space**: O(1) - Only pointers used

**Key optimization**: Leveraging sorted property

- Duplicates are adjacent in sorted array
- No need to track all seen values
- Simple comparison with previous element

**Why this is efficient**:

- Single pass through array
- No extra data structures
- In-place modification
- Constant-time operations per element

## Visual Example

```
Input: [1, 1, 2, 2, 3, 3]

Initial:
  [1, 1, 2, 2, 3, 3]
   i=1

n=1: nums[1]=1 == nums[0]=1, skip
  [1, 1, 2, 2, 3, 3]
   i=1

n=2: nums[2]=2 != nums[1]=1, copy
  nums[1] = 2, i=2
  [1, 2, 2, 2, 3, 3]
      i=2

n=3: nums[3]=2 == nums[2]=2, skip
  [1, 2, 2, 2, 3, 3]
      i=2

n=4: nums[4]=3 != nums[3]=2, copy
  nums[2] = 3, i=3
  [1, 2, 3, 2, 3, 3]
         i=3

n=5: nums[5]=3 == nums[4]=3, skip
  [1, 2, 3, 2, 3, 3]
         i=3

Return i=3
First 3 elements: [1, 2, 3] ✓
```

## Test Cases

```python
# Basic with duplicates
removeDuplicates([1,1,2])              # 2, [1,2,...]

# No duplicates
removeDuplicates([0,1,2,3,4])          # 5, [0,1,2,3,4]

# All same
removeDuplicates([5,5,5,5])            # 1, [5,...]

# Empty (needs fix)
removeDuplicates([])                   # 0, []

# Single element
removeDuplicates([10])                 # 1, [10]

# Large with duplicates
nums = [1]*1000 + [2]*500 + [3]*200
removeDuplicates(nums)                 # 3, [1,2,3,...]

# Alternating
removeDuplicates([1,1,2,2,3,3,4,4])    # 4, [1,2,3,4,...]

# Negative numbers
removeDuplicates([-1,-1,0,0,1,1])      # 3, [-1,0,1,...]

# Duplicates at end
removeDuplicates([1,2,3,4,5,5,5,5])    # 5, [1,2,3,4,5,...]
```

## Thought Process

**Problem analysis**:

- Array is sorted (crucial!)
- Remove duplicates in-place
- Return count of unique elements
- Keep relative order

**Key observations**:

1. Sorted array → duplicates are adjacent
2. Don't need to track all seen values
3. Simple comparison with previous element
4. Two pointers: one for reading, one for writing

**Approach considerations**:

**Why two pointers work**:

- `i` tracks where to write next unique value
- `n` scans through array
- Only copy when value changes
- Leverages sorted property perfectly

**Why this is optimal**:

- Single pass: O(n) time
- No extra space: O(1) space
- In-place modification
- Maintains order naturally

This is the standard solution for removing duplicates from a sorted array!

## Related Problems

- [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
- [27. Remove Element](https://leetcode.com/problems/remove-element/)
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

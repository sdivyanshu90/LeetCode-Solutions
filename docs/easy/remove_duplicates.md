# Remove Duplicates from Sorted Array

## Problem Summary

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
- The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**LeetCode Problem**: [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

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

1. **Empty array**: `[]` → Returns 0 (loop doesn't run)
2. **Single element**: `[1]` → Returns 1 (i starts at 1, loop doesn't find duplicates)
3. **No duplicates**: `[1,2,3]` → Returns 3 (all elements copied)
4. **All duplicates**: `[1,1,1,1,1]` → Returns 1 (only first kept)
5. **Two elements (same)**: `[1,1]` → Returns 1
6. **Two elements (different)**: `[1,2]` → Returns 2

## Approach 2: Two Pointers (Alternative)

Slightly different two-pointer approach:

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

### Differences

- Uses `slow` and `fast` naming (more descriptive)
- Increments `slow` before assignment
- Returns `slow + 1` instead of `slow`
- Explicit empty array check

### Complexity

- **Time**: O(n)
- **Space**: O(1)

### Advantages

- More descriptive variable names
- Clearer logic flow

## Approach 3: Set and Rebuild

Using a set to track unique elements:

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

    # Copy back to nums
    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique)
```

### Analysis

- **Time**: O(n)
- **Space**: O(n) - Set and list storage
- **Not optimal**: Uses extra space
- Works but violates O(1) space requirement

## Approach 4: Using Python List Methods

Pythonic approach (not in-place):

```python
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    # Remove duplicates while maintaining order
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
        else:
            i += 1

    return len(nums)
```

### Analysis

- **Time**: O(n²) - pop operation is O(n)
- **Space**: O(1) - In-place
- **Inefficient**: Not optimal due to repeated pop operations

## Comparison of Approaches

| Approach                   | Time  | Space | Pros              | Cons          |
| -------------------------- | ----- | ----- | ----------------- | ------------- |
| Two Pointers (Implemented) | O(n)  | O(1)  | Optimal, simple   | None          |
| Two Pointers (Alternative) | O(n)  | O(1)  | Descriptive names | Same as above |
| Set and Rebuild            | O(n)  | O(n)  | Clear logic       | Extra space   |
| List Methods               | O(n²) | O(1)  | Pythonic          | Too slow      |

**Winner**: Two-pointer approach - O(n) time, O(1) space

## Edge Cases & Considerations

1. **Empty array**:

   - `nums = []` → `0`
   - Loop doesn't execute, returns 0 (but would fail without check)

2. **Single element**:

   - `nums = [1]` → `1`
   - Loop starts at index 1 (doesn't execute), returns i=1

3. **Two identical elements**:

   - `nums = [1,1]` → `1`
   - n=1: 1==1, skip, return 1

4. **No duplicates**:

   - `nums = [1,2,3]` → `3`
   - Each element is unique, all copied

5. **All same elements**:

   - `nums = [1,1,1,1,1]` → `1`
   - Only first element kept

6. **Multiple groups of duplicates**:

   - `nums = [1,1,2,2,3,3]` → `3`
   - One from each group kept

7. **Negative numbers**:

   - `nums = [-3,-3,-2,-1,-1,0,0,0,0,0]` → `4`
   - Works with any integers

8. **Large number of duplicates**:
   - `nums = [1,1,1,...,1] (1000 times)` → `1`
   - Still O(n) time

## Common Pitfalls

1. **Not starting from correct index**:

   ```python
   # WRONG: i starts at 0
   i = 0
   for n in range(1, len(nums)):
       if nums[n] != nums[n-1]:
           nums[i] = nums[n]  # Overwrites first element!
           i += 1

   # CORRECT: i starts at 1
   i = 1
   for n in range(1, len(nums)):
       if nums[n] != nums[n-1]:
           nums[i] = nums[n]
           i += 1
   ```

2. **Comparing with wrong element**:

   ```python
   # WRONG: Comparing with nums[i]
   for n in range(1, len(nums)):
       if nums[n] != nums[i]:  # Wrong comparison
           nums[i] = nums[n]
           i += 1

   # CORRECT: Compare with previous element
   if nums[n] != nums[n-1]:
   ```

3. **Off-by-one in return value**:

   ```python
   # WRONG: Returning i-1
   return i - 1

   # CORRECT: i is already the count
   return i
   ```

4. **Not handling empty array**:

   ```python
   # RISKY: Might work in this implementation
   i = 1
   for n in range(1, len(nums)):  # range(1, 0) is empty
   return i  # Returns 1 for empty array! WRONG

   # BETTER: Check empty explicitly
   if not nums:
       return 0
   ```

5. **Creating new array instead of in-place**:

   ```python
   # WRONG: Not in-place
   def removeDuplicates(self, nums):
       return len(set(nums))  # Doesn't modify nums!

   # CORRECT: Modify nums in-place
   # Copy unique elements to front of nums
   ```

## Optimization Notes

The two-pointer approach is **optimal**:

- **Time**: O(n) - Can't do better, must check all elements
- **Space**: O(1) - In-place modification, only pointers

**Why this is optimal**:

- Single pass through array
- No additional data structures
- In-place modification
- Leverages sorted property

**Key optimization**: The array is sorted, so duplicates are adjacent

- Don't need to track all seen values
- Just compare with previous element
- Simple O(1) comparison per element

## Visual Example

```
Input: [1, 1, 2, 2, 3]

Initial state:
  [1, 1, 2, 2, 3]
   i=1

Step 1: n=1, nums[1]=1, nums[0]=1
  1 == 1, skip
  [1, 1, 2, 2, 3]
   i=1

Step 2: n=2, nums[2]=2, nums[1]=1
  2 != 1, copy
  nums[1] = 2, i = 2
  [1, 2, 2, 2, 3]
      i=2

Step 3: n=3, nums[3]=2, nums[2]=2
  2 == 2, skip
  [1, 2, 2, 2, 3]
      i=2

Step 4: n=4, nums[4]=3, nums[3]=2
  3 != 2, copy
  nums[2] = 3, i = 3
  [1, 2, 3, 2, 3]
         i=3

Return i=3
First 3 elements: [1, 2, 3] ✓
```

## Test Cases

```python
# Basic cases
removeDuplicates([1,1,2])                    # 2, [1,2,...]
removeDuplicates([0,0,1,1,1,2,2,3,3,4])      # 5, [0,1,2,3,4,...]

# Empty array
removeDuplicates([])                         # 0, []

# Single element
removeDuplicates([1])                        # 1, [1]

# No duplicates
removeDuplicates([1,2,3])                    # 3, [1,2,3]

# All duplicates
removeDuplicates([1,1,1,1,1])                # 1, [1,...]

# Two elements (same)
removeDuplicates([1,1])                      # 1, [1,...]

# Two elements (different)
removeDuplicates([1,2])                      # 2, [1,2]

# Multiple duplicate groups
removeDuplicates([1,2,2,3,3,4,4,5,5])        # 5, [1,2,3,4,5,...]

# Long array no duplicates
removeDuplicates([1,2,3,4,5,6,7,8,9,10])     # 10, [1,2,...,10]

# Mixed duplicates
removeDuplicates([1,1,1,2,2,3,3,4,4,5,5])    # 5, [1,2,3,4,5,...]
```

## Thought Process

**Problem analysis**:

- Array is sorted (important!)
- Remove duplicates in-place
- Return count of unique elements
- First k elements should contain uniques

**Key observations**:

1. Array is sorted → duplicates are adjacent
2. Don't need to track all seen values
3. Just need to identify when value changes
4. Can use two pointers: one for reading, one for writing

**Approach considerations**:

**Why two pointers?**

- Need to track: where to write next unique value
- Need to track: where we're currently reading
- `i` = write position (next slot for unique element)
- `n` = read position (scanning through array)

**Why compare with previous element?**

- Array is sorted, so duplicates are consecutive
- If `nums[n] != nums[n-1]`, we found a new value
- No need for hash set or complex tracking

**Why start i at 1?**

- First element is always unique (nothing before it)
- Start writing at position 1 (may overwrite duplicate)

This leads to an optimal O(n) time, O(1) space solution that leverages the sorted property!

## Related Problems

- [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
- [27. Remove Element](https://leetcode.com/problems/remove-element/)
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [26. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

# Merge Sorted Array

## Problem Summary

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored **inside the array** `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**LeetCode Problem**: [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

## Approach 1: Three Pointers (Backward) - Implemented

### Strategy

The implemented solution uses a **backward three-pointer approach**:

1. Start from the end of both arrays (positions `m-1` and `n-1`)
2. Compare elements from both arrays
3. Place the larger element at the end of `nums1` (position `m+n-1`)
4. Move the relevant pointers backward
5. If `nums2` has remaining elements, copy them to `nums1`

**Key Insight**: By filling from the back, we avoid overwriting elements in `nums1` that haven't been processed yet.

**Code**:

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m + n - 1  # Position to fill in nums1
    j, k = m - 1, n - 1  # Last elements of nums1 and nums2

    while j >= 0 and k >= 0:
        if nums1[j] > nums2[k]:
            nums1[i] = nums1[j]
            i -= 1
            j -= 1
        else:
            nums1[i] = nums2[k]
            i -= 1
            k -= 1

    # Copy remaining elements from nums2 if any
    while k >= 0:
        nums1[i] = nums2[k]
        i -= 1
        k -= 1
```

### How It Works

**Example**: `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`

```
Initial state:
nums1: [1, 2, 3, 0, 0, 0]
        j=2        i=5
nums2: [2, 5, 6]
        k=2

Step 1: Compare nums1[2]=3 vs nums2[2]=6
  - 6 > 3, place 6 at position 5
  nums1: [1, 2, 3, 0, 0, 6]
          j=2     i=4
  nums2: [2, 5, 6]
          k=1

Step 2: Compare nums1[2]=3 vs nums2[1]=5
  - 5 > 3, place 5 at position 4
  nums1: [1, 2, 3, 0, 5, 6]
          j=2  i=3
  nums2: [2, 5, 6]
          k=0

Step 3: Compare nums1[2]=3 vs nums2[0]=2
  - 3 > 2, place 3 at position 3
  nums1: [1, 2, 3, 3, 5, 6]
          j=1  i=2
  nums2: [2, 5, 6]
          k=0

Step 4: Compare nums1[1]=2 vs nums2[0]=2
  - 2 ≤ 2, place 2 (from nums2) at position 2
  nums1: [1, 2, 2, 3, 5, 6]
          j=1  i=1
  nums2: [2, 5, 6]
          k=-1

Step 5: k < 0, exit while loop
Result: [1, 2, 2, 3, 5, 6]
```

### Why Fill Backward?

- **Avoids overwriting**: The last `n` positions of `nums1` are zeros (placeholders)
- **No extra space needed**: We use the existing space in `nums1`
- **Forward filling would require**: Either extra space or complex shifting

### Complexity Analysis

- **Time Complexity**: O(m + n)
  - Each element from both arrays is processed exactly once
  - Single pass through both arrays
- **Space Complexity**: O(1)
  - Only using three pointer variables
  - In-place modification of `nums1`

### Edge Cases Handled

1. **nums2 is empty** (`n = 0`): Loop never executes, `nums1` unchanged
2. **nums1 is empty** (`m = 0`): Only second loop runs, copies all of `nums2`
3. **All nums1 elements smaller**: nums2 elements fill the end
4. **All nums1 elements larger**: nums1 stays mostly the same, nums2 goes to front
5. **Equal elements**: Takes from nums2 (stable-like behavior)

## Approach 2: Three Pointers (Simplified)

Cleaner version with single pointer update:

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1, p2 = m - 1, n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining from nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
```

### Differences

- More descriptive variable names: `p1`, `p2`, `p`
- Single `p` pointer that always decrements
- Slightly more readable

### Complexity

- **Time**: O(m + n)
- **Space**: O(1)

## Approach 3: Copy and Sort (Naive)

Simple but less efficient approach:

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Copy nums2 into nums1
    nums1[m:m+n] = nums2
    # Sort in place
    nums1.sort()
```

### Analysis

- **Time**: O((m+n) log(m+n)) - Due to sorting
- **Space**: O(1) or O(m+n) depending on sort implementation
- **Simple** but doesn't use the fact that arrays are already sorted
- **Not optimal** - wastes the pre-sorted property

## Approach 4: Forward Merge with Extra Space

Use auxiliary array to merge forward:

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1_copy = nums1[:m]
    p1 = p2 = 0

    for p in range(m + n):
        if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[p] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
```

### Analysis

- **Time**: O(m + n)
- **Space**: O(m) - Need to store copy of nums1
- **Less optimal** due to extra space usage
- More intuitive for those familiar with standard merge

## Approach 5: Using Python Built-ins

Pythonic one-liner:

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()
```

### Notes

- Very concise
- Same complexity as Approach 3
- Good for quick prototyping, not for interview optimization

## Comparison of Approaches

| Approach               | Time             | Space | Pros              | Cons                        |
| ---------------------- | ---------------- | ----- | ----------------- | --------------------------- |
| Backward (Implemented) | O(m+n)           | O(1)  | Optimal, in-place | Requires backward thinking  |
| Simplified Backward    | O(m+n)           | O(1)  | More readable     | Same logic                  |
| Copy & Sort            | O((m+n)log(m+n)) | O(1)  | Very simple       | Doesn't use sorted property |
| Forward with Copy      | O(m+n)           | O(m)  | Forward logic     | Extra space                 |
| Python Built-in        | O((m+n)log(m+n)) | O(1)  | One-liner         | Suboptimal                  |

**Winner**: Backward three-pointer approach (Implemented) - O(m+n) time, O(1) space

## Edge Cases & Considerations

1. **Empty nums2** (`n = 0`):

   - `nums1 = [1], m = 1, nums2 = [], n = 0` → `[1]`
   - No changes needed, first loop never executes

2. **Empty nums1** (`m = 0`):

   - `nums1 = [0], m = 0, nums2 = [1], n = 1` → `[1]`
   - First loop skipped (j < 0), second loop copies all of nums2

3. **All nums2 elements larger**:

   - `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [4,5,6], n = 3` → `[1,2,3,4,5,6]`
   - nums2 naturally fills the end

4. **All nums2 elements smaller**:

   - `nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3` → `[1,2,3,4,5,6]`
   - nums1 elements shift to the end, nums2 fills from front

5. **Interleaved elements**:

   - `nums1 = [1,3,5,0,0,0], m = 3, nums2 = [2,4,6], n = 3` → `[1,2,3,4,5,6]`
   - Elements alternate from both arrays

6. **Duplicate elements**:

   - `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3` → `[1,2,2,3,5,6]`
   - Duplicates handled correctly

7. **Single elements**:

   - `nums1 = [2,0], m = 1, nums2 = [1], n = 1` → `[1,2]`
   - Works for minimal input

8. **Large arrays with different sizes**:
   - `nums1 = [1,2,3,4,5,0,0], m = 5, nums2 = [6,7], n = 2` → `[1,2,3,4,5,6,7]`
   - Handles varying m and n

## Common Pitfalls

1. **Trying to merge forward without extra space**:

   ```python
   # WRONG: Overwrites elements we haven't processed
   i = j = k = 0
   while j < m and k < n:
       if nums1[j] <= nums2[k]:
           nums1[i] = nums1[j]  # Can overwrite needed elements!
           j += 1
       else:
           nums1[i] = nums2[k]
           k += 1
       i += 1
   ```

2. **Forgetting to copy remaining nums2 elements**:

   ```python
   # WRONG: Missing second while loop
   while j >= 0 and k >= 0:
       # ... merge logic
   # If nums2 has elements left, they're not copied!

   # CORRECT: Add second loop
   while k >= 0:
       nums1[i] = nums2[k]
       i -= 1
       k -= 1
   ```

3. **Not handling empty arrays**:

   ```python
   # WRONG: Doesn't check if arrays are empty
   if nums1[j] > nums2[k]:  # Can fail if m=0 or n=0

   # CORRECT: Loop condition handles it
   while j >= 0 and k >= 0:
       # ...
   ```

4. **Off-by-one errors with indices**:

   ```python
   # WRONG: Starting at m and n instead of m-1 and n-1
   j, k = m, n  # Out of bounds!

   # CORRECT: Last valid indices
   j, k = m - 1, n - 1
   ```

5. **Returning a value instead of modifying in-place**:

   ```python
   # WRONG: Problem asks for in-place modification
   def merge(self, nums1, m, nums2, n):
       return sorted(nums1[:m] + nums2)

   # CORRECT: Modify nums1 directly, no return
   def merge(self, nums1, m, nums2, n) -> None:
       # ... modify nums1 in-place
   ```

6. **Not needing to copy remaining nums1 elements**:
   ```python
   # UNNECESSARY: If j >= 0, elements are already in place
   while j >= 0:
       nums1[i] = nums1[j]  # Not needed!
       i -= 1
       j -= 1
   ```
   nums1 elements are already in the correct positions if they remain.

## Optimization Notes

The backward three-pointer approach is **optimal**:

- **Time**: O(m + n) - Can't be better, must process all elements
- **Space**: O(1) - Can't be better, in-place requirement
- **Single pass** through both arrays

**Why backward is better than forward**:

- Forward requires O(m) extra space to avoid overwriting
- Backward uses the fact that last n positions are empty
- No auxiliary array needed

**Key optimization**: Using the empty space at the end of nums1 as working area.

## Visual Example

```
nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3

Initial:
  [1, 2, 3, 0, 0, 0]
   j=2           i=5
  [2, 5, 6]
   k=2

Step 1: 3 < 6, place 6
  [1, 2, 3, 0, 0, 6]
   j=2        i=4
  [2, 5, 6]
      k=1

Step 2: 3 < 5, place 5
  [1, 2, 3, 0, 5, 6]
   j=2     i=3
  [2, 5, 6]
   k=0

Step 3: 3 > 2, place 3
  [1, 2, 3, 3, 5, 6]
      j=1  i=2
  [2, 5, 6]
   k=0

Step 4: 2 ≤ 2, place 2 (from nums2)
  [1, 2, 2, 3, 5, 6]
      j=1  i=1
  [2, 5, 6]
      k=-1

Done! k < 0, exit
Final: [1, 2, 2, 3, 5, 6]
```

**Another example** (nums2 smaller):

```
nums1 = [4,5,6,0,0,0], m=3, nums2 = [1,2,3], n=3

Initial:
  [4, 5, 6, 0, 0, 0]
         j=2        i=5
  [1, 2, 3]
         k=2

Step 1: 6 > 3, place 6
  [4, 5, 6, 0, 0, 6]
      j=1        i=4
  [1, 2, 3]
         k=2

Step 2: 5 > 3, place 5
  [4, 5, 6, 0, 5, 6]
   j=0        i=3
  [1, 2, 3]
         k=2

Step 3: 4 > 3, place 4
  [4, 5, 6, 4, 5, 6]
      j=-1     i=2
  [1, 2, 3]
         k=2

Now j < 0, copy remaining nums2:

Step 4: Copy 3
  [4, 5, 3, 4, 5, 6]
              i=1
  [1, 2, 3]
      k=1

Step 5: Copy 2
  [4, 2, 3, 4, 5, 6]
      i=0
  [1, 2, 3]
   k=0

Step 6: Copy 1
  [1, 2, 3, 4, 5, 6]
   i=-1
  [1, 2, 3]
      k=-1

Final: [1, 2, 3, 4, 5, 6]
```

## Test Cases

```python
# Basic merge
nums1 = [1,2,3,0,0,0]; merge(nums1, 3, [2,5,6], 3)
# Result: [1,2,2,3,5,6]

# Empty nums2
nums1 = [1]; merge(nums1, 1, [], 0)
# Result: [1]

# Empty nums1
nums1 = [0]; merge(nums1, 0, [1], 1)
# Result: [1]

# All nums2 larger
nums1 = [1,2,3,0,0,0]; merge(nums1, 3, [4,5,6], 3)
# Result: [1,2,3,4,5,6]

# All nums2 smaller
nums1 = [4,5,6,0,0,0]; merge(nums1, 3, [1,2,3], 3)
# Result: [1,2,3,4,5,6]

# Single element
nums1 = [2,0]; merge(nums1, 1, [1], 1)
# Result: [1,2]

# Duplicates
nums1 = [1,1,1,0,0,0]; merge(nums1, 3, [1,1,1], 3)
# Result: [1,1,1,1,1,1]

# Interleaved
nums1 = [1,3,5,0,0,0]; merge(nums1, 3, [2,4,6], 3)
# Result: [1,2,3,4,5,6]

# Different sizes
nums1 = [1,2,3,4,5,0,0]; merge(nums1, 5, [6,7], 2)
# Result: [1,2,3,4,5,6,7]

nums1 = [1,0,0,0,0,0]; merge(nums1, 1, [2,3,4,5,6], 5)
# Result: [1,2,3,4,5,6]
```

## Thought Process

**Problem analysis**:

- Two sorted arrays need to be merged
- Result must be in nums1 (in-place)
- nums1 has extra space at the end (n zeros)

**Key observations**:

1. Arrays are already sorted - can use merge logic
2. nums1 has exactly enough space (m + n total)
3. Last n positions are empty (zeros)

**Approach considerations**:

**Forward merge** (intuitive but problematic):

- Start from beginning, compare elements
- Problem: Overwriting nums1 elements we haven't processed
- Would need O(m) extra space to store nums1 copy

**Backward merge** (optimal):

- Start from the end where there's empty space
- Compare largest elements from both arrays
- Place the larger one at the current end position
- No risk of overwriting unprocessed elements
- Uses the zeros space as working area

**Why backward works**:

- Empty space is at the end
- We fill from right to left
- By the time we reach a position, we've already processed what was there
- If nums1 elements remain, they're already in correct positions

This leads to O(m+n) time, O(1) space solution - optimal!

## Related Problems

- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
- [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
- [148. Sort List](https://leetcode.com/problems/sort-list/)
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

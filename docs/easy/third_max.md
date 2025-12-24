# Third Maximum Number

## Problem Summary

Given an integer array `nums`, return the **third distinct maximum number** in this array. If the third maximum does not exist, return the **maximum number** in the array.

**LeetCode Problem**: [414. Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)

## Approach: Single Pass with Three Variables (Implemented)

### Strategy

The implemented solution uses **three variables to track the top three maximum values**:

1. Initialize three variables `first_max`, `second_max`, `third_max` to `-infinity`
2. Initialize `distinct_count = 0` to track how many distinct numbers we've found
3. Iterate through the array once:
   - If number > first_max: shift all values down, set new first_max, increment count
   - Else if number is between first_max and second_max: shift second and third, set new second_max, increment count
   - Else if number is between second_max and third_max: set new third_max, increment count
4. If we found at least 3 distinct numbers, return third_max
5. Otherwise return first_max (the maximum)

**Code**:

```python
def thirdMax(self, nums: List[int]) -> int:
    first_max = second_max = third_max = float('-inf')
    distinct_count = 0

    for num in nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
            distinct_count += 1
        elif num < first_max and num > second_max:
            third_max = second_max
            second_max = num
            distinct_count += 1
        elif num < second_max and num > third_max:
            third_max = num
            distinct_count += 1

    if distinct_count >= 3:
        return third_max
    else:
        return first_max
```

### How It Works

**Key insight**: Use three variables to maintain the top 3 values seen so far, only counting distinct numbers.

**Example 1**: `nums = [3, 2, 1]`

```
Initial: first_max=-inf, second_max=-inf, third_max=-inf, distinct_count=0

Process num=3:
  3 > -inf? Yes
  Shift: third_max=-inf, second_max=-inf, first_max=3
  distinct_count=1
  State: first=3, second=-inf, third=-inf, count=1

Process num=2:
  2 > 3? No
  2 < 3 and 2 > -inf? Yes
  Shift: third_max=-inf, second_max=2
  distinct_count=2
  State: first=3, second=2, third=-inf, count=2

Process num=1:
  1 > 3? No
  1 < 3 and 1 > 2? No
  1 < 2 and 1 > -inf? Yes
  Set: third_max=1
  distinct_count=3
  State: first=3, second=2, third=1, count=3

distinct_count >= 3? Yes
Return third_max = 1 ✓
```

**Example 2**: `nums = [1, 2]`

```
Initial: first_max=-inf, second_max=-inf, third_max=-inf, distinct_count=0

Process num=1:
  1 > -inf? Yes
  Shift: third_max=-inf, second_max=-inf, first_max=1
  distinct_count=1
  State: first=1, second=-inf, third=-inf, count=1

Process num=2:
  2 > 1? Yes
  Shift: third_max=-inf, second_max=1, first_max=2
  distinct_count=2
  State: first=2, second=1, third=-inf, count=2

distinct_count >= 3? No
Return first_max = 2 ✓
```

**Example 3**: `nums = [2, 2, 3, 1]` (duplicates)

```
Initial: first_max=-inf, second_max=-inf, third_max=-inf, distinct_count=0

Process num=2:
  2 > -inf? Yes
  Shift: first_max=2, distinct_count=1
  State: first=2, second=-inf, third=-inf, count=1

Process num=2:
  2 > 2? No
  2 < 2 and 2 > -inf? No (2 is not < 2)
  2 < -inf and 2 > -inf? No
  No condition met, skip (duplicate)
  State: first=2, second=-inf, third=-inf, count=1

Process num=3:
  3 > 2? Yes
  Shift: first_max=3, second_max=2, distinct_count=2
  State: first=3, second=2, third=-inf, count=2

Process num=1:
  1 > 3? No
  1 < 3 and 1 > 2? No
  1 < 2 and 1 > -inf? Yes
  Set: third_max=1, distinct_count=3
  State: first=3, second=2, third=1, count=3

distinct_count >= 3? Yes
Return third_max = 1 ✓
```

**Example 4**: `nums = [1, 2, -2147483648]` (extreme values)

```
Initial: first_max=-inf, second_max=-inf, third_max=-inf, distinct_count=0

Process num=1:
  1 > -inf? Yes
  first_max=1, distinct_count=1
  State: first=1, second=-inf, third=-inf, count=1

Process num=2:
  2 > 1? Yes
  first_max=2, second_max=1, distinct_count=2
  State: first=2, second=1, third=-inf, count=2

Process num=-2147483648:
  -2147483648 > 2? No
  -2147483648 < 2 and -2147483648 > 1? No
  -2147483648 < 1 and -2147483648 > -inf? Yes
  third_max=-2147483648, distinct_count=3
  State: first=2, second=1, third=-2147483648, count=3

distinct_count >= 3? Yes
Return third_max = -2147483648 ✓
```

### Why Use -infinity?

**Initial value choice**:

```
Using -infinity handles edge cases:
- Any number (even negative integers) will be > -infinity
- No special handling needed for negative numbers
- Natural boundary for comparisons

Alternative: Use None
- Would need explicit None checks
- More verbose code
- Less elegant
```

### Tracking Distinct Count

**Why count distinct numbers**:

```
Problem: "return third distinct maximum"
Examples:
  [1, 2, 2] → Only 2 distinct numbers (1, 2)
              So return max = 2, not 2 (third doesn't exist)

  [1, 2, 3, 4, 5] → 5 distinct numbers (1, 2, 3, 4, 5)
                     Third max = 3
```

**Without counting**:

```
# WRONG: Might return -inf if no third value seen
if third_max != float('-inf'):
    return third_max
else:
    return first_max

# Using count is clearer:
if distinct_count >= 3:
    return third_max
else:
    return first_max
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass through array
  - Constant work per element (comparisons and assignments)
  - n = length of array
- **Space Complexity**: O(1)
  - Only three variables for tracking max values
  - No additional data structures
  - Fixed extra space regardless of input size

### Advantages

- **Optimal time**: O(n) single pass required
- **Optimal space**: O(1) constant extra space
- **Efficient**: No sorting, no hash maps
- **Clear logic**: Easy to understand the tracking

### Disadvantages

- **Multiple conditions**: Several comparisons needed
- **Manual shifting**: Have to manually manage three variables
- **Error-prone**: Easy to get comparison operators wrong

## Alternative Approach 1: Using a Set

Use a set to get distinct numbers, then sort:

```python
def thirdMax(self, nums: List[int]) -> int:
    # Get distinct numbers
    distinct_nums = list(set(nums))

    # If less than 3 distinct numbers, return maximum
    if len(distinct_nums) < 3:
        return max(distinct_nums)

    # Sort in descending order and return third
    distinct_nums.sort(reverse=True)
    return distinct_nums[2]
```

### How It Works

**Example**: `nums = [3, 2, 1]`

```
distinct_nums = set(nums) = {1, 2, 3}
list(distinct_nums) = [1, 2, 3] (or any order)
len(distinct_nums) = 3 >= 3

Sort in descending order: [3, 2, 1]
Return [3, 2, 1][2] = 1 ✓
```

### Complexity

- **Time**: O(n + k log k)
  - Create set: O(n)
  - Sort: O(k log k) where k ≤ n, often k ≤ 3
  - Overall: O(n)
- **Space**: O(k) where k ≤ n (set of distinct numbers)

### Advantages

- **Simpler logic**: No manual comparisons
- **Clear intent**: Easily see we want third of distinct numbers
- **Flexible**: Easy to extend to nth maximum

### Disadvantages

- **Extra space**: Uses O(k) additional space
- **Sorting overhead**: Unnecessary to sort all distinct numbers
- **Less efficient**: More operations than needed

## Alternative Approach 2: Using Heap

Use a min-heap to track top 3 values:

```python
import heapq

def thirdMax(self, nums: List[int]) -> int:
    # Use set to get distinct numbers
    distinct_nums = set(nums)

    # If less than 3, return maximum
    if len(distinct_nums) < 3:
        return max(distinct_nums)

    # Use nlargest to get top 3
    top_three = heapq.nlargest(3, distinct_nums)
    return top_three[2]
```

### How It Works

Uses `heapq.nlargest` to efficiently find top 3 elements.

**Example**: `nums = [3, 2, 1]`

```
distinct_nums = {1, 2, 3}
len(distinct_nums) = 3

heapq.nlargest(3, {1, 2, 3}) = [3, 2, 1]
Return [3, 2, 1][2] = 1 ✓
```

### Complexity

- **Time**: O(n + k log k) where k = 3
  - Set creation: O(n)
  - nlargest: O(n log k) = O(n log 3)
  - Overall: O(n)
- **Space**: O(k) for set

### Advantages

- **Efficient**: Better than full sort
- **Clear semantics**: "nlargest" clearly states intent
- **Flexible**: Easy to find nth largest

### Disadvantages

- **More space**: Still requires set
- **Library dependent**: Requires heapq import
- **Overkill**: For just 3 elements, simpler approaches better

## Alternative Approach 3: Manual Stack Tracking

Manually maintain sorted list of top 3:

```python
def thirdMax(self, nums: List[int]) -> int:
    max_three = []

    for num in nums:
        # Skip if duplicate
        if num in max_three:
            continue

        # Insert in sorted position
        max_three.append(num)
        max_three.sort(reverse=True)

        # Keep only top 3
        if len(max_three) > 3:
            max_three.pop()

    # Return third if exists, else maximum
    if len(max_three) >= 3:
        return max_three[2]
    else:
        return max_three[0]
```

### Complexity

- **Time**: O(n) with O(3 log 3) = O(1) sort per element
- **Space**: O(1) - at most 3 elements

### Advantages

- **Simple to understand**: Easy to see what's happening
- **Flexible**: Works for any nth maximum

### Disadvantages

- **Slower**: Repeated sorting is wasteful
- **List operations**: List.append and sort overhead
- **Membership check**: `in` operator is O(k)

## Comparison of Approaches

| Approach                      | Time | Space | Difficulty | Pros              | Cons                |
| ----------------------------- | ---- | ----- | ---------- | ----------------- | ------------------- |
| Three Variables (Implemented) | O(n) | O(1)  | Medium     | Optimal both ways | Multiple conditions |
| Set + Sort                    | O(n) | O(k)  | Easy       | Simple logic      | Extra space         |
| Heap (nlargest)               | O(n) | O(k)  | Easy       | Library support   | Extra space         |
| Manual Stack                  | O(n) | O(1)  | Medium     | Flexible          | Repeated operations |

**Winner**: Three variables for optimal time and space

## Edge Cases & Considerations

1. **Less than 3 elements**:

   - `nums = [1, 2]` → `2` (return max)
   - Handled by: distinct_count < 3 check ✓

2. **Less than 3 distinct elements**:

   - `nums = [1, 1, 1]` → `1` (return max)
   - Handled by: duplicate detection ✓

3. **Exactly 3 distinct elements**:

   - `nums = [1, 2, 3]` → `1` (return third)
   - Normal case ✓

4. **Negative numbers**:

   - `nums = [-1, -2, -3]` → `-3` (return third)
   - Works correctly with -infinity initial value ✓

5. **Mix of positive and negative**:

   - `nums = [1, -1, 3, -2, -3]` → `-2` (return third)
   - Comparisons handle mixed signs ✓

6. **Large integers**:

   - `nums = [2147483647, -2147483648, 0]` → `-2147483648`
   - -infinity is less than all values ✓

7. **Single element**:

   - `nums = [5]` → `5` (return max)
   - distinct_count = 1 < 3 ✓

8. **All same value**:

   - `nums = [1, 1, 1, 1]` → `1` (return max)
   - Only 1 distinct, so return max ✓

9. **Two distinct values**:
   - `nums = [1, 2, 1, 2]` → `2` (return max)
   - Only 2 distinct, so return max ✓

## Common Pitfalls

1. **Not handling duplicates**:

   ```python
   # WRONG: Counts duplicates as distinct
   distinct_count += 1  # Always increments

   # CORRECT: Only count when truly a new maximum value
   if num > first_max:
       distinct_count += 1  # Skip if duplicate
   ```

2. **Wrong comparison operators**:

   ```python
   # WRONG: Allows equal values to update
   if num >= first_max:  # Should be >

   # CORRECT: Use strict inequalities
   if num > first_max:
   ```

3. **Not shifting values correctly**:

   ```python
   # WRONG: Lost second_max
   first_max = num
   second_max = num

   # CORRECT: Shift down the chain
   third_max = second_max
   second_max = first_max
   first_max = num
   ```

4. **Incorrect return condition**:

   ```python
   # WRONG: Returns -inf if no third value
   return third_max

   # CORRECT: Check if third exists
   if distinct_count >= 3:
       return third_max
   else:
       return first_max
   ```

5. **Using 0 or None as initial value**:

   ```python
   # WRONG: What if all numbers are negative?
   first_max = 0

   # CORRECT: Use -infinity
   first_max = float('-inf')
   ```

6. **Missing duplicate checks in conditions**:

   ```python
   # WRONG: Duplicate might update second when it shouldn't
   elif num > second_max:  # Missing bounds check
       second_max = num

   # CORRECT: Check both bounds
   elif num < first_max and num > second_max:
       second_max = num
   ```

## Optimization Notes

The implemented solution is **already optimal**:

- **Time**: O(n) - must examine every element at least once
- **Space**: O(1) - three variables is minimal possible
- **Single pass**: Can't reduce further

**Interview tips**:

- Start by explaining the problem clearly
- Mention that we need to track three maximum values
- Explain why using three variables is efficient
- Walk through step-by-step with an example
- Discuss handling duplicates
- Mention alternative approaches (set + sort)

**Key insight for interviews**:

```
Why three variables is optimal:

We only care about finding the third largest.
We don't need to store all elements or sort them.
Just track the top 3 as we iterate once.

This is O(1) space instead of O(n) like sorting would require.
This is O(n) time, same as any approach that reads all elements.
```

## Visual Example

```
Array: [3, 2, 1]

Step 1: Process 3
  first=-inf, second=-inf, third=-inf
  3 > -inf? Yes
  Shift: third=-inf, second=-inf, first=3

  first=3, second=-inf, third=-inf ✓

Step 2: Process 2
  first=3, second=-inf, third=-inf
  2 > 3? No
  2 < 3 and 2 > -inf? Yes
  Shift: third=-inf, second=2

  first=3, second=2, third=-inf ✓

Step 3: Process 1
  first=3, second=2, third=-inf
  1 > 3? No
  1 < 3 and 1 > 2? No
  1 < 2 and 1 > -inf? Yes
  Set: third=1

  first=3, second=2, third=1 ✓

Return 1 (third max) ✓


Array: [1, 1, 2] (with duplicates)

Step 1: Process 1
  1 > -inf? Yes
  first=1, count=1

Step 2: Process 1
  1 > 1? No
  1 < 1? No
  No condition met (duplicate skipped)
  Still count=1

Step 3: Process 2
  2 > 1? Yes
  Shift: first=2, second=1, count=2

count < 3, return first=2 ✓
```

## Test Cases

```python
# Basic cases
thirdMax([3, 2, 1])                    # 1

# Less than 3 elements
thirdMax([1, 2])                       # 2

# With duplicates
thirdMax([2, 2, 3, 1])                 # 1

# Negative numbers
thirdMax([1, 2, -2147483648])          # -2147483648

# Duplicates with 3 distinct
thirdMax([1, 1, 2])                    # 2

# Few elements with duplicates
thirdMax([5, 2, 2])                    # 5

# All same value
thirdMax([1, 1, 1])                    # 1

# Larger array
thirdMax([1, 2, 3, 4, 5])              # 3

# Many duplicates
thirdMax([2, 2, 3, 3, 1, 1])           # 1

# Multiple duplicates mixed
thirdMax([1, 2, 2, 5, 3, 5])           # 2

# Negative extremes
thirdMax([-1, -2, -3])                 # -3

# Large positive numbers
thirdMax([2147483646, 2147483647, 2147483645])  # 2147483645

# Single element
thirdMax([42])                         # 42

# Zero included
thirdMax([-1, 0, 1])                   # -1
```

## Thought Process

**Problem analysis**:

- Find third distinct maximum number
- If fewer than 3 distinct: return maximum
- Need to handle duplicates
- Need efficient single-pass approach

**Key observations**:

1. Only need to track top 3 values
2. Duplicates should be ignored (distinct means unique)
3. Can solve in single pass without storing all values
4. Three variables enough to track top 3

**Algorithm insight**:

```
Maintain three variables: first, second, third
As we iterate:
  - If number is new max: shift all down, set first
  - Else if between first and second: shift second/third, set second
  - Else if between second and third: set third

At end:
  - If we found 3 distinct: return third
  - Else: return first (the overall max)
```

**Why this works**:

- Each variable maintains its position in top-3 order
- Single pass O(n) time
- Constant O(1) space
- Handles duplicates by not incrementing count

**Optimal solution**:

- Time: O(n) - must see every element
- Space: O(1) - just three variables
- Both are optimal (can't do better)

**Interview strategy**:

1. Understand the problem (distinct maximum)
2. Mention single-pass approach
3. Explain three variables tracking
4. Code carefully with correct operators
5. Walk through examples with duplicates
6. Discuss complexity
7. Mention set+sort alternative

This problem tests:

- Array iteration
- Comparison logic and operators
- Edge case handling
- Space vs time optimization
- Problem constraint understanding (distinct)

## Related Problems

- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [1737. Change Minimum Characters to Satisfy One of Three Conditions](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/)
- [1738. Find Kth Largest XOR Coordinate Value](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/)
- [2119. A Number After Removing the Digit 6](https://leetcode.com/problems/a-number-after-removing-the-digit-6/)

# Contains Duplicate

## Problem Summary

Given an integer array `nums`, determine if any value appears at least twice. Return `True` if any duplicate exists, otherwise `False`.

**Examples**:

- `[1,2,3,1]` → `True`
- `[1,2,3,4]` → `False`
- `[]` → `False`

## Approach: Set Comparison (Implemented)

### Strategy

The solution uses set comparison to detect duplicates:

1. Convert the list to a set (which removes duplicates)
2. Compare the length of the set with the original list length
3. If lengths differ, duplicates exist

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

### How It Works

**Key insight**: Sets store only unique elements, so comparing sizes reveals duplicates.

**Example 1**: `nums = [1,2,3,1]`

```
Original list: [1,2,3,1]
len(nums) = 4

set(nums) = {1,2,3}
len(set(nums)) = 3

4 != 3 → True (duplicates exist) ✓
```

**Example 2**: `nums = [1,2,3,4]`

```
Original list: [1,2,3,4]
len(nums) = 4

set(nums) = {1,2,3,4}
len(set(nums)) = 4

4 == 4 → False (no duplicates) ✓
```

**Edge cases**:

- Empty list `[]` → `False` (no duplicates)
- Single element `[1]` → `False`
- All identical `[7,7,7,7]` → `True`

### Why Set Comparison Works

- **Automatic deduplication**: Sets inherently remove duplicates during construction
- **Length comparison**: If any element appeared multiple times, the set will be smaller
- **One-liner elegance**: Concise and leverages Python's built-in set implementation
- **Type-agnostic**: Works with any hashable type (integers, strings, tuples)

### Complexity Analysis

- **Time Complexity**: O(n) average case
  - Building set from list: O(n) with average O(1) hash operations
  - Length comparisons: O(1)
- **Space Complexity**: O(n)
  - Set stores up to n unique elements in worst case

### Advantages

- **Very concise**: One-liner solution
- **Fast for typical inputs**: Hash set operations are efficient
- **Clear intent**: Easy to understand what the code does
- **Pythonic**: Idiomatic use of Python's built-in types

### Disadvantages

- **Always builds full set**: Must process entire array, no early exit
- **Space usage**: Always uses O(n) space even if duplicate is found early
- **Not optimal for many duplicates**: If duplicates are common, wastes work

## Alternative Approach 1: Early-Exit with Streaming Set

Check elements one-by-one with early termination:

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

### How It Works

- Iterate through array maintaining a "seen" set
- For each element, check if already seen
- If yes, immediately return `True` (found duplicate)
- If no, add to set and continue
- Return `False` if loop completes (no duplicates)

### Complexity

- **Time**: O(n) average, but can exit early
- **Space**: O(n) worst case

### Advantages

- **Early termination**: Returns as soon as first duplicate found
- **Better for duplicate-heavy inputs**: Avoids processing entire array
- **Same asymptotic complexity**: O(n) time and space

### Disadvantages

- **More code**: Not a one-liner
- **Slightly slower for no-duplicate case**: Extra overhead of explicit loop

## Alternative Approach 2: Sorting (O(1) Space if in-place allowed)

Sort array and check adjacent elements:

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    nums_sorted = sorted(nums)
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i-1]:
            return True
    return False
```

### Complexity

- **Time**: O(n log n) - dominated by sorting
- **Space**: O(1) if in-place sort allowed, O(n) for sorted copy

### Advantages

- **Can use O(1) space**: If modifying input is allowed
- **Early exit**: Returns on first adjacent duplicate

### Disadvantages

- **Slower**: O(n log n) vs O(n)
- **Modifies input**: If sorting in-place

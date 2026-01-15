# Monotonic Array

## Problem Summary

- Array is monotonic if it's entirely non-increasing or entirely non-decreasing.
- Return true if array is monotonic.
- Example: [1,2,2,3] -> True (non-decreasing), [6,5,4,4] -> True (non-increasing).

Current implementation (in repository)

- Implementation tracks both directions:
  - Initializes two boolean flags: increase and decrease, both True.
  - Iterates through array comparing adjacent elements.
  - If element increases, sets decrease = False.
  - If element decreases, sets increase = False.
  - Returns True if either flag remains True.
- Example code:
  ```python
  increase, decrease = True, True
  for i in range(1, len(nums)):
      if nums[i] > nums[i - 1]:
          decrease = False
      elif nums[i] < nums[i - 1]:
          increase = False
  return increase or decrease
  ```

Why this works

- Starting with both flags True assumes monotonicity until proven otherwise.
- Any increase proves array is not decreasing (decrease = False).
- Any decrease proves array is not increasing (increase = False).
- Equal elements maintain both possibilities.
- At least one flag True means array is monotonic in that direction.

Time complexity

- Let n = length of array.
- Single pass through array: O(n).
- Each comparison is O(1).
- Overall time complexity: O(n).

Space complexity

- Only using two boolean variables.
- Space complexity: O(1).

Thought process and trade-offs

- Dual flag approach: elegant single-pass solution.
- Alternative: calculate overall trend first (first and last elements), then verify - could fail early but adds complexity.
- Alternative: two passes, one checking increase, one checking decrease - same complexity but less elegant.
- Current approach: optimal and clean.
- Early termination possible: could return False when both flags become False, but adds negligible benefit.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  increase, decrease = True, True
  for i in range(1, len(nums)):
      if nums[i] > nums[i - 1]:
          decrease = False
      elif nums[i] < nums[i - 1]:
          increase = False
  return increase or decrease
  ```

### How It Works

- Alternative: calculate overall trend first (first and last elements), then verify - could fail early but adds complexity.
- Alternative: two passes, one checking increase, one checking decrease - same complexity but less elegant.
- Current approach: optimal and clean.
- Early termination possible: could return False when both flags become False, but adds negligible benefit.

### Why Iteration Works

- Starting with both flags True assumes monotonicity until proven otherwise.
- Any increase proves array is not decreasing (decrease = False).
- Any decrease proves array is not increasing (increase = False).
- Equal elements maintain both possibilities.
- At least one flag True means array is monotonic in that direction.

Time complexity

- Let n = length of array.
- Single pass through array: O(n).
- Each comparison is O(1).
- Overall time complexity: O(n).

Space complexity

- Only using two boolean variables.
- Space complexity: O(1).

Thought process and trade-offs

- Dual flag approach: elegant single-pass solution.
- Alternative: calculate overall trend first (first and last elements), then verify - could fail early but adds complexity.
- Alternative: two passes, one checking increase, one checking decrease - same complexity but less elegant.
- Current approach: optimal and clean.
- Early termination possible: could return False when both flags become False, but adds negligible benefit.

### Complexity Analysis

- **Time Complexity**: - Let n = length of array. - Single pass through array: O(n). - Each comparison is O(1). - Overall time complexity: O(n). Space complexity - Only using two boolean variables. - Space complexity: O(1). Thought process and trade-offs - Dual flag approach: elegant single-pass solution. - Alternative: calculate overall trend first (first and last elements), then verify - could fail early but adds complexity. - Alternative: two passes, one checking increase, one checking decrease - same complexity but less elegant. - Current approach: optimal and clean. - Early termination possible: could return False when both flags become False, but adds negligible benefit.
- **Space Complexity**: - Only using two boolean variables. - Space complexity: O(1). Thought process and trade-offs - Dual flag approach: elegant single-pass solution. - Alternative: calculate overall trend first (first and last elements), then verify - could fail early but adds complexity. - Alternative: two passes, one checking increase, one checking decrease - same complexity but less elegant. - Current approach: optimal and clean. - Early termination possible: could return False when both flags become False, but adds negligible benefit.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space

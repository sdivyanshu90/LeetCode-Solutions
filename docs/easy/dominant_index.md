# Largest Number At Least Twice of Others

## Problem Summary

- Given an integer array nums, return the index of the largest element if it's at least twice every other element.
- If no such element exists, return -1.
- Example: [3,6,1,0] -> 6 is at least twice all others (6 >= 2×3, 6 >= 2×1, 6 >= 2×0), return index 1.

Current implementation (in repository)

- Implementation tracks largest and second largest:
  - Initializes largest as index 0, second_largest as None.
  - Iterates through array comparing each element.
  - Updates largest and second_largest indices accordingly.
  - At end, checks if largest >= 2 × second_largest.
  - Returns largest index if condition met, otherwise -1.
- Example code:
  ```python
  for i in range(1, len(nums)):
      if nums[i] > nums[largest]:
          second_largest = largest
          largest = i
      elif second_largest is None or nums[i] > nums[second_largest]:
          second_largest = i
  ```

Why this works

- For largest to be twice all others, it only needs to be twice the second largest.
- If largest >= 2 × second_largest, it's automatically >= 2 × all smaller elements.
- Single pass finds both largest and second largest efficiently.
- None handling for second_largest covers case when only one element processed.

Time complexity

- Let n = length of nums array.
- Single pass through array: O(n).
- Each comparison and update: O(1).
- Overall time complexity: O(n).

Space complexity

- Only storing two indices (largest, second_largest).
- Space complexity: O(1).

Thought process and trade-offs

- Key insight: only need to compare with second largest, not all elements.
- One-pass solution is optimal for this problem.
- Alternative: find max, remove it, find max again - requires two passes or copying array.
- Alternative: sort array and compare last two - O(n log n) time.
- Current approach: optimal O(n) time with O(1) space.
- Handles edge cases: single element array returns 0 (vacuously true).

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  for i in range(1, len(nums)):
      if nums[i] > nums[largest]:
          second_largest = largest
          largest = i
      elif second_largest is None or nums[i] > nums[second_largest]:
          second_largest = i
  ```

### How It Works

- Handles edge cases: single element array returns 0 (vacuously true).

### Why Iteration Works

- For largest to be twice all others, it only needs to be twice the second largest.
- If largest >= 2 × second_largest, it's automatically >= 2 × all smaller elements.
- Single pass finds both largest and second largest efficiently.
- None handling for second_largest covers case when only one element processed.

Time complexity

- Let n = length of nums array.
- Single pass through array: O(n).
- Each comparison and update: O(1).
- Overall time complexity: O(n).

Space complexity

- Only storing two indices (largest, second_largest).
- Space complexity: O(1).

Thought process and trade-offs

- Key insight: only need to compare with second largest, not all elements.
- One-pass solution is optimal for this problem.
- Alternative: find max, remove it, find max again - requires two passes or copying array.
- Alternative: sort array and compare last two - O(n log n) time.
- Current approach: optimal O(n) time with O(1) space.
- Handles edge cases: single element array returns 0 (vacuously true).

### Complexity Analysis

- **Time Complexity**: - Let n = length of nums array. - Single pass through array: O(n). - Each comparison and update: O(1). - Overall time complexity: O(n). Space complexity - Only storing two indices (largest, second_largest). - Space complexity: O(1). Thought process and trade-offs - Key insight: only need to compare with second largest, not all elements. - One-pass solution is optimal for this problem. - Alternative: find max, remove it, find max again - requires two passes or copying array. - Alternative: sort array and compare last two - O(n log n) time. - Current approach: optimal O(n) time with O(1) space. - Handles edge cases: single element array returns 0 (vacuously true).
- **Space Complexity**: - Only storing two indices (largest, second_largest). - Space complexity: O(1). Thought process and trade-offs - Key insight: only need to compare with second largest, not all elements. - One-pass solution is optimal for this problem. - Alternative: find max, remove it, find max again - requires two passes or copying array. - Alternative: sort array and compare last two - O(n log n) time. - Current approach: optimal O(n) time with O(1) space. - Handles edge cases: single element array returns 0 (vacuously true).

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space

# Distribute Candies

## Problem Summary

- Given an integer array of candy types, you have n candies where n is even.
- You can eat n/2 candies. Return the maximum number of different candy types you can eat.
- Example: [1,1,2,2,3,3] -> can eat 3, unique types = 3, so return 3.

Current implementation (in repository)

- Implementation uses set and comparison:
  - Converts candy array to set to get unique candy types.
  - Compares number of unique types with maximum eatable (n/2).
  - Returns minimum of the two values.
- Example code:
  ```python
  return min(len(set(candyType)), len(candyType) // 2)
  ```

Why this works

- Set automatically deduplicates, giving count of unique candy types.
- Maximum diversity = min(unique types available, maximum you can eat).
- If unique types < n/2: limited by variety available.
- If unique types >= n/2: can eat n/2 different types, reaching maximum allowed.

Time complexity

- Let n = length of candyType array.
- Creating set: O(n) for iterating through array and adding to set.
- len() operations: O(1).
- Overall time complexity: O(n).

Space complexity

- Set stores unique elements: O(k) where k is number of unique types, k <= n.
- Worst case: O(n) when all types are different.
- Overall space complexity: O(n).

Thought process and trade-offs

- Mathematical insight: answer is always min(unique_types, n/2).
- Clean one-liner solution leveraging Python's set data structure.
- Alternative: use Counter to count types, but set is sufficient since we only need count of unique types.
- No need to track which specific types to eat, only the count.
- Trade-off: creating set uses O(n) space, but provides O(1) lookup and automatic deduplication.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  return min(len(set(candyType)), len(candyType) // 2)
  ```

### How It Works

Step-by-step explanation of the approach.

### Why Iteration Works

- Set automatically deduplicates, giving count of unique candy types.
- Maximum diversity = min(unique types available, maximum you can eat).
- If unique types < n/2: limited by variety available.
- If unique types >= n/2: can eat n/2 different types, reaching maximum allowed.

Time complexity

- Let n = length of candyType array.
- Creating set: O(n) for iterating through array and adding to set.
- len() operations: O(1).
- Overall time complexity: O(n).

Space complexity

- Set stores unique elements: O(k) where k is number of unique types, k <= n.
- Worst case: O(n) when all types are different.
- Overall space complexity: O(n).

Thought process and trade-offs

- Mathematical insight: answer is always min(unique_types, n/2).
- Clean one-liner solution leveraging Python's set data structure.
- Alternative: use Counter to count types, but set is sufficient since we only need count of unique types.
- No need to track which specific types to eat, only the count.
- Trade-off: creating set uses O(n) space, but provides O(1) lookup and automatic deduplication.

### Complexity Analysis

- **Time Complexity**: - Let n = length of candyType array. - Creating set: O(n) for iterating through array and adding to set. - len() operations: O(1). - Overall time complexity: O(n). Space complexity - Set stores unique elements: O(k) where k is number of unique types, k <= n. - Worst case: O(n) when all types are different. - Overall space complexity: O(n). Thought process and trade-offs - Mathematical insight: answer is always min(unique_types, n/2). - Clean one-liner solution leveraging Python's set data structure. - Alternative: use Counter to count types, but set is sufficient since we only need count of unique types. - No need to track which specific types to eat, only the count. - Trade-off: creating set uses O(n) space, but provides O(1) lookup and automatic deduplication.
- **Space Complexity**: - Set stores unique elements: O(k) where k is number of unique types, k <= n. - Worst case: O(n) when all types are different. - Overall space complexity: O(n). Thought process and trade-offs - Mathematical insight: answer is always min(unique_types, n/2). - Clean one-liner solution leveraging Python's set data structure. - Alternative: use Counter to count types, but set is sufficient since we only need count of unique types. - No need to track which specific types to eat, only the count. - Trade-off: creating set uses O(n) space, but provides O(1) lookup and automatic deduplication.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space

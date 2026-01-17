# Largest Perimeter Triangle

## Problem Summary

- Given array of lengths, find the largest perimeter of a triangle that can be formed.
- Triangle inequality: sum of two smaller sides > largest side.
- Return perimeter, or 0 if no valid triangle.
- Example: [2,1,2] -> 5 (forms triangle with perimeter 2+1+2=5).

Current implementation (in repository)

- Implementation uses greedy approach with sorting:
  - Sorts array in ascending order.
  - Iterates from largest to smallest triplets.
  - Checks triangle inequality for each triplet.
  - Returns sum of first valid triangle found.
  - Returns 0 if no valid triangle exists.
- Example code:
  ```python
  nums.sort()
  for i in range(len(nums) - 1, 1, -1):
      if nums[i-2] + nums[i-1] > nums[i]:
          return nums[i-2] + nums[i-1] + nums[i]
  return 0
  ```

Why this works

- Sorting enables greedy selection: larger sides produce larger perimeter.
- Starting from largest values maximizes potential perimeter.
- Triangle inequality check: for sorted triplet [a, b, c] where a <= b <= c, only need to check a + b > c.
- Other inequalities automatically satisfied: a + c > b and b + c > a always true when a + b > c for sorted values.
- First valid triangle found has maximum perimeter.

Time complexity

- Let n = length of array.
- Sorting: O(n log n).
- Linear scan: O(n).
- Overall time complexity: O(n log n).

Space complexity

- Sorting in-place (Python's sort): O(1) auxiliary space.
- Space complexity: O(1).

Thought process and trade-offs

- Greedy with sorting: optimal approach for this problem.
- Key insight: largest valid triangle uses largest possible sides.
- Single inequality check sufficient: sorted property simplifies validation.
- Alternative: check all triplets without sorting - O(n³) time, much slower.
- Current approach: efficient and elegant.

## Approach: Greedy (Implemented)

### Strategy

The solution uses greedy to solve the problem efficiently.

```python
  nums.sort()
  for i in range(len(nums) - 1, 1, -1):
      if nums[i-2] + nums[i-1] > nums[i]:
          return nums[i-2] + nums[i-1] + nums[i]
  return 0
  ```

### How It Works

- Sorts array in ascending order.
  - Iterates from largest to smallest triplets.
  - Checks triangle inequality for each triplet.
  - Returns sum of first valid triangle found.
  - Returns 0 if no valid triangle exists.
- Example code:
  ```python
  nums.sort()
  for i in range(len(nums) - 1, 1, -1):
      if nums[i-2] + nums[i-1] > nums[i]:
          return nums[i-2] + nums[i-1] + nums[i]
  return 0
  ```

Why this works

- Sorting enables greedy selection: larger sides produce larger perimeter.
- Starting from largest values maximizes potential perimeter.
- Triangle inequality check: for sorted triplet [a, b, c] where a <= b <= c, only need to check a + b > c.
- Other inequalities automatically satisfied: a + c > b and b + c > a always true when a + b > c for sorted values.
- First valid triangle found has maximum perimeter.

Time complexity

- Let n = length of array.
- Sorting: O(n log n).
- Linear scan: O(n).
- Overall time complexity: O(n log n).

Space complexity

- Sorting in-place (Python's sort): O(1) auxiliary space.
- Space complexity: O(1).

Thought process and trade-offs

- Greedy with sorting: optimal approach for this problem.
- Key insight: largest valid triangle uses largest possible sides.
- Single inequality check sufficient: sorted property simplifies validation.
- Alternative: check all triplets without sorting - O(n³) time, much slower.
- Current approach: efficient and elegant.

### Why Greedy Works

- Sorting enables greedy selection: larger sides produce larger perimeter.
- Starting from largest values maximizes potential perimeter.
- Triangle inequality check: for sorted triplet [a, b, c] where a <= b <= c, only need to check a + b > c.
- Other inequalities automatically satisfied: a + c > b and b + c > a always true when a + b > c for sorted values.
- First valid triangle found has maximum perimeter.

Time complexity

- Let n = length of array.
- Sorting: O(n log n).
- Linear scan: O(n).
- Overall time complexity: O(n log n).

Space complexity

- Sorting in-place (Python's sort): O(1) auxiliary space.
- Space complexity: O(1).

Thought process and trade-offs

- Greedy with sorting: optimal approach for this problem.
- Key insight: largest valid triangle uses largest possible sides.
- Single inequality check sufficient: sorted property simplifies validation.
- Alternative: check all triplets without sorting - O(n³) time, much slower.
- Current approach: efficient and elegant.

### Complexity Analysis

- **Time Complexity**: - Let n = length of array. - Sorting: O(n log n). - Linear scan: O(n). - Overall time complexity: O(n log n). Space complexity - Sorting in-place (Python's sort): O(1) auxiliary space. - Space complexity: O(1). Thought process and trade-offs - Greedy with sorting: optimal approach for this problem. - Key insight: largest valid triangle uses largest possible sides. - Single inequality check sufficient: sorted property simplifies validation. - Alternative: check all triplets without sorting - O(n³) time, much slower. - Current approach: efficient and elegant.
- **Space Complexity**: - Sorting in-place (Python's sort): O(1) auxiliary space. - Space complexity: O(1). Thought process and trade-offs - Greedy with sorting: optimal approach for this problem. - Key insight: largest valid triangle uses largest possible sides. - Single inequality check sufficient: sorted property simplifies validation. - Alternative: check all triplets without sorting - O(n³) time, much slower. - Current approach: efficient and elegant.

### Advantages

- Efficient greedy solution
- Clear and maintainable code

### Disadvantages

- May require additional space

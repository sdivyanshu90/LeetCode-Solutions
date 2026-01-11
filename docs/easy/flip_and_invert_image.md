# Flipping an Image

## Problem Summary

- Given an m x n binary matrix (0s and 1s), flip each row horizontally then invert the image.
- Flip: reverse each row. Invert: replace 0 with 1 and 1 with 0.
- Example: [[1,1,0],[1,0,1],[0,0,0]] -> flip -> [[0,1,1],[1,0,1],[0,0,0]] -> invert -> [[1,0,0],[0,1,0],[1,1,1]].

Current implementation (in repository)

- Implementation performs flip and invert in two steps:
  - Flips each row using slice notation `row[::-1]` for all rows.
  - Iterates through all elements and inverts: 0 becomes 1, 1 becomes 0.
  - Returns the modified matrix.
- Example code:
  ```python
  arr = [row[::-1] for row in image]
  for i in range(len(arr)):
      for j in range(len(arr[0])):
          arr[i][j] = 1 if arr[i][j] == 0 else 0
  ```

Why this works

- List slicing with [::-1] reverses each row efficiently (flipping horizontally).
- Nested loops access each element for inversion.
- Conditional assignment inverts binary values.
- Two-step process clearly separates flip and invert operations.

Time complexity

- Let m = number of rows, n = number of columns.
- Flipping all rows: O(m × n) for creating reversed rows.
- Inverting all elements: O(m × n) for nested loop iteration.
- Overall time complexity: O(m × n).

Space complexity

- New array arr stores all elements: O(m × n).
- Space complexity: O(m × n).

Thought process and trade-offs

- Two-pass approach: clear and maintainable.
- Alternative (commented in code): combine flip and invert in single pass using XOR (row[i] ^= 1) - more efficient, single pass.
- Alternative: in-place with two pointers per row - O(1) extra space.
- Current approach: prioritizes readability over optimization.
- For interview: mention XOR optimization or in-place approach as follow-up.

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
  arr = [row[::-1] for row in image]
  for i in range(len(arr)):
      for j in range(len(arr[0])):
          arr[i][j] = 1 if arr[i][j] == 0 else 0
  ```

### How It Works

- Alternative (commented in code): combine flip and invert in single pass using XOR (row[i] ^= 1) - more efficient, single pass.
- Alternative: in-place with two pointers per row - O(1) extra space.
- Current approach: prioritizes readability over optimization.
- For interview: mention XOR optimization or in-place approach as follow-up.

### Why Two Pointers Works

- List slicing with [::-1] reverses each row efficiently (flipping horizontally).
- Nested loops access each element for inversion.
- Conditional assignment inverts binary values.
- Two-step process clearly separates flip and invert operations.

Time complexity

- Let m = number of rows, n = number of columns.
- Flipping all rows: O(m × n) for creating reversed rows.
- Inverting all elements: O(m × n) for nested loop iteration.
- Overall time complexity: O(m × n).

Space complexity

- New array arr stores all elements: O(m × n).
- Space complexity: O(m × n).

Thought process and trade-offs

- Two-pass approach: clear and maintainable.
- Alternative (commented in code): combine flip and invert in single pass using XOR (row[i] ^= 1) - more efficient, single pass.
- Alternative: in-place with two pointers per row - O(1) extra space.
- Current approach: prioritizes readability over optimization.
- For interview: mention XOR optimization or in-place approach as follow-up.

### Complexity Analysis

- **Time Complexity**: - Let m = number of rows, n = number of columns. - Flipping all rows: O(m × n) for creating reversed rows. - Inverting all elements: O(m × n) for nested loop iteration. - Overall time complexity: O(m × n). Space complexity - New array arr stores all elements: O(m × n). - Space complexity: O(m × n). Thought process and trade-offs - Two-pass approach: clear and maintainable. - Alternative (commented in code): combine flip and invert in single pass using XOR (row[i] ^= 1) - more efficient, single pass. - Alternative: in-place with two pointers per row - O(1) extra space. - Current approach: prioritizes readability over optimization. - For interview: mention XOR optimization or in-place approach as follow-up.
- **Space Complexity**: - New array arr stores all elements: O(m × n). - Space complexity: O(m × n). Thought process and trade-offs - Two-pass approach: clear and maintainable. - Alternative (commented in code): combine flip and invert in single pass using XOR (row[i] ^= 1) - more efficient, single pass. - Alternative: in-place with two pointers per row - O(1) extra space. - Current approach: prioritizes readability over optimization. - For interview: mention XOR optimization or in-place approach as follow-up.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space

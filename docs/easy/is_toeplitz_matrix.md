# Toeplitz Matrix

Problem summary

- Matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
- Return true if matrix is Toeplitz.
- Example: [[1,2,3,4],[5,1,2,3],[9,5,1,2]] -> True.

Current implementation (in repository)

- Implementation compares each element with its diagonal predecessor:
  - Iterates through all elements starting from position (1,1).
  - For each element at (i,j), checks if it equals element at (i-1,j-1).
  - Returns False immediately if any mismatch found.
  - Returns True if all elements match their diagonal predecessors.
- Example code:
  ```python
  for i in range(1, len(matrix)):
      for j in range(1, len(matrix[0])):
          if matrix[i][j] != matrix[i - 1][j - 1]:
              return False
  return True
  ```

Why this works

- Toeplitz property: each element should equal its upper-left neighbor.
- Starting from (1,1) ensures predecessor (i-1,j-1) always exists.
- First row and first column automatically satisfy property (no predecessors to check).
- Checking all elements ensures all diagonals are verified.

Time complexity

- Let m = number of rows, n = number of columns.
- Nested loops iterate through (m-1) × (n-1) elements.
- Each comparison is O(1).
- Overall time complexity: O(m × n).

Space complexity

- No additional data structures used.
- Space complexity: O(1).

Thought process and trade-offs

- Element-wise comparison: simple and efficient single-pass solution.
- Alternative: extract each diagonal and check if all elements equal - more complex, same complexity.
- Alternative: for each diagonal starting point, verify entire diagonal - requires identifying all starting points.
- Current approach: optimal and intuitive.
- Early termination: returns False immediately on first mismatch.

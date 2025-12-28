# Image Smoother

Problem summary

- Given an m x n image matrix, return a smoothed image.
- For each cell, smoothed value = floor average of the cell and its 8 neighbors (or fewer at edges).
- Example: [[1,1,1],[1,0,1],[1,1,1]] -> [[0,0,0],[0,0,0],[0,0,0]].

Current implementation (in repository)

- Implementation manually checks all 8 directions plus center:
  - Creates result matrix of same dimensions.
  - For each cell, initializes sum with current cell value and counter = 1.
  - Checks all 8 directions (up, down, left, right, and diagonals) with bounds checking.
  - Adds valid neighbor values to sum and increments counter.
  - Sets result cell to integer division sum // counter.
- Example code:
  ```python
  _sum = img[r][c]
  counter = 1
  if r - 1 >= 0:
      counter += 1
      _sum += img[r-1][c]
      # ... check diagonals
  res[r][c] = _sum // counter
  ```

Why this works

- Bounds checking ensures only valid cells are included in average.
- Counter tracks actual number of cells included (varies at edges/corners).
- Integer division gives floor of average as required.
- All 9 positions (center + 8 neighbors) are considered when valid.

Time complexity

- Let m = rows, n = columns.
- For each cell: O(9) = O(1) to check all neighbors.
- Total: O(m × n × 1) = O(m × n).

Space complexity

- Result matrix: O(m × n).
- Space complexity: O(m × n).

Thought process and trade-offs

- Manual direction checking: explicit but verbose.
- Alternative: use direction arrays [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)] to loop through neighbors - cleaner code, same complexity.
- Current approach: clear logic but repetitive.
- Trade-off: code length vs. readability.

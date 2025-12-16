# Pascal's Triangle II — Explanation, Approach, Complexity

Problem summary

- Given an integer `rowIndex`, return the rowIndex-th row of Pascal's Triangle (0-indexed).
- Each element in a row is the sum of the two elements above it.
- Example: rowIndex = 3 → [1, 3, 3, 1]

Approach (space-optimized in-place update)

- Initialize a result array `res` of size rowIndex + 1, filled with 1s (all elements default to 1).
- Iterate from row i = 1 to rowIndex.
  - Within each row, iterate j from i-1 down to 1 (reverse order is crucial).
  - Update `res[j] += res[j-1]` (current element = element above + element to the left above).
- **Key insight**: by updating in reverse order (right to left), we reuse the same array without needing a separate temporary row.
- Return the result array.

Why this works (mathematical insight)

- Pascal's Triangle follows the property: element[i][j] = element[i-1][j-1] + element[i-1][j].
- By updating from right to left within a row, `res[j-1]` still contains the previous row's value (not yet updated).
- This allows us to compute the new row in-place using only O(rowIndex) space.

Time and space complexity

- Time: O(rowIndex²) — outer loop: rowIndex iterations; inner loop: ~i iterations per iteration.
  - Total: 1 + 2 + 3 + ... + rowIndex = rowIndex × (rowIndex + 1) / 2 ≈ O(rowIndex²).
- Space: O(1) auxiliary space (excluding the output array). The result array uses O(rowIndex) space, which is necessary for the output.

Key insight: reverse iteration

- Updating from left to right would overwrite values we still need (from the previous row).
- Example for rowIndex = 3:
  - Start: res = [1, 1, 1, 1]
  - After i=1: res = [1, 2, 1, 1] (res[1] += res[0])
  - After i=2 (right to left): res = [1, 3, 3, 1]
    - res[2] += res[1]: [1, 2, 3, 1] (uses updated res[1])
    - res[1] += res[0]: [1, 3, 3, 1]
  - Reverse order ensures res[j-1] reflects the previous row's value, not the current row's.

Edge cases

- rowIndex = 0 → return [1] (first row of Pascal's Triangle).
- rowIndex = 1 → return [1, 1] (second row).
- Large rowIndex (e.g., 30): O(rowIndex²) time is acceptable; output size is O(rowIndex).
- Integer overflow: binomial coefficients can grow large; Python handles arbitrary-precision integers, so no overflow.

Example testcases (from repository)

- rowIndex = 3 → [1, 3, 3, 1]
- rowIndex = 0 → [1]
- rowIndex = 1 → [1, 1]
- rowIndex = 4 → [1, 4, 6, 4, 1]
- rowIndex = 5 → [1, 5, 10, 10, 5, 1]

Alternative approaches

- Two-pass iterative (separate rows):

  ```python
  prev_row = [1]
  for i in range(1, rowIndex + 1):
      curr_row = [1]
      for j in range(1, i):
          curr_row.append(prev_row[j-1] + prev_row[j])
      curr_row.append(1)
      prev_row = curr_row
  return prev_row
  ```

  Time: O(rowIndex²), Space: O(rowIndex) for prev/curr rows.
  Less space-efficient but clearer and easier to understand.

- Binomial coefficient formula (direct computation):
  ```python
  from math import comb
  return [comb(rowIndex, i) for i in range(rowIndex + 1)]
  ```
  Time: O(rowIndex²) for computing comb efficiently, or O(rowIndex · log rowIndex) for optimized implementations.
  Space: O(rowIndex) for output.
  Most concise but relies on built-in function (available in Python 3.8+).

Thought process / design choices

- The current approach is optimal in terms of space complexity: O(1) auxiliary (plus output).
- The in-place update strategy is elegant and efficient.
- Reverse iteration is a classic technique for in-place array updates.
- This approach generalizes well to other dynamic programming problems.

Common pitfalls

- Iterating left-to-right instead of right-to-left → overwrites values needed for computation.
- Forgetting to start j from i-1 (should skip the first and last elements, which remain 1) → causes incorrect values.
- Off-by-one errors in loop bounds → careful with range(1, rowIndex + 1) and range(i - 1, 0, -1).
- Using j from 0 or j from i (inclusive) → would compute 1 + 1 = 2 at the boundaries, incorrect.

Correctness proof

- By induction on rowIndex, assume res correctly represents row i-1 before iteration i.
- During iteration i, updating res[j] = res[j] + res[j-1] for j from i-1 down to 1 computes the correct values for row i.
- Base case: rowIndex = 0 returns [1] (correct).
- After all iterations, res contains row rowIndex (correct).

Notes

- This is a space-optimized version of the Pascal's Triangle generation problem.
- The reverse iteration trick is a useful technique for in-place DP updates.
- The solution is optimal and elegant; widely used in competitive programming and interviews.

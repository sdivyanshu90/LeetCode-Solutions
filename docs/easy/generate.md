# Pascal's Triangle — Explanation, Approach, Complexity

Problem summary

- Given an integer `numRows`, generate the first `numRows` rows of Pascal's Triangle.
- Pascal's Triangle is a triangular array where each element is the sum of the two elements above it (or 1 on the edges).
- Each row i contains i+1 elements.
- Example: numRows = 5 → [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Approach (binomial coefficient formula)

- For row i (0-indexed), each element at position j is the binomial coefficient C(i, j).
- Use the combinatorial formula: C(i, j) = i! / (j! × (i-j)!)
- Compute using the factorial function from the math module.
- Iterate from row 0 to numRows-1; within each row, compute elements from column 0 to i.

Why this works (mathematical insight)

- Pascal's Triangle is directly related to binomial coefficients. The element at row i, column j equals C(i, j).
- This formula is mathematically rigorous and guarantees correct values.
- The factorial approach is straightforward to implement.

Time complexity

- Naive analysis: O(numRows^2 × k) where k is the time to compute a factorial.
  - Computing i! takes O(i) time (iterative multiplication).
  - For row i, computing factorials takes O(i) time per element, and there are i+1 elements.
  - Total per row: O(i^2).
  - Summing over all rows: O(1^2 + 2^2 + ... + numRows^2) = O(numRows^3).

**⚠️ Inefficiency notice and optimization**

The current approach is **inefficient** due to repeated factorial computations. Here are better approaches:

**Approach 1: Dynamic Programming (Recommended)**

- Each element is the sum of the two elements above it.
- Implement iteratively from top to bottom:
  ```python
  def generate(self, numRows: int) -> List[List[int]]:
      res = []
      for i in range(numRows):
          row = [1] * (i + 1)
          for j in range(1, i):
              row[j] = res[i-1][j-1] + res[i-1][j]
          res.append(row)
      return res
  ```
- Time: O(numRows^2) — each element computed once from two previous elements.
- Space: O(numRows^2) for the output.

**Approach 2: Incremental Row Building**

- Build each row from the previous row by shifting and adding.
- Time: O(numRows^2).
- Space: O(numRows) auxiliary (reusing a single row array).

**Approach 3: Optimized Binomial Coefficient**

- Avoid recalculating factorials; use the recurrence: C(i, j) = C(i, j-1) × (i-j+1) / j.
  ```python
  def generate(self, numRows: int) -> List[List[int]]:
      res = []
      for i in range(numRows):
          row = [1]
          for j in range(1, i + 1):
              row.append(row[-1] * (i - j + 1) // j)
          res.append(row)
      return res
  ```
- Time: O(numRows^2) — each element computed in O(1) using the previous element.
- Space: O(numRows^2) for output.

Space complexity

- Current implementation: O(numRows^2) for the output triangle. Auxiliary space: O(1) (excluding output).

Edge cases

- numRows = 0 → return [] (empty list).
- numRows = 1 → return [[1]] (single row with one element).
- Large numRows (e.g., 30): factorial computation becomes expensive and causes large integer operations. DP approach handles this better.

Example testcases (from repository)

- numRows = 5 → [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
- numRows = 1 → [[1]]
- numRows = 0 → []
- numRows = 3 → [[1], [1, 1], [1, 2, 1]]
- numRows = 6 → [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

Mathematical properties of Pascal's Triangle

- Symmetry: row i is symmetric (C(i, j) = C(i, i-j)).
- Row sums: sum of row i = 2^i.
- Diagonal patterns: diagonals represent triangular numbers, tetrahedral numbers, etc.

Thought process / design choices

- The current factorial-based approach is mathematically elegant but computationally inefficient.
- The DP approach is more practical for typical problem constraints.
- The optimized binomial coefficient recurrence is the best balance of clarity and efficiency.

Recommendation

- **Use Approach 1 (DP)** for clarity and efficiency — most straightforward and widely taught.
- **Use Approach 3** if you want to demonstrate understanding of binomial coefficients and mathematical optimization.
- Avoid the factorial approach for large numRows due to O(numRows^3) complexity.

Notes

- Pascal's Triangle has many interesting properties and applications in combinatorics, probability, and algebra.
- The solution is foundational for understanding dynamic programming and combinatorial mathematics.
- The triangle is named after Blaise Pascal, though it was known to mathematicians centuries earlier.

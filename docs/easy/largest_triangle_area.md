# Largest Triangle Area

Problem summary

- Given array of 2D points, find the maximum area of any triangle formed by 3 of these points.
- Use coordinate geometry to calculate triangle area.
- Example: [[0,0],[0,1],[1,0],[0,2],[2,0]] -> 2.0.

Current implementation (in repository)

- Implementation uses brute force with area formula:
  - Triple nested loops to try all possible combinations of 3 points.
  - For each triplet, calculates area using determinant formula.
  - Formula: |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2.
  - Tracks and returns maximum area found.
- Example code:
  ```python
  for i in range(n):
      for j in range(i+1, n):
          for k in range(j+1, n):
              x1, y1 = points[i]
              x2, y2 = points[j]
              x3, y3 = points[k]
              area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
              max_area = max(max_area, area)
  ```

Why this works

- Determinant formula calculates signed area of triangle directly from coordinates.
- Absolute value ensures positive area.
- Division by 2 gives actual area (determinant gives twice the area).
- Checking all combinations guarantees finding maximum.

Time complexity

- Let n = number of points.
- Three nested loops: C(n,3) = n×(n-1)×(n-2)/6 combinations.
- Each area calculation: O(1).
- Overall time complexity: O(n³).

Space complexity

- Only using variables for coordinates and max tracking.
- Space complexity: O(1).

Thought process and trade-offs

- Brute force approach: straightforward and correct for small to medium n.
- Determinant formula: mathematically elegant, avoids separate base/height calculation.
- For n <= 50 (typical constraint), O(n³) is acceptable.
- More sophisticated algorithms exist (convex hull-based) but add complexity.
- Current approach: optimal for simplicity given typical constraints.

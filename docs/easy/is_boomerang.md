# Valid Boomerang

Problem summary

- Given three points in 2D plane, return true if they form a boomerang (not collinear).
- Three points are collinear if they lie on the same straight line.
- Example: [[1,1],[2,3],[3,2]] -> True (not on same line).

Current implementation (in repository)

- Implementation uses cross product approach:
  - First checks if any two points are identical (would be degenerate).
  - Calculates cross product to check collinearity.
  - Uses formula: (y2-y1) × (x3-x2) ≠ (y3-y2) × (x2-x1).
  - Returns True if cross products are not equal (points not collinear).
- Example code:
  ```python
  if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):
      return False
  return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
  ```

Why this works

- Three points are collinear if slopes between point pairs are equal.
- Slope formula: (y2-y1)/(x2-x1), but division can cause issues with vertical lines.
- Cross product avoids division: rearrange slope equality to multiplication.
- If slopes equal: (y2-y1)/(x2-x1) = (y3-y2)/(x3-x2), then (y2-y1)(x3-x2) = (y3-y2)(x2-x1).
- Not equal cross products means different slopes, thus not collinear.

Time complexity

- Constant number of operations: coordinate access, multiplication, comparison.
- Time complexity: O(1).

Space complexity

- Only using a few variables for coordinates.
- Space complexity: O(1).

Thought process and trade-offs

- Cross product method: mathematically elegant, avoids division by zero issues.
- Alternative: calculate slopes directly with special case for vertical lines - more cases to handle.
- Alternative: use area formula (area = 0 for collinear points) - equivalent to cross product.
- Current approach: clean and handles all edge cases naturally.
- Duplicate point check: necessary to avoid degenerate case (two identical points don't form a valid boomerang).

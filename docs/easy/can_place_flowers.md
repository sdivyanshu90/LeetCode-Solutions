# Can Place Flowers

Problem summary

- Given a flowerbed array (0 = empty, 1 = planted) and n flowers to plant.
- Flowers cannot be planted in adjacent plots.
- Return true if n flowers can be planted without violating the no-adjacent rule.
- Example: [1,0,0,0,1], n = 1 -> True (can plant at index 2).

Current implementation (in repository)

- Implementation uses greedy single-pass approach:
  - Iterates through flowerbed from left to right.
  - For each position, checks if current plot is empty AND neighbors are empty (or don't exist).
  - If conditions met, plants flower (sets to 1) and decrements n.
  - Returns early with True if n becomes <= 0.
  - Returns False if loop completes without planting all flowers.
- Example code:
  ```python
  if (i == 0 or flowerbed[i - 1] == 0) and flowerbed[i] == 0 and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
      flowerbed[i] = 1
      n -= 1
  ```

Why this works

- Greedy approach: plant as soon as possible maximizes opportunities for remaining flowers.
- Three conditions ensure validity: current empty, left empty (or boundary), right empty (or boundary).
- Modifying array in-place tracks planting state for subsequent iterations.
- Early return optimization exits as soon as all flowers are planted.

Time complexity

- Let m = length of flowerbed.
- Single pass through flowerbed: O(m).
- Each position check is O(1).
- Overall time complexity: O(m).

Space complexity

- In-place modification of flowerbed array.
- No additional data structures.
- Space complexity: O(1).

Thought process and trade-offs

- Greedy strategy works because planting earlier never hurts future placements.
- Boundary handling: `i == 0` and `i == len(flowerbed) - 1` handle edge positions without separate logic.
- Alternative: calculate maximum plantable positions first, then compare with n - requires same O(m) time but doesn't modify input.
- Current approach modifies input, which may not be desirable in all scenarios, but problem doesn't specify preservation requirement.

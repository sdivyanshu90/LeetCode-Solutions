# Available Captures for Rook

## Problem Summary

- Given 8x8 board with one rook 'R', pawns 'p', bishops 'B', and empty '.'.
- Count how many pawns the rook can capture.
- Rook moves in 4 directions until hitting edge, bishop, or pawn (captures pawn).
- Example: rook can capture pawns in its row/column if no bishop blocks.

Current implementation (in repository)

- Implementation searches in four directions:
  - Finds rook position by scanning board.
  - Defines four direction vectors: up, down, left, right.
  - For each direction, moves step by step until boundary.
  - Stops if hits bishop 'B' (blocked).
  - Counts and stops if hits pawn 'p' (capture).
  - Returns total captures.
- Example code:
  ```python
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for dx, dy in directions:
      x, y = rook_x, rook_y
      while 0 <= x + dx < 8 and 0 <= y + dy < 8:
          x += dx
          y += dy
          if board[x][y] == 'B':
              break
          if board[x][y] == 'p':
              captures += 1
              break
  ```

Why this works

- Four directions cover all possible rook moves (orthogonal).
- Step-by-step movement simulates rook traversal.
- Bishop stops search in that direction (blocking).
- Pawn capture increments count and stops (can't move through captured piece).
- Boundary check prevents out-of-bounds access.

Time complexity

- Finding rook: O(64) = O(1) for 8x8 board.
- Four directions: each scans up to 7 squares = O(7) = O(1).
- Overall time complexity: O(1) for fixed board size.

Space complexity

- Only using position variables and counter.
- Space complexity: O(1).

Thought process and trade-offs

- Direction vector approach: clean and extensible pattern for movement problems.
- Fixed board size: simplifies complexity analysis (always 8x8).
- Early termination: stops at first obstacle in each direction.
- Could optimize: combine directions into single loop, but current approach is clearer.

## Approach: Frequency Counting (Implemented)

### Strategy

The solution uses frequency counting to solve the problem efficiently.

```python
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for dx, dy in directions:
      x, y = rook_x, rook_y
      while 0 <= x + dx < 8 and 0 <= y + dy < 8:
          x += dx
          y += dy
          if board[x][y] == 'B':
              break
          if board[x][y] == 'p':
              captures += 1
              break
  ```

### How It Works

- Fixed board size: simplifies complexity analysis (always 8x8).
- Early termination: stops at first obstacle in each direction.
- Could optimize: combine directions into single loop, but current approach is clearer.

### Why Frequency Counting Works

- Four directions cover all possible rook moves (orthogonal).
- Step-by-step movement simulates rook traversal.
- Bishop stops search in that direction (blocking).
- Pawn capture increments count and stops (can't move through captured piece).
- Boundary check prevents out-of-bounds access.

Time complexity

- Finding rook: O(64) = O(1) for 8x8 board.
- Four directions: each scans up to 7 squares = O(7) = O(1).
- Overall time complexity: O(1) for fixed board size.

Space complexity

- Only using position variables and counter.
- Space complexity: O(1).

Thought process and trade-offs

- Direction vector approach: clean and extensible pattern for movement problems.
- Fixed board size: simplifies complexity analysis (always 8x8).
- Early termination: stops at first obstacle in each direction.
- Could optimize: combine directions into single loop, but current approach is clearer.

### Complexity Analysis

- **Time Complexity**: - Finding rook: O(64) = O(1) for 8x8 board. - Four directions: each scans up to 7 squares = O(7) = O(1). - Overall time complexity: O(1) for fixed board size. Space complexity - Only using position variables and counter. - Space complexity: O(1). Thought process and trade-offs - Direction vector approach: clean and extensible pattern for movement problems. - Fixed board size: simplifies complexity analysis (always 8x8). - Early termination: stops at first obstacle in each direction. - Could optimize: combine directions into single loop, but current approach is clearer.
- **Space Complexity**: - Only using position variables and counter. - Space complexity: O(1). Thought process and trade-offs - Direction vector approach: clean and extensible pattern for movement problems. - Fixed board size: simplifies complexity analysis (always 8x8). - Early termination: stops at first obstacle in each direction. - Could optimize: combine directions into single loop, but current approach is clearer.

### Advantages

- Efficient frequency counting solution
- Clear and maintainable code

### Disadvantages

- May require additional space

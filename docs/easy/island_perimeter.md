# Island Perimeter

## Problem Summary

You are given `row x col` grid representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island). One cell is a square with side length 1. Return the perimeter of the island.

**LeetCode Problem**: [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/)

**LeetCode Problem**: [Island Perimeter](https://leetcode.com/problems/island-perimeter/)

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def islandPerimeter(self, grid: List[List[int]]) -> int:
    per = 0
    for i, j in product(range(len(grid)), range(len(grid[0]))):
        if grid[i][j] == 1:
            per += (i == 0 or grid[i-1][j] == 0)
            per += (j == 0 or grid[i][j-1] == 0)
    return per*2
```

### How It Works

For each land cell at position (i, j), check:

- **Top edge** exposed? → `i == 0` (top boundary) OR `grid[i-1][j] == 0` (water above)
- **Left edge** exposed? → `j == 0` (left boundary) OR `grid[i][j-1] == 0` (water to left)

**Why multiply by 2?**

- We only check 2 of the 4 sides (top and left)
- By symmetry, the bottom and right sides contribute equally
- Total perimeter = 2 × (top + left edges)

### Why DFS Works

**Key insight**: Each exposed edge is counted exactly once:

- Checking top/left of each cell counts each exposed edge once
- Internal edges (shared between two land cells) are never counted
- Boundary edges (facing water or grid edge) are counted once
- Multiplying by 2 accounts for all 4 directions

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space

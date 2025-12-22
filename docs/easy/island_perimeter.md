# Island Perimeter

## Problem Summary

You are given `row x col` grid representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island). One cell is a square with side length 1. Return the perimeter of the island.

**LeetCode Problem**: [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/)

## Approach 1: Count Edges (Implemented)

### Strategy

The implemented solution uses a **clever counting approach**:

1. For each land cell, count how many edges are exposed to water or grid boundary
2. Check only the **top** and **left** edges of each cell
3. Multiply the count by 2 (since we only checked 2 of 4 sides)
4. This avoids double-counting shared edges

**Code**:

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

### Visual Example

```
Grid:
  0 1 2 3
0 [0,1,0,0]
1 [1,1,1,0]
2 [0,1,0,0]
3 [1,1,0,0]

Cell (0,1): Land
  - Top edge: i==0 ✓ (count += 1)
  - Left edge: grid[0][0]==0 ✓ (count += 1)
  - Contributes: 2 edges

Cell (1,0): Land
  - Top edge: grid[0][0]==0 ✓ (count += 1)
  - Left edge: j==0 ✓ (count += 1)
  - Contributes: 2 edges

Cell (1,1): Land
  - Top edge: grid[0][1]==1 ✗ (count += 0)
  - Left edge: grid[1][0]==1 ✗ (count += 0)
  - Contributes: 0 edges

... (continue for all land cells)

Total count = 8
Perimeter = 8 × 2 = 16
```

### Why This Works

**Key insight**: Each exposed edge is counted exactly once:

- Checking top/left of each cell counts each exposed edge once
- Internal edges (shared between two land cells) are never counted
- Boundary edges (facing water or grid edge) are counted once
- Multiplying by 2 accounts for all 4 directions

### Complexity Analysis

- **Time Complexity**: O(m × n) - Visit each cell once
- **Space Complexity**: O(1) - Only using counter variable

### Edge Cases Handled

- **Single cell island**: `[[1]]` → 4 (all edges exposed)
- **Island at corner**: Correctly counts boundary edges
- **Island at edge**: Works for any position
- **Complex shapes**: Handles any connected island shape

## Approach 2: Count All Four Sides

The more intuitive but verbose approach - check all 4 directions:

```python
def islandPerimeter(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 directions
                if i == 0 or grid[i-1][j] == 0:  # Top
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1

    return perimeter
```

### Complexity

- **Time**: O(m × n)
- **Space**: O(1)

### When to Use

- When clarity is more important than brevity
- When the multiplication trick seems too clever
- For easier debugging (can see each edge contribution)

## Approach 3: Formula (4 × islands - 2 × neighbors)

Mathematical approach based on counting land cells and shared edges:

```python
def islandPerimeter(self, grid: List[List[int]]) -> int:
    islands = 0
    neighbors = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                islands += 1

                # Count neighbors (to avoid double counting, only check right and down)
                if i < len(grid) - 1 and grid[i+1][j] == 1:
                    neighbors += 1
                if j < len(grid[0]) - 1 and grid[i][j+1] == 1:
                    neighbors += 1

    return 4 * islands - 2 * neighbors
```

### How It Works

**Formula**: `Perimeter = 4 × (number of land cells) - 2 × (number of adjacent pairs)`

**Reasoning**:

- Each land cell contributes 4 edges initially
- Each shared edge between two land cells reduces perimeter by 2 (1 from each cell)
- Count adjacent pairs by checking right and down (avoids double counting)

### Example

```
[1,1]
[1,1]

Islands = 4
Neighbors = 4 (top-right: 1, top-down: 1, bottom-right: 1, left-down: 1)
Wait, checking only right and down:
  - (0,0) → right (0,1): 1
  - (0,0) → down (1,0): 1
  - (0,1) → down (1,1): 1
  - (1,0) → right (1,1): 1
  Total neighbors = 4

Perimeter = 4×4 - 2×4 = 16 - 8 = 8 ✓
```

### Complexity

- **Time**: O(m × n)
- **Space**: O(1)

### Advantages

- Elegant mathematical formula
- Clear logic (each cell has 4 edges, subtract shared edges)
- Easy to understand once you know the formula

## Approach 4: DFS/BFS

Using graph traversal (overkill for this problem):

```python
def islandPerimeter(self, grid: List[List[int]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 1  # Hit water or boundary, count this edge

        if grid[i][j] == -1:  # Already visited
            return 0

        grid[i][j] = -1  # Mark as visited

        # Explore all 4 directions
        return (dfs(i-1, j) + dfs(i+1, j) +
                dfs(i, j-1) + dfs(i, j+1))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)

    return 0
```

### Complexity

- **Time**: O(m × n)
- **Space**: O(m × n) - Recursion stack and modifies grid

### Drawbacks

- Overly complex for this problem
- Modifies the input grid
- Uses extra space
- Not recommended

## Comparison of Approaches

| Approach          | Time   | Space  | Pros                       | Cons                    |
| ----------------- | ------ | ------ | -------------------------- | ----------------------- |
| Count Edges (×2)  | O(m×n) | O(1)   | Clever, concise, efficient | Less obvious logic      |
| Check All 4 Sides | O(m×n) | O(1)   | Clear, straightforward     | More verbose            |
| Formula           | O(m×n) | O(1)   | Elegant, mathematical      | Need to know formula    |
| DFS/BFS           | O(m×n) | O(m×n) | Graph traversal practice   | Overkill, modifies grid |

## Edge Cases & Considerations

1. **Single Cell Island**:

   ```
   [[1]]
   ```

   - Perimeter = 4
   - All edges exposed

2. **Single Row Island**:

   ```
   [[1,1,1]]
   ```

   - Perimeter = 8
   - Only top and bottom edges exposed, plus 2 end edges

3. **Square Island**:

   ```
   [[1,1],
    [1,1]]
   ```

   - Perimeter = 8
   - 4 cells, 4 shared edges

4. **L-Shaped Island**:

   ```
   [[1,0],
    [1,1]]
   ```

   - Perimeter = 8
   - More complex shape

5. **Island at Corner**:

   ```
   [[1,0,0],
    [0,0,0]]
   ```

   - Perimeter = 4
   - Correctly handles boundary

6. **Complex Shape**:
   ```
   [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]
   ```
   - Perimeter = 16
   - Implementation handles any shape

## Common Pitfalls

1. **Double Counting Edges**:

   ```python
   # WRONG: Counting all 4 sides of every land cell
   for each land cell:
       count += 4
   # This doesn't account for shared edges
   ```

2. **Not Checking Boundaries**:

   ```python
   # WRONG: Will cause IndexError
   if grid[i-1][j] == 0:
       count += 1
   # Must check: i == 0 or grid[i-1][j] == 0
   ```

3. **Forgetting to Check Water**:

   ```python
   # WRONG: Only checking boundaries
   if i == 0 or i == rows-1:
       count += 1
   # Must also check if neighbor is water
   ```

4. **Incorrect Multiplication Factor**:

   ```python
   # WRONG: Wrong multiplier
   return per * 4  # Should be per * 2
   ```

5. **Checking Same Edge Twice in Formula Approach**:
   ```python
   # WRONG: Double counting neighbors
   if grid[i-1][j] == 1:
       neighbors += 1
   if grid[i+1][j] == 1:
       neighbors += 1
   # Each neighbor would be counted twice
   # Only check right and down to avoid this
   ```

## Why the Implemented Solution is Clever

The key insight is recognizing that:

1. We can avoid checking all 4 sides by using **symmetry**
2. Only checking **top and left** is sufficient
3. The **bottom and right** contribute equally by symmetry
4. Multiply by 2 to get the full perimeter

This reduces code complexity while maintaining clarity once understood.

### Alternative Interpretation

Think of it as scanning the grid **twice** in concept:

- First pass: Count top/left edges
- Second pass: Count bottom/right edges (implicit via multiplication)

## Optimization Notes

All iterative approaches are **O(m × n)** time and **O(1)** space, which is optimal since we must examine every cell.

The implemented solution is optimal because:

- Single pass through the grid
- Minimal operations per cell
- No extra space
- Clean and concise

No further optimization is possible without changing the problem constraints.

## Test Cases

```python
# Basic square
grid = [[1,1],
        [1,1]]
islandPerimeter(grid)  # 8

# Single cell
grid = [[1]]
islandPerimeter(grid)  # 4

# Single row
grid = [[1,0]]
islandPerimeter(grid)  # 4

# Complex shape (from problem)
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
islandPerimeter(grid)  # 16

# L-shape
grid = [[1,0],
        [1,1]]
islandPerimeter(grid)  # 8

# Single cell in center
grid = [[0,0,0],
        [0,1,0],
        [0,0,0]]
islandPerimeter(grid)  # 4

# Linear island
grid = [[1,1,1,1]]
islandPerimeter(grid)  # 10

# T-shape
grid = [[1,1,1],
        [0,1,0]]
islandPerimeter(grid)  # 10

# All land
grid = [[1,1],
        [1,1]]
islandPerimeter(grid)  # 8
```

## Thought Process

The problem asks for the perimeter of an island in a grid. Key observations:

1. **Perimeter = exposed edges**: Count edges that face water or grid boundary
2. **Each land cell has 4 potential edges**: top, bottom, left, right
3. **Shared edges don't count**: Two adjacent land cells share an edge

**Naive approach**: For each land cell, check all 4 directions and count exposed edges. This works but checks every direction.

**Optimization**: Use symmetry!

- Only check 2 directions (top and left)
- The other 2 directions (bottom and right) contribute equally
- Multiply by 2 to get full perimeter

**Mathematical approach**: Recognize the formula:

- Start with 4 edges per land cell
- Subtract 2 for each adjacent pair (shared edge)
- `Perimeter = 4 × islands - 2 × neighbors`

All approaches are O(m × n) time and O(1) space, but the implemented solution is the most elegant.

## Related Problems

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
- [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/)

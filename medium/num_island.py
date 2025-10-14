import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r_new, c_new = row + dr, col + dc
                    if (r_new in range(n) and
                        c_new in range(m) and
                        grid[r_new][c_new] == "1" and
                        (r_new, c_new) not in visit):
                        
                        q.append((r_new, c_new))
                        visit.add((r_new, c_new))
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    
        return islands

def test_num_islands():
    s = Solution()

    # Test Case 1: Standard case with multiple islands
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(f"\n--- Test Case 1 ---")
    print("Input Grid:")
    for row in grid1: print(row)
    print(f"Output: {s.numIslands(grid1)}") # Expected: 3

    # Test Case 2: No islands (all water)
    grid2 = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    print(f"\n--- Test Case 2 ---")
    print("Input Grid:")
    for row in grid2: print(row)
    print(f"Output: {s.numIslands(grid2)}") # Expected: 0

    # Test Case 3: One large island
    grid3 = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    print(f"\n--- Test Case 3 ---")
    print("Input Grid:")
    for row in grid3: print(row)
    print(f"Output: {s.numIslands(grid3)}") # Expected: 1

    # Test Case 4: Empty grid (edge case)
    grid4 = []
    print(f"\n--- Test Case 4 ---")
    print(f"Input Grid: {grid4}")
    print(f"Output: {s.numIslands(grid4)}") # Expected: 0
    
    # Test Case 5: Islands that are long and thin
    grid5 = [
        ["1", "0", "0", "1"],
        ["1", "0", "0", "1"],
        ["1", "0", "0", "1"]
    ]
    print(f"\n--- Test Case 5 ---")
    print("Input Grid:")
    for row in grid5: print(row)
    print(f"Output: {s.numIslands(grid5)}") # Expected: 2

    # Test Case 6: Single row grid
    grid6 = [["1", "0", "1", "1", "0", "1"]]
    print(f"\n--- Test Case 6 ---")
    print(f"Input Grid: {grid6}")
    print(f"Output: {s.numIslands(grid6)}") # Expected: 3

    # Test Case 7: Single column grid
    grid7 = [["1"], ["0"], ["1"], ["1"]]
    print(f"\n--- Test Case 7 ---")
    print("Input Grid:")
    for row in grid7: print(row)
    print(f"Output: {s.numIslands(grid7)}") # Expected: 2

    # Test Case 8: Diagonal lands (not connected)
    grid8 = [
        ["1", "0", "0"],
        ["0", "1", "0"],
        ["0", "0", "1"]
    ]
    print(f"\n--- Test Case 8 ---")
    print("Input Grid:")
    for row in grid8: print(row)
    print(f"Output: {s.numIslands(grid8)}") # Expected: 3

    # Test Case 9: Single cell grid
    grid9 = [["1"]]
    print(f"\n--- Test Case 9 ---")
    print(f"Input Grid: {grid9}")
    print(f"Output: {s.numIslands(grid9)}") # Expected: 1

    # Test Case 10: A more complex shape (U-shape)
    grid10 = [
        ["1", "1", "1", "1", "0"],
        ["1", "0", "0", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(f"\n--- Test Case 10 ---")
    print("Input Grid:")
    for row in grid10: print(row)
    print(f"Output: {s.numIslands(grid10)}") # Expected: 2

# Run the test function
test_num_islands()
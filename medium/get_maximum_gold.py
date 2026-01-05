from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0

        def dfs_backtrack(grid, rows, cols, row, col):
            if row < 0 or col < 0 or row == rows or col == cols or \
                    grid[row][col] == 0:
                return 0
            max_gold = 0
            original_val = grid[row][col]
            grid[row][col] = 0
            for direction in range(4):
                max_gold = max(max_gold,
                               dfs_backtrack(grid, rows, cols, 
                                             DIRECTIONS[direction] + row,
                                             DIRECTIONS[direction + 1] + col))
            grid[row][col] = original_val
            return max_gold + original_val

        for row in range(rows):
            for col in range(cols):
                max_gold = max(max_gold, dfs_backtrack(grid, rows, cols, row, 
                                                       col))
        return max_gold

def test_get_maximum_gold():
    solution = Solution()

    # Test Case 1
    grid1 = [[0,6,0],[5,8,7],[0,9,0]]
    print(solution.getMaximumGold(grid1))  # Expected Output: 24

    # Test Case 2
    grid2 = [[1,0,7],[2,0,6],[3,4,5],[0,0,0],[9,0,20]]
    print(solution.getMaximumGold(grid2))  # Expected Output: 28

    # Test Case 3
    grid3 = [[0,0,0],[0,0,0],[0,0,0]]
    print(solution.getMaximumGold(grid3))  # Expected Output: 0

    # Test Case 4
    grid4 = [[10,33,13,15],[22,21,4,1],[5,0,2,3],[0,6,14,2]]
    print(solution.getMaximumGold(grid4))  # Expected Output: 149

    # Test Case 5
    grid5 = [[1]]
    print(solution.getMaximumGold(grid5))  # Expected Output: 1

test_get_maximum_gold()
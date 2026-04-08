from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid, sub_grid, lin, col):
            if sub_grid[lin][col] == 0:
                return False
            else:
                sub_grid[lin][col] = 0
                flag = True
                if grid[lin][col] == 0:
                    flag = False
                
                if lin - 1 >= 0 and sub_grid[lin - 1][col] == 1:
                    if not dfs(grid, sub_grid, lin - 1, col):
                        flag = False
                if lin + 1 < len(grid) and sub_grid[lin + 1][col] == 1:
                    if not dfs(grid, sub_grid, lin + 1, col):
                        flag = False
                if col - 1 >= 0 and sub_grid[lin][col - 1] == 1:
                    if not dfs(grid, sub_grid, lin, col - 1):
                        flag = False
                if col + 1 < len(grid[0]) and sub_grid[lin][col + 1] == 1:
                    if not dfs(grid, sub_grid, lin, col + 1):
                        flag = False
                
                return flag
        
        aux = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    if dfs(grid1, grid2, i, j):
                        aux += 1
        
        return aux

def test_count_sub_islands():
    solution = Solution()

    # Test case 1
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    print(solution.countSubIslands(grid1, grid2))  # Expected output: 3

    # Test case 2
    grid1 = [[1,0,1],[0,1,0],[1,0,1]]
    grid2 = [[0,0,0],[0,1,0],[0,0,0]]
    print(solution.countSubIslands(grid1, grid2))  # Expected output: 1

    # Test case 3
    grid1 = [[1,1,1],[1,0,1],[1,1,1]]
    grid2 = [[1,1,1],[1,0,1],[1,1,1]]
    print(solution.countSubIslands(grid1, grid2))  # Expected output: 1

    # Test case 4
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[0,0,0,0,0]]
    print(solution.countSubIslands(grid1, grid2))  # Expected output: 1

    # Test case 5
    grid1 = [[1,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0]]
    grid2 = [[1,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0]]
    print(solution.countSubIslands(grid1, grid2))  # Expected output: 2

test_count_sub_islands()
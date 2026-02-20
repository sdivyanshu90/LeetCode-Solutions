from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(1, rows):
            for c in range(cols):
                grid[r][c] += min(grid[r-1][prev_c] for prev_c in range(cols) if prev_c != c)
        
        return min(grid[-1])

def test_min_falling_path_sum():
    solution = Solution()

    # Test case 1
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.minFallingPathSum(grid))  # Expected output: 12

    # Test case 2
    grid = [[7]]
    print(solution.minFallingPathSum(grid))  # Expected output: 7

    # Test case 3
    grid = [[-10, -20, -30], [-5, -15, -25], [-1, -2, -3]]
    print(solution.minFallingPathSum(grid))  # Expected output: -60

    # Test case 4
    grid = [[1,2],[3,4]]
    print(solution.minFallingPathSum(grid))  # Expected output: 5

    # Test case 5
    grid = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
    print(solution.minFallingPathSum(grid))  # Expected output: -60

test_min_falling_path_sum()
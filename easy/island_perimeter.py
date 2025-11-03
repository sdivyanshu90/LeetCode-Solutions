from itertools import product
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 1:
                per += (i == 0 or grid[i-1][j] == 0)
                per += (j == 0 or grid[i][j-1] == 0)
        return per*2

def test_island_perimeter():
    s = Solution()

    # Test case 1
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    print(s.islandPerimeter(grid))  # Expected output: 16

    # Test case 2
    grid = [[1]]
    print(s.islandPerimeter(grid))  # Expected output: 4

    # Test case 3
    grid = [[1,0]]
    print(s.islandPerimeter(grid))  # Expected output: 4

    # Test case 4
    grid = [[1,1],
            [1,1]]
    print(s.islandPerimeter(grid))  # Expected output: 8

    # Test case 5
    grid = [[0,0,0],
            [0,1,0],
            [0,0,0]]
    print(s.islandPerimeter(grid))  # Expected output: 4

test_island_perimeter()
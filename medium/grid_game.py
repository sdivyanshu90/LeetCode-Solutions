from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = float("inf")
        for turn_index in range(len(grid[0])):
            first_row_sum -= grid[0][turn_index]
            minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][turn_index]
        return minimum_sum

def test_grid_game():
    solution = Solution()

    # Test case 1
    grid1 = [[2, 5, 4], [1, 5, 1]]
    print(solution.gridGame(grid1))  # Expected output: 4

    # Test case 2
    grid2 = [[3, 3, 1], [8, 5, 2]]
    print(solution.gridGame(grid2))  # Expected output: 4

    # Test case 3
    grid3 = [[1, 3, 1], [6, 5, 2]]
    print(solution.gridGame(grid3))  # Expected output: 4

    # Test case 4
    grid4 = [[7, 0, 9], [8, 5, 6]]
    print(solution.gridGame(grid4))  # Expected output: 9

    # Test case 5
    grid5 = [[1, 2, 3], [4, 5, 6]]
    print(solution.gridGame(grid5))  # Expected output: 4

test_grid_game()
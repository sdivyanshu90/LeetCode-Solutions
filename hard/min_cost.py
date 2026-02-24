class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        min_changes = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_changes[0][0] = 0

        while True:
            prev_state = [row[:] for row in min_changes]

            for row in range(num_rows):
                for col in range(num_cols):
                    if row > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row - 1][col]
                            + (0 if grid[row - 1][col] == 3 else 1),
                        )
                    if col > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col - 1]
                            + (0 if grid[row][col - 1] == 1 else 1),
                        )

            for row in range(num_rows - 1, -1, -1):
                for col in range(num_cols - 1, -1, -1):
                    if row < num_rows - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row + 1][col]
                            + (0 if grid[row + 1][col] == 4 else 1),
                        )
                    if col < num_cols - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col + 1]
                            + (0 if grid[row][col + 1] == 2 else 1),
                        )
            if min_changes == prev_state:
                break

        return min_changes[num_rows - 1][num_cols - 1]

def test_minCost():
    solution = Solution()

    # Test case 1
    grid1 = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
    print(solution.minCost(grid1)) # Expected output: 0

    # Test case 2
    grid2 = [[1, 2], [4, 3]]
    print(solution.minCost(grid2)) # Expected output: 1

    # Test case 3
    grid3 = [[2, 2, 2], [2, 2, 2]]
    print(solution.minCost(grid3)) # Expected output: 3

    # Test case 4
    grid4 = [[4]]
    print(solution.minCost(grid4)) # Expected output: 0

    # Test case 5
    grid5 = [[1, 1], [1, 1]]
    print(solution.minCost(grid5)) # Expected output: 2

test_minCost()
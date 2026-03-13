from typing import List

class Solution:
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ap_info = {"has_articulation_point": False, "time": 0}
        land_cells = 0
        island_count = 0

        discovery_time = [
            [-1] * cols for _ in range(rows)
        ]
        lowest_reachable = [
            [-1] * cols for _ in range(rows)
        ]
        parent_cell = [
            [-1] * cols for _ in range(rows)
        ]

        def _find_articulation_points(row, col):
            discovery_time[row][col] = ap_info["time"]
            ap_info["time"] += 1
            lowest_reachable[row][col] = discovery_time[row][col]
            children = 0

            for direction in self.DIRECTIONS:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == 1
                ):
                    if discovery_time[new_row][new_col] == -1:
                        children += 1
                        parent_cell[new_row][new_col] = (
                            row * cols + col
                        )
                        _find_articulation_points(new_row, new_col)

                        lowest_reachable[row][col] = min(
                            lowest_reachable[row][col],
                            lowest_reachable[new_row][new_col],
                        )

                        if (
                            lowest_reachable[new_row][new_col]
                            >= discovery_time[row][col]
                            and parent_cell[row][col] != -1
                        ):
                            ap_info["has_articulation_point"] = True
                    elif new_row * cols + new_col != parent_cell[row][col]:
                        lowest_reachable[row][col] = min(
                            lowest_reachable[row][col],
                            discovery_time[new_row][new_col],
                        )

            if parent_cell[row][col] == -1 and children > 1:
                ap_info["has_articulation_point"] = True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    if discovery_time[i][j] == -1:
                        _find_articulation_points(i, j)
                        island_count += 1

        if island_count == 0 or island_count >= 2:
            return 0
        if land_cells == 1:
            return 1
        if ap_info["has_articulation_point"]:
            return 1
        return 2

def test_min_days():
    solution = Solution()

    # Test case 1
    grid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    print(solution.minDays(grid))  # Expected output: 1

    # Test case 2
    grid = [[1, 1]]
    print(solution.minDays(grid))  # Expected output: 2

    # Test case 3
    grid = [[1, 0], [0, 1]]
    print(solution.minDays(grid))  # Expected output: 0

    # Test case 4
    grid = [[1]]
    print(solution.minDays(grid))  # Expected output: 1

    # Test case 5
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(solution.minDays(grid))  # Expected output: 2

test_min_days()
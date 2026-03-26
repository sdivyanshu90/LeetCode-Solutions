class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        rows = len(is_water)
        columns = len(is_water[0])
        INF = rows * columns

        cell_heights = [[INF] * columns for _ in range(rows)]

        for row in range(rows):
            for col in range(columns):
                if is_water[row][col] == 1:
                    cell_heights[row][col] = 0

        for row in range(rows):
            for col in range(columns):
                min_neighbor_distance = INF

                neighbor_row = row - 1
                neighbor_col = col
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                neighbor_row = row
                neighbor_col = col - 1
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                cell_heights[row][col] = min(
                    cell_heights[row][col], min_neighbor_distance + 1
                )

        for row in range(rows - 1, -1, -1):
            for col in range(columns - 1, -1, -1):
                min_neighbor_distance = INF

                neighbor_row = row + 1
                neighbor_col = col
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                neighbor_row = row
                neighbor_col = col + 1
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                cell_heights[row][col] = min(
                    cell_heights[row][col], min_neighbor_distance + 1
                )

        return cell_heights

    def is_valid_cell(
        self, row: int, col: int, rows: int, columns: int
    ) -> bool:
        return 0 <= row < rows and 0 <= col < columns

def test_highest_peak():
    solution = Solution()

    # Test Case 1
    is_water1 = [[0, 1], [0, 0]]
    print(solution.highestPeak(is_water1)) # Expected Output: [[1, 0], [2, 1]]

    # Test Case 2
    is_water2 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(solution.highestPeak(is_water2)) # Expected Output: [[2, 1, 2], [1, 0, 1], [2, 1, 2]]

    # Test Case 3
    is_water3 = [[1]]
    print(solution.highestPeak(is_water3)) # Expected Output: [[0]]

    # Test Case 4
    is_water4 = [[0]]
    print(solution.highestPeak(is_water4)) # Expected Output: [[2147483647]]

    # Test Case 5
    is_water5 = [[0, 0], [0, 0]]
    print(solution.highestPeak(is_water5)) # Expected Output: [[2147483647, 2147483647], [2147483647, 2147483647]]

test_highest_peak()
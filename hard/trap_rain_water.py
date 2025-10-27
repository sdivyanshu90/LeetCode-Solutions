import heapq

class Solution:
    class Cell:
        def __init__(self, height, row, col):
            self.height = height
            self.row = row
            self.col = col

        def __lt__(self, other):
            return self.height < other.height

    def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
        return 0 <= row < num_of_rows and 0 <= col < num_of_cols

    def trapRainWater(self, height_map):
        d_row = [0, 0, -1, 1]
        d_col = [-1, 1, 0, 0]

        num_of_rows = len(height_map)
        num_of_cols = len(height_map[0])

        visited = [[False] * num_of_cols for _ in range(num_of_rows)]

        boundary = []

        for i in range(num_of_rows):
            heapq.heappush(boundary, self.Cell(height_map[i][0], i, 0))
            heapq.heappush(
                boundary,
                self.Cell(height_map[i][num_of_cols - 1], i, num_of_cols - 1),
            )
            visited[i][0] = visited[i][num_of_cols - 1] = True

        for i in range(num_of_cols):
            heapq.heappush(boundary, self.Cell(height_map[0][i], 0, i))
            heapq.heappush(
                boundary,
                self.Cell(height_map[num_of_rows - 1][i], num_of_rows - 1, i),
            )
            visited[0][i] = visited[num_of_rows - 1][i] = True

        total_water_volume = 0

        while boundary:
            current_cell = heapq.heappop(boundary)

            current_row = current_cell.row
            current_col = current_cell.col
            min_boundary_height = current_cell.height

            for direction in range(4):
                neighbor_row = current_row + d_row[direction]
                neighbor_col = current_col + d_col[direction]

                if (
                    self._is_valid_cell(
                        neighbor_row, neighbor_col, num_of_rows, num_of_cols
                    )
                    and not visited[neighbor_row][neighbor_col]
                ):
                    neighbor_height = height_map[neighbor_row][neighbor_col]

                    if neighbor_height < min_boundary_height:
                        total_water_volume += (
                            min_boundary_height - neighbor_height
                        )

                    heapq.heappush(
                        boundary,
                        self.Cell(
                            max(neighbor_height, min_boundary_height),
                            neighbor_row,
                            neighbor_col,
                        ),
                    )
                    visited[neighbor_row][neighbor_col] = True

        return total_water_volume

def test_trap_rain_water():
    s = Solution()

    # Test case 1
    height_map1 = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1],
    ]
    print(s.trapRainWater(height_map1))  # Expected output: 4

    # Test case 2
    height_map2 = [
        [12, 13, 1, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13],
    ]
    print(s.trapRainWater(height_map2))  # Expected output: 14

    # Test case 3
    height_map3 = [
        [5,5,5,1],
        [5,1,5,5],
        [5,5,5,5]
    ]
    print(s.trapRainWater(height_map3))  # Expected output: 4

    # Test case 4
    height_map4 = [
        [3,3,3,3,3],
        [3,2,2,2,3],
        [3,2,1,2,3],
        [3,2,2,2,3],
        [3,3,3,3,3]
    ]
    print(s.trapRainWater(height_map4))  # Expected output: 10

    # Test case 5
    height_map5 = [
        [1,1,1,1],
        [1,0,0,1],
        [1,1,1,1]
    ]
    print(s.trapRainWater(height_map5))  # Expected output: 2

test_trap_rain_water()
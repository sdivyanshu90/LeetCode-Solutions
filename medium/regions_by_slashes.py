from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_size = len(grid)
        points_per_side = grid_size + 1
        total_points = points_per_side * points_per_side

        parent_array = [-1] * total_points
        for i in range(points_per_side):
            for j in range(points_per_side):
                if (
                    i == 0
                    or j == 0
                    or i == points_per_side - 1
                    or j == points_per_side - 1
                ):
                    point = i * points_per_side + j
                    parent_array[point] = 0

        parent_array[0] = -1
        region_count = 1
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == "/":
                    top_right = i * points_per_side + (j + 1)
                    bottom_left = (i + 1) * points_per_side + j
                    region_count += self._union(
                        parent_array, top_right, bottom_left
                    )
                elif grid[i][j] == "\\":
                    top_left = i * points_per_side + j
                    bottom_right = (i + 1) * points_per_side + (j + 1)
                    region_count += self._union(
                        parent_array, top_left, bottom_right
                    )

        return region_count

    def _find(self, parent_array: List[int], node: int) -> int:
        if parent_array[node] == -1:
            return node

        parent_array[node] = self._find(parent_array, parent_array[node])
        return parent_array[node]

    def _union(self, parent_array: List[int], node1: int, node2: int) -> int:
        parent1 = self._find(parent_array, node1)
        parent2 = self._find(parent_array, node2)

        if parent1 == parent2:
            return 1
            
        parent_array[parent2] = parent1
        return 0

def test_regions_by_slashes():
    solution = Solution()

    # Test case 1
    grid1 = [
        " /",
        "/ "
    ]
    print(solution.regionsBySlashes(grid1))  # Expected output: 2

    # Test case 2
    grid2 = [
        " /",
        "  "
    ]
    print(solution.regionsBySlashes(grid2))  # Expected output: 1

    # Test case 3
    grid3 = [
        "\\/",
        "/\\"
    ]
    print(solution.regionsBySlashes(grid3))  # Expected output: 4

    # Test case 4
    grid4 = [
        "/\\",
        "\\/"
    ]
    print(solution.regionsBySlashes(grid4))  # Expected output: 5

    # Test case 5
    grid5 = [
        "//",
        "/ "
    ]
    print(solution.regionsBySlashes(grid5))  # Expected output: 3

test_regions_by_slashes()
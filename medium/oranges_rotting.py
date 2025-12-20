from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        fresh = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0

        time = 0
        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                curr_x, curr_y = queue.popleft()
                for dx, dy in dirs:
                    x_new, y_new = curr_x + dx, curr_y + dy
                    if 0 <= x_new < m and 0 <= y_new < n and grid[x_new][y_new] == 1:
                        queue.append((x_new, y_new))
                        fresh -= 1
                        grid[x_new][y_new] = 2

            time += 1
        return time if fresh == 0 else -1


def test_oranges_rotting():
    solution = Solution()
    
    # Test case 1
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(solution.orangesRotting(grid))  # Expected output: 4

    # Test case 2
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(solution.orangesRotting(grid))  # Expected output: -1

    # Test case 3
    grid = [[0,2]]
    print(solution.orangesRotting(grid))  # Expected output: 0

    # Test case 4
    grid = [[2,2,0,1]]
    print(solution.orangesRotting(grid))  # Expected output: 1

    # Test case 5
    grid = [[1,1,1],[1,2,1],[1,1,1]]
    print(solution.orangesRotting(grid))  # Expected output: 2


test_oranges_rotting()
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, 0, 0)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        while heap:
            d, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                return d
            visited[x][y] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(
                        heap, (max(d, abs(heights[x][y] - heights[nx][ny])), nx, ny))
        return -1

def test_minimum_effort_path():
    solution = Solution()

    # Test case 1
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(solution.minimumEffortPath(heights))  # Expected output: 2

    # Test case 2
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(solution.minimumEffortPath(heights))  # Expected output: 1

    # Test case 3
    heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print(solution.minimumEffortPath(heights))  # Expected output: 0

    # Test case 4
    heights = [[1, 10, 6, 7, 9, 10, 4, 9]]
    print(solution.minimumEffortPath(heights))  # Expected output: 9

    # Test case 5
    heights = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.minimumEffortPath(heights))  # Expected output: 1

test_minimum_effort_path()
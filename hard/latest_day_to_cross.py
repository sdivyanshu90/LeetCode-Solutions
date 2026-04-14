class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day):
            water = set()
            for i in range(day):
                water.add(tuple(cells[i]))
            
            queue = deque()
            visited = set()
            
            for c in range(1, col + 1):
                if (1, c) not in water:
                    queue.append((1, c))
                    visited.add((1, c))
            
            while queue:
                r, c = queue.popleft()
                if r == row:
                    return True
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 1 <= nr <= row and 1 <= nc <= col and (nr, nc) not in water and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False

        left, right = 0, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

def test_latest_day_to_cross():
    solution = Solution()

    # Test case 1
    row1 = 2
    col1 = 2
    cells1 = [[1, 1], [2, 1], [1, 2], [2, 2]]
    print(solution.latestDayToCross(row1, col1, cells1))  # Expected output: 2

    # Test case 2
    row2 = 3
    col2 = 3
    cells2 = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [3, 2], [2, 3], [3, 1], [1, 3]]
    print(solution.latestDayToCross(row2, col2, cells2))  # Expected output: 3

    # Test case 3
    row3 = 1
    col3 = 1
    cells3 = [[1, 1]]
    print(solution.latestDayToCross(row3, col3, cells3))  # Expected output: 1

    # Test case 4
    row4 = 2
    col4 = 3
    cells4 = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3]]
    print(solution.latestDayToCross(row4, col4, cells4))  # Expected output: 3

    # Test case 5
    row5 = 3
    col5 = 2
    cells5 = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2]]
    print(solution.latestDayToCross(row5, col5, cells5))  # Expected output: 3

test_latest_day_to_cross()
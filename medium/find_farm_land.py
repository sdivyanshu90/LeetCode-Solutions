from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        ans = []
        for i in range(n):
            for j in range(m):
                if land[i][j]:
                    min_i, min_j = i, j
                    max_i, max_j = i, j
                    stack = [(i, j)]
                    land[i][j] = 0
                    while stack:
                        r, c = stack.pop()
                        for x, y in (r-1, c), (r, c-1), (r, c+1), (r+1, c):
                            if 0 <= x < n and 0 <= y < m and land[x][y]:
                                stack.append((x, y))
                                land[x][y] = 0
                                max_i = max(max_i, x)
                                max_j = max(max_j, y)
                    ans.append([min_i, min_j, max_i, max_j])
        return ans

def test_find_farm_land():
    solution = Solution()

    # Test case 1
    land1 = [[1, 0], [0, 1]]
    print(solution.findFarmland(land1))  # Expected output: [[0, 0, 0, 0], [1, 1, 1, 1]]

    # Test case 2
    land2 = [[1, 1], [1, 1]]
    print(solution.findFarmland(land2))  # Expected output: [[0, 0, 1, 1]]

    # Test case 3
    land3 = [[0]]
    print(solution.findFarmland(land3))  # Expected output: []

    # Test case 4
    land4 = [[1]]
    print(solution.findFarmland(land4))  # Expected output: [[0, 0, 0, 0]]

    # Test case 5
    land5 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    print(solution.findFarmland(land5))  
    # Expected output: [[0, 0, 0, 0], [0, 2, 0, 2], [1, 1, 1, 1], [2, 0, 2, 0], [2, 2, 2, 2]]

test_find_farm_land()
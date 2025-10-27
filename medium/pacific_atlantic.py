from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (
                r < 0 or c < 0 or r >= m or c >= n
                or (r, c) in visited
                or heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(m):
            dfs(r, 0, pacific, -1)
        for c in range(n):
            dfs(0, c, pacific, -1)

        for r in range(m):
            dfs(r, n - 1, atlantic, -1)
        for c in range(n):
            dfs(m - 1, c, atlantic, -1)

        return list(map(list, pacific & atlantic))

def test_pacific_atlantic():
    s = Solution()

    # Test case 1
    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # Expected: [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]]

    # Test Case 2
    print(s.pacificAtlantic([])) # Expected: []
    
    # Test Case 3
    print(s.pacificAtlantic([[2,1],[1,2]])) # Expected: [[0,0],[0,1],[1,0],[1,1]]

    # Test Case 4
    print(s.pacificAtlantic([[10]])) # Expected: [[0,0]]

    # Test Case 5
    print(s.pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]])) # Expected: [[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],[0,0]]

    # Test Case 6
    print(s.pacificAtlantic([[3,3,3,3,3],[3,1,1,1,3],[3,1,3,1,3],[3,1,1,1,3],[3,3,3,3,3]])) # Expected: [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,4],[2,0],[2,2],[2,4],[3,0],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]]

    # Test Case 7
    print(s.pacificAtlantic([[1,1],[1,1]])) # Expected: [[0,0],[0,1],[1,0],[1,1]]

    # Test Case 8
    print(s.pacificAtlantic([[5,5,5],[5,1,5],[5,5,5]])) # Expected: [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]

    # Test Case 9
    print(s.pacificAtlantic([[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]])) # Expected: [[0,4],[1,4],[2,4],[3,4],[4,4],[4,3],[4,2],[4,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

    # Test Case 10
    print(s.pacificAtlantic([[1]])) # Expected: [[0,0]]

test_pacific_atlantic()
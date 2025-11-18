from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat


def test_update_matrix():
    s = Solution()

    # Test case 1
    mat1 = [[0,0,0],[0,1,0],[0,0,0]]
    print(s.updateMatrix(mat1)) # Expected output: [[0,0,0],[0,1,0],[0,0,0]]

    # Test case 2
    mat2 = [[0,0,0],[0,1,0],[1,1,1]]
    print(s.updateMatrix(mat2)) # Expected output: [[0,0,0],[0,1,0],[1,2,1]]

    # Test case 3
    mat3 = [[1,1,1],[1,0,1],[1,1,1]]
    print(s.updateMatrix(mat3)) # Expected output: [[2,1,2],[1,0,1],[2,1,2]]

    # Test case 4
    mat4 = [[0]]
    print(s.updateMatrix(mat4)) # Expected output: [[0]]

    # Test case 5
    mat5 = [[1]]
    print(s.updateMatrix(mat5)) # Expected output: [[inf]]

test_update_matrix()
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        heights = [[0]*n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 1:
                    heights[i][j] = 1 + (heights[i-1][j] if i > 0 else 0)
        
        count = 0
        for i in range(m):
            for j in range(n):
                min_h = float('inf')
                for k in range(j, -1, -1):
                    if heights[i][k] == 0: break
                    min_h = min(min_h, heights[i][k])
                    count += min_h
        return count

def test_num_submat():
    solution = Solution()

    # Test Case 1
    mat1 = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
    print(solution.numSubmat(mat1))  # Expected output: 13

    # Test Case 2
    mat2 = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
    print(solution.numSubmat(mat2))  # Expected output: 24

    # Test Case 3
    mat3 = [[1]]
    print(solution.numSubmat(mat3))  # Expected output: 1

    # Test Case 4
    mat4 = [[0]]
    print(solution.numSubmat(mat4))  # Expected output: 0

    # Test Case 5
    mat5 = [[1] * (10 ** 1) for _ in range(10 ** 5)]
    print(solution.numSubmat(mat5))  # Expected output: 275002750000

test_num_submat()
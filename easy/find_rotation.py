from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(matrix: List[List[int]]) -> List[List[int]]:
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for i in range(n):
                matrix[i].reverse()

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)

        return False

def test_find_rotation():
    solution = Solution()

    # Test case 1
    mat1 = [[0, 1], [1, 0]]
    target1 = [[1, 0], [0, 1]]
    print(solution.findRotation(mat1, target1))  # Expected output: True

    # Test case 2
    mat2 = [[0, 1], [1, 1]]
    target2 = [[1, 0], [0, 1]]
    print(solution.findRotation(mat2, target2))  # Expected output: False

    # Test case 3
    mat3 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    target3 = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    print(solution.findRotation(mat3, target3))  # Expected output: True

    # Test case 4
    mat4 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    target4 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(solution.findRotation(mat4, target4))  # Expected output: True

    # Test case 5
    mat5 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    target5 = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    print(solution.findRotation(mat5, target5))  # Expected output: True

test_find_rotation()
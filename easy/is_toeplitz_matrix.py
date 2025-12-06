from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True

def test_is_toeplitz_matrix():
    solution = Solution()
    
    # Test case 1
    matrix1 = [
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]
    ]
    print(solution.isToeplitzMatrix(matrix1)) # Expected: True
    
    # Test case 2
    matrix2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    print(solution.isToeplitzMatrix(matrix2)) # Expected: False
    
    # Test case 3
    matrix3 = [
        [1]
    ]
    print(solution.isToeplitzMatrix(matrix3)) # Expected: True
    
    # Test case 4
    matrix4 = [
        [1,2],
        [2,1]
    ]
    print(solution.isToeplitzMatrix(matrix4)) # Expected: False

    # Test case 5
    matrix5 = [
        [7,8,9],
        [6,7,8],
        [5,6,7]
    ]
    print(solution.isToeplitzMatrix(matrix5)) # Expected: True

    # Test case 6
    matrix6 = [
        [1,2,3],
        [4,1,2],
        [5,4,1]
    ]
    print(solution.isToeplitzMatrix(matrix6)) # Expected: True

    # Test case 7
    matrix7 = [
        [1,2,3,4,5],
        [6,1,2,3,4],
        [7,6,1,2,3],
        [8,7,6,1,2]
    ]
    print(solution.isToeplitzMatrix(matrix7)) # Expected: True

    # Test case 8
    matrix8 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(solution.isToeplitzMatrix(matrix8)) # Expected: False

    # Test case 9
    matrix9 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    print(solution.isToeplitzMatrix(matrix9)) # Expected: True

    # Test case 10
    matrix10 = [
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2],
        [0,9,5,1]
    ]
    print(solution.isToeplitzMatrix(matrix10)) # Expected: True

test_is_toeplitz_matrix()
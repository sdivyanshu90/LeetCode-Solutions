from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j  in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()

def test_rotate():
    solution = Solution()
    
    # Test case 1: Regular case with a 3x3 matrix
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix1)
    print(matrix1)  # Expected output: [[7,4,1],[8,5,2],[9,6,3]]
    
    # Test case 2: Diagonal matrix
    matrix2 = [[1,0,0],[0,2,0],[0,0,3]]
    solution.rotate(matrix2)
    print(matrix2)  # Expected output: [[0,0,1],[0,2,0],[3,0,0]]

    # Test case 3: Rectangular matrix (more columns than rows)
    matrix3 = [[1,2,3],[4,5,6]]
    solution.rotate(matrix3)
    print(matrix3)  # Expected output: [[4,1],[5,2],[6,3]]

    # Test case 4: Single row matrix
    matrix4 = [[1,2,3,4]]
    solution.rotate(matrix4)
    print(matrix4)  # Expected output: [[1],[2],[3],[4]]

    # Test case 5: Matrix with negative numbers
    matrix5 = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
    solution.rotate(matrix5)
    print(matrix5)  # Expected output: [[-7,-4,-1],[-8,-5,-2],[-9,-6,-3]]

    # Test case 6: Matrix
    matrix6 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix6)
    print(matrix6)  # Expected output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    # Test case 7: Matrix with one element
    matrix7 = [[42]]
    solution.rotate(matrix7)
    print(matrix7)  # Expected output: [[42]]

    # Test case 8: Larger matrix
    matrix8 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    solution.rotate(matrix8)
    print(matrix8)  # Expected output: [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]

    # Test case 9: Empty matrix
    matrix9 = []
    solution.rotate(matrix9)
    print(matrix9)  # Expected output: []

    # Test case 10: Non-square matrix (should handle gracefully)
    matrix10 = [[1,2,3],[4,5,6]]
    solution.rotate(matrix10)
    print(matrix10)  # Expected output: [[4,1],[5,2],[6,3]]

test_rotate()
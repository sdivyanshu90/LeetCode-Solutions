from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        n, m =  len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in row:
            for j in range(m):
                matrix[i][j] = 0

        for j in col:
            for i in range(n):
                matrix[i][j] = 0

def test_set_zeroes():
    solution = Solution()

    # Test case 1
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    solution.setZeroes(matrix1)
    print(matrix1)


    # Test case 2
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix2)
    print(matrix2)

    # Test case 3
    matrix3 = [[1]]
    solution.setZeroes(matrix3)
    print(matrix3)

    # Test case 4
    matrix4 = [[0]]
    solution.setZeroes(matrix4)
    print(matrix4)

    # Test case 5
    matrix5 = [[1,2,3],[4,0,6],[7,8,9]]
    solution.setZeroes(matrix5)
    print(matrix5)
    
test_set_zeroes()
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        r = len(matrix)
        c = len(matrix[0])

        rowEnd = r - 1
        rowStart = 0
        colStart = 0
        colEnd = c - 1

        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd + 1):
                result.append(matrix[rowStart][i])
                
            rowStart += 1
            for i in range(rowStart, rowEnd + 1):
                result.append(matrix[i][colEnd])
                
            colEnd -= 1
            if rowStart <= rowEnd:
                for i in range(colEnd, colStart - 1, -1):
                    result.append(matrix[rowEnd][i])
                rowEnd -= 1
                
            if colStart <= colEnd:
                for i in range(rowEnd, rowStart - 1, -1):
                    result.append(matrix[i][colStart])
                colStart += 1
        return result

def test_spiral_order():
    solution = Solution()
    
    # Test case 1: Regular case with a 3x3 matrix
    print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Expected output: [1,2,3,6,9,8,7,4,5]
    
    # Test case 2: Rectangular matrix (more rows than columns)
    print(solution.spiralOrder([[1,2],[3,4],[5,6]]))  # Expected output: [1,2,4,6,5,3]

    # Test case 3: Rectangular matrix (more columns than rows)
    print(solution.spiralOrder([[1,2,3],[4,5,6]]))  # Expected output: [1,2,3,6,5,4]

    # Test case 4: Single row matrix
    print(solution.spiralOrder([[1,2,3,4]]))  # Expected output: [1,2,3,4]

    # Test case 5: Single column matrix
    print(solution.spiralOrder([[1],[2],[3],[4]]))  # Expected output: [1,2,3,4]

    # Test case 6: Diagonal matrix
    print(solution.spiralOrder([[1,0,0],[0,2,0],[0,0,3]]))  # Expected output: [1,0,0,0,3,0,0,2]

    # Test case 7: Matrix with one element
    print(solution.spiralOrder([[42]]))  # Expected output: [42]

    # Test case 8: Larger matrix
    print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))  # Expected output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

    # Test case 9: Matrix with negative numbers
    print(solution.spiralOrder([[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]))  # Expected output: [-1,-2,-3,-6,-9,-8,-7,-4,-5]

    # Test case 10: Non-square matrix with odd dimensions
    print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))  # Expected output: [1,2,3,6,9,12,11,10,7,4,5,8]

test_spiral_order()
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (right + left) // 2
            num = matrix[mid // cols][mid % cols]
            
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

def test_search_matrix():
    solution = Solution()

    # Test case 1
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    print(solution.searchMatrix(matrix1, target1))  # Expected output: True

    # Test case 2
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    print(solution.searchMatrix(matrix2, target2))  # Expected output: False

    # Test case 3
    matrix3 = []
    target3 = 0
    print(solution.searchMatrix(matrix3, target3))  # Expected output: False

    # Test case 4
    matrix4 = [[1]]
    target4 = 1
    print(solution.searchMatrix(matrix4, target4))  # Expected output: True

    # Test case 5
    matrix5 = [[1]]
    target5 = 0
    print(solution.searchMatrix(matrix5, target5))  # Expected output: False

    # Test case 6
    matrix6 = [[1,3]]
    target6 = 3
    print(solution.searchMatrix(matrix6, target6))  # Expected output: True

    # Test case 7
    matrix7 = [[1],[3]]
    target7 = 2
    print(solution.searchMatrix(matrix7, target7))  # Expected output: False

    # Test case 8
    matrix8 = [[1,2],[3,4]]
    target8 = 4
    print(solution.searchMatrix(matrix8, target8))  # Expected output: True

    # Test case 9
    matrix9 = [[1,2,3],[4,5,6],[7,8,9]]
    target9 = 5
    print(solution.searchMatrix(matrix9, target9))  # Expected output: True

    # Test case 10
    matrix10 = [[1,2,3],[4,5,6],[7,8,9]]
    target10 = 10
    print(solution.searchMatrix(matrix10, target10))  # Expected output: False

test_search_matrix()
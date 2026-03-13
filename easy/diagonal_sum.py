class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0

        for i in range(n):
            res += mat[i][i]
            if i != n - i - 1:
                res += mat[i][n - i - 1]
        return res

def test_diagonal_sum():
    solution = Solution()

    # Test case 1
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.diagonalSum(mat))  # Expected output: 25

    # Test case 2
    mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    print(solution.diagonalSum(mat))  # Expected output: 8

    # Test case 3
    mat = [[5]]
    print(solution.diagonalSum(mat))  # Expected output: 5

    # Test case 4
    mat = [[1, 2], [3, 4]]
    print(solution.diagonalSum(mat))  # Expected output: 10

    # Test case 5
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(solution.diagonalSum(mat))  # Expected output: 68

test_diagonal_sum()
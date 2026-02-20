from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = (
                        min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    )
                    ans += dp[i + 1][j + 1]
        return ans

def test_count_squares():
    solution = Solution()

    # Test case 1
    matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
    print(solution.countSquares(matrix))  # Expected output: 15

    # Test case 2
    matrix = [[1,0,1],[0,1,0],[1,0,1]]
    print(solution.countSquares(matrix))  # Expected output: 5

    # Test case 3
    matrix = [[0]]
    print(solution.countSquares(matrix))  # Expected output: 0

    # Test case 4
    matrix = [[1]]
    print(solution.countSquares(matrix))  # Expected output: 1

    # Test case 5
    matrix = [[1,1],[1,1]]
    print(solution.countSquares(matrix))  # Expected output: 5

test_count_squares()
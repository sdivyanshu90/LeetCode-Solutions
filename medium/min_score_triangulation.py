from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], values[i] * values[j] * values[k] + dp[i][k] + dp[k][j])

        return dp[0][n-1]

def test_min_score_triangulation():
    solution = Solution()

    # Test case 1
    values = [1, 2, 3]
    print(solution.minScoreTriangulation(values))  # Expected output: 6

    # Test case 2
    values = [3, 7, 4, 5]
    print(solution.minScoreTriangulation(values))  # Expected output: 144

    # Test case 3
    values = [1, 3, 1, 4, 1, 5]
    print(solution.minScoreTriangulation(values))  # Expected output: 13

    # Test case 4
    values = [2, 1, 3]
    print(solution.minScoreTriangulation(values))  # Expected output: 6

    # Test case 5
    values = [1, 2, 3, 4, 5]
    print(solution.minScoreTriangulation(values))  # Expected output: 38

test_min_score_triangulation()
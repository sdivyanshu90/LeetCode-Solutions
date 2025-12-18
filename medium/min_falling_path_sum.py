from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        if m == 1 or n == 1:
            return A[0][0]

        dp = [[float('inf')] * n for _ in range(m)]
        ans = float('inf')

        for i in range(len(A)):
            ans = min(ans, self.minFallingPathSumHelper(A, 0, i, dp))
        return ans

    def minFallingPathSumHelper(self, A, row, col, dp):
        m, n = len(A), len(A[0])

        if dp[row][col] != float('inf'):
            return dp[row][col]

        if row == m - 1:
            return A[row][col]

        left = right = float('inf')

        if col > 0:
            left = self.minFallingPathSumHelper(A, row + 1, col - 1, dp)

        straight = self.minFallingPathSumHelper(A, row + 1, col, dp)

        if col < n - 1:
            right = self.minFallingPathSumHelper(A, row + 1, col + 1, dp)

        dp[row][col] = min(left, min(straight, right)) + A[row][col]

        return dp[row][col]

def test_min_falling_path_sum():
    solution = Solution()

    # Test case 1
    A1 = [[2,1,3],[6,5,4],[7,8,9]]
    print(solution.minFallingPathSum(A1))  # Expected output: 13

    # Test case 2
    A2 = [[-19,57],[-40,-5]]
    print(solution.minFallingPathSum(A2))  # Expected output: -59

    # Test case 3
    A3 = [[-48]]
    print(solution.minFallingPathSum(A3))  # Expected output: -48

    # Test case 4
    A4 = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[-51,81,69,-51]]
    print(solution.minFallingPathSum(A4))  # Expected output: -138

    # Test case 5
    A5 = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.minFallingPathSum(A5))  # Expected output: 12

test_min_falling_path_sum()
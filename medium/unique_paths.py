class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

def test_unique_paths():
    solution = Solution()
    # Test Case 1
    print(solution.uniquePaths(3, 7))    # Expected output: 28
    # Test Case 2
    print(solution.uniquePaths(3, 2))    # Expected output: 3
    # Test Case 3
    print(solution.uniquePaths(7, 3))    # Expected output: 28
    # Test Case 4
    print(solution.uniquePaths(3, 3))    # Expected output: 6
    # Test Case 5
    print(solution.uniquePaths(1, 1))    # Expected output: 1
    # Test Case 6
    print(solution.uniquePaths(10, 10))  # Expected output: 48620
    # Test Case 7
    print(solution.uniquePaths(5, 5))    # Expected output: 70
    # Test Case 8
    print(solution.uniquePaths(2, 2))    # Expected output: 2
    # Test Case 9
    print(solution.uniquePaths(4, 4))    # Expected output: 20
    # Test Case 10
    print(solution.uniquePaths(6, 6))    # Expected output: 462

test_unique_paths()
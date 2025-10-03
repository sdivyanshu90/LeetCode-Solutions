from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j-1]
        
        return dp[n-1]

def test_unique_paths_with_obstacles():
    solution = Solution()
    # Test Case 1
    print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # Expected output: 2
    # Test Case 2
    print(solution.uniquePathsWithObstacles([[0,1],[0,0]]))              # Expected output: 1
    # Test Case 3
    print(solution.uniquePathsWithObstacles([[1]]))                      # Expected output: 0
    # Test Case 4
    print(solution.uniquePathsWithObstacles([[0]]))                      # Expected output: 1
    # Test Case 5
    print(solution.uniquePathsWithObstacles([[0,0],[1,0]]))              # Expected output: 1
    # Test Case 6
    print(solution.uniquePathsWithObstacles([[0,0],[0,1]]))              # Expected output: 0
    # Test Case 7
    print(solution.uniquePathsWithObstacles([[0,0,0],[1,1,0],[0,0,0]]))  # Expected output: 2
    # Test Case 8
    print(solution.uniquePathsWithObstacles([[0,1,0],[0,1,0],[0,0,0]]))  # Expected output: 1
    # Test Case 9
    print(solution.uniquePathsWithObstacles([[0,0],[0,0]]))              # Expected output: 2
    # Test Case 10
    print(solution.uniquePathsWithObstacles([[0,0,1],[0,0,0],[1,0,0]]))  # Expected output: 2

test_unique_paths_with_obstacles()
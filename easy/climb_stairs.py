class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]

        for i in range(2, n+2):
            dp.append(dp[i-2] + dp[i-1])
        
        return dp[n+1]

def test_climb_stairs():
    solution = Solution()
    # Test Case 1
    print(solution.climbStairs(2))  # Expected output: 2
    # Test Case 2
    print(solution.climbStairs(3))  # Expected output: 3
    # Test Case 3
    print(solution.climbStairs(4))  # Expected output: 5
    # Test Case 4
    print(solution.climbStairs(5))  # Expected output: 8
    # Test Case 5
    print(solution.climbStairs(6))  # Expected output: 13
    # Test Case 6
    print(solution.climbStairs(7))  # Expected output: 21
    # Test Case 7
    print(solution.climbStairs(8))  # Expected output: 34
    # Test Case 8
    print(solution.climbStairs(9))  # Expected output: 55
    # Test Case 9
    print(solution.climbStairs(10)) # Expected output: 89
    # Test Case 10
    print(solution.climbStairs(20)) # Expected output: 10946

test_climb_stairs()
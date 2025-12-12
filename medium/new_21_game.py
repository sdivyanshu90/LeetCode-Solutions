class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        result = 0.0
        
        for x in range(1, n + 1):
            dp[x] = window_sum / maxPts
            if x < k:
                window_sum += dp[x]
            else:
                result += dp[x]
            
            if x - maxPts >= 0:
                window_sum -= dp[x - maxPts]
        
        return result

def test_new21Game():
    solution = Solution()
    
    # Test Case 1
    print(abs(solution.new21Game(10, 1, 10) - 1.0)) # Expected: 1.1102230246251565e-16

    # Test Case 2
    print(abs(solution.new21Game(6, 1, 10) - 0.6)) # Expected: 0.0

    # Test Case 3
    print(abs(solution.new21Game(5, 0, 2) - 1.0)) # Expected: 0.0

    # Test Case 4
    print(abs(solution.new21Game(21, 17, 10) - 0.73278)) # Expected: 2.212931391798456e-06

    # Test Case 5
    print(abs(solution.new21Game(0, 0, 1) - 1.0)) # Expected: 0.0
    
test_new21Game()
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        arrLen = min(arrLen, steps)
        dp = [[0] * (steps + 1) for _ in range(arrLen)]
        dp[0][0] = 1
        
        for remain in range(1, steps + 1):
            for curr in range(arrLen - 1, -1, -1):
                ans = dp[curr][remain - 1]
                
                if curr > 0:
                    ans = (ans + dp[curr - 1][remain - 1]) % MOD
                
                if curr < arrLen - 1:
                    ans = (ans + dp[curr + 1][remain - 1]) % MOD
                
                dp[curr][remain] = ans
        
        return dp[0][steps]

def test_num_ways():
    solution = Solution()

    # Test case 1
    steps = 3
    arrLen = 2
    print(solution.numWays(steps, arrLen))  # Expected output: 4

    # Test case 2
    steps = 2
    arrLen = 4
    print(solution.numWays(steps, arrLen))  # Expected output: 2

    # Test case 3
    steps = 4
    arrLen = 2
    print(solution.numWays(steps, arrLen))  # Expected output: 8

    # Test case 4
    steps = 27
    arrLen = 7
    print(solution.numWays(steps, arrLen))  # Expected output: 127784505

    # Test case 5
    steps = 7
    arrLen = 3
    print(solution.numWays(steps, arrLen))  # Expected output: 28

test_num_ways()
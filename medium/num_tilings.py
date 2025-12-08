class Solution:
    def numTilings(self, n: int) -> int:
        mod = int(1e9 + 7)
        dp = [1,0,0,0]
        for i in range(n):
            dp = [(dp[0] + dp[3]) % mod,
                (dp[0] + dp[2]) % mod,
                (dp[0] + dp[1]) % mod,
                (dp[0] + dp[1] + dp[2]) % mod]
        return dp[0]

def test_num_tilings():
    solution = Solution()
    
    # Test case 1
    n = 1
    print(solution.numTilings(n)) # Expected: 1
    
    # Test case 2
    n = 2
    print(solution.numTilings(n)) # Expected: 2
    
    # Test case 3
    n = 3
    print(solution.numTilings(n)) # Expected: 5
    
    # Test case 4
    n = 4
    print(solution.numTilings(n)) # Expected: 11

    # Test case 5
    n = 5
    print(solution.numTilings(n)) # Expected: 24

    # Test case 6
    n = 6
    print(solution.numTilings(n)) # Expected: 53

    # Test case 7
    n = 7
    print(solution.numTilings(n)) # Expected: 117

    # Test case 8
    n = 8
    print(solution.numTilings(n)) # Expected: 258

    # Test case 9
    n = 9
    print(solution.numTilings(n)) # Expected: 569

    # Test case 10
    n = 10
    print(solution.numTilings(n)) # Expected: 1255

test_num_tilings()
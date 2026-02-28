class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]
        prefix = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]
        MOD = 10 ** 9 + 7
        
        for num in range(1, m + 1):
            dp[1][num][1] = 1
            prefix[1][num][1] = prefix[1][num - 1][1] + 1

        for i in range(1, n + 1):
            for max_num in range(1, m + 1):
                for cost in range(1, k + 1):                    
                    ans = (max_num * dp[i - 1][max_num][cost]) % MOD
                    ans = (ans + prefix[i - 1][max_num - 1][cost - 1]) % MOD

                    dp[i][max_num][cost] += ans
                    dp[i][max_num][cost] %= MOD
                    
                    prefix[i][max_num][cost] = (prefix[i][max_num - 1][cost] + dp[i][max_num][cost]) % MOD

        return prefix[n][m][k]

def test_num_of_arrays():
    solution = Solution()

    # Test case 1
    n1, m1, k1 = 2, 3, 1
    print(solution.numOfArrays(n1, m1, k1))  # Expected output: 6

    # Test case 2
    n2, m2, k2 = 5, 2, 3
    print(solution.numOfArrays(n2, m2, k2))  # Expected output: 0

    # Test case 3
    n3, m3, k3 = 9, 1, 1
    print(solution.numOfArrays(n3, m3, k3))  # Expected output: 1

    # Test case 4
    n4, m4, k4 = 50, 1000000000, 25
    print(solution.numOfArrays(n4, m4, k4))  # Expected output: 34549172

    # Test case 5
    n5, m5, k5 = 37, 17, 7
    print(solution.numOfArrays(n5, m5, k5))  # Expected output: 418930126

test_num_of_arrays()
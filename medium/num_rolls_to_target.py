class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, n + 1):
            for j in range(1, min(i * k, target) + 1):
                for h in range(1, min(j, k) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - h]) % mod
        return dp[n][target]

def test_num_rolls_to_target():
    solution = Solution()

    # Test case 1
    n = 2
    k = 6
    target = 7
    print(solution.numRollsToTarget(n, k, target))  # Expected output: 6

    # Test case 2
    n = 1
    k = 6
    target = 3
    print(solution.numRollsToTarget(n, k, target))  # Expected output: 1

    # Test case 3
    n = 30
    k = 30
    target = 500
    print(solution.numRollsToTarget(n, k, target))  # Expected output: 222616187

    # Test case 4
    n = 3
    k = 4
    target = 5
    print(solution.numRollsToTarget(n, k, target))  # Expected output: 6

    # Test case 5
    n = 2
    k = 5
    target = 10
    print(solution.numRollsToTarget(n, k, target))  # Expected output: 1

test_num_rolls_to_target()
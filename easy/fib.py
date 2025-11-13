class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]

def test_fib():
    solution = Solution()

    print(solution.fib(2))  # Expected: 1
    print(solution.fib(3))  # Expected: 2
    print(solution.fib(4))  # Expected: 3
    print(solution.fib(5))  # Expected: 5
    print(solution.fib(10)) # Expected: 55

test_fib()
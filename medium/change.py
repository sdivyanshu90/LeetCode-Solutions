class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]


def test_change():
    solution = Solution()

    # Test Case 1
    amount1 = 5
    coins1 = [1, 2, 5]
    print(solution.change(amount1, coins1))  # Expected: 4

    # Test Case 2
    amount2 = 3
    coins2 = [2]
    print(solution.change(amount2, coins2))  # Expected: 0

    # Test Case 3
    amount3 = 10
    coins3 = [10]
    print(solution.change(amount3, coins3))  # Expected: 1

    # Test Case 4
    amount4 = 0
    coins4 = [1, 2, 3]
    print(solution.change(amount4, coins4))  # Expected: 1

    # Test Case 5
    amount5 = 7
    coins5 = [1, 3, 4, 5]
    print(solution.change(amount5, coins5))  # Expected: 6

test_change()
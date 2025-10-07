from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit

def test_max_profit():
    solution = Solution()

    # Test case 1: Example case
    prices1 = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices1))  # Expected output: 5

    # Test case 2: No profit case
    prices2 = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices2))  # Expected output: 0

    # Test case 3: Single day prices
    prices3 = [5]
    print(solution.maxProfit(prices3))  # Expected output: 0

    # Test case 4: Increasing prices
    prices4 = [1, 2, 3, 4, 5]
    print(solution.maxProfit(prices4))  # Expected output: 4

    # Test case 5: Decreasing then increasing
    prices5 = [9, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices5))  # Expected output: 5

test_max_profit()
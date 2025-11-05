import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = []
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)
        for i in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -1 * p)
            if not max_profit:
                break
            w += -1 * heapq.heappop(max_profit)
        return w

def test_find_maximized_capital():
    solution = Solution()

    # Test case 1
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print(solution.findMaximizedCapital(k, w, profits, capital))  # Expected output: 4

    # Test case 2
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    print(solution.findMaximizedCapital(k, w, profits, capital))  # Expected output: 6

    # Test case 3
    k = 1
    w = 2
    profits = [3, 5, 1]
    capital = [0, 1, 2]
    print(solution.findMaximizedCapital(k, w, profits, capital))  # Expected output: 5

    # Test case 4
    k = 4
    w = 0
    profits = [1, 2, 3, 5]
    capital = [0, 1, 1, 2]
    print(solution.findMaximizedCapital(k, w, profits, capital))  # Expected output: 11

    # Test case 5
    k = 0
    w = 10
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    print(solution.findMaximizedCapital(k, w, profits, capital))  # Expected output: 10

test_find_maximized_capital()
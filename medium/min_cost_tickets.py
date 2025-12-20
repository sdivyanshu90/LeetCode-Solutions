from functools import cache
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        tickets: List[int] = [1, 7, 30]

        @cache
        def next_idx(curr: int, tick: int = 0) -> int:
            for i in range(curr, -1, -1):
                if days[i] <= days[curr] - tick:
                    return i
            return -1

        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0
            elif i == 0:
                return min(costs)
            return min(c + dp(next_idx(i, tickets[j])) for j, c in enumerate(costs))

        return dp(len(days) - 1)

def test_min_cost_tickets():
    solution = Solution()
    
    # Test case 1
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(solution.mincostTickets(days, costs))  # Expected output: 11

    # Test case 2
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    print(solution.mincostTickets(days, costs))  # Expected output: 17

    # Test case 3
    days = [1,3,5,7,12,20]
    costs = [3,8,20]
    print(solution.mincostTickets(days, costs))  # Expected output: 14

    # Test case 4
    days = [1,2,4,5,6,8,9,10]
    costs = [2,10,25]
    print(solution.mincostTickets(days, costs))  # Expected output: 14

    # Test case 5
    days = [2,3,5,7,11,13,17,19]
    costs = [4,12,30]
    print(solution.mincostTickets(days, costs))  # Expected output: 16

test_min_cost_tickets()
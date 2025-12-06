from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = cost[0]
        dp2 = cost[1]

        for i in range(2, len(cost)):
            dp0 = cost[i] + min(dp1, dp2)
            dp1 = dp2
            dp2 = dp0
        return min(dp2, dp1)

def test_min_cost_climbing_stairs():
    solution = Solution()
    
    # Test case 1
    cost1 = [10, 15, 20]
    print(solution.minCostClimbingStairs(cost1)) # Expected: 15
    
    # Test case 2
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(solution.minCostClimbingStairs(cost2)) # Expected: 6
    
    # Test case 3
    cost3 = [0, 0, 0, 0]
    print(solution.minCostClimbingStairs(cost3)) # Expected: 0
    
    # Test case 4
    cost4 = [5, 10, 15]
    print(solution.minCostClimbingStairs(cost4)) # Expected: 10
    
    # Test case 5
    cost5 = [1, 2]
    print(solution.minCostClimbingStairs(cost5)) # Expected: 1

    # Test case 6
    cost6 = [10, 5, 15, 20, 10]
    print(solution.minCostClimbingStairs(cost6)) # Expected: 25

    # Test case 7
    cost7 = [3, 2, 4, 1, 5]
    print(solution.minCostClimbingStairs(cost7)) # Expected: 6

    # Test case 8
    cost8 = [100, 1, 1, 100, 1, 1, 100]
    print(solution.minCostClimbingStairs(cost8)) # Expected: 4

    # Test case 9
    cost9 = [1, 2, 3, 4, 5]
    print(solution.minCostClimbingStairs(cost9)) # Expected: 6

    # Test case 10
    cost10 = [20, 15, 10, 5]
    print(solution.minCostClimbingStairs(cost10)) # Expected: 15

test_min_cost_climbing_stairs()
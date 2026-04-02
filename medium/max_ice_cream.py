from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        res = 0
        for i in range(len(costs)):
            coins -= costs[i]
            if coins >= 0:
                res += 1
        return res

def test_max_ice_cream():
    solution = Solution()

    # Test Case 1
    costs1 = [1,3,2,4,1]
    coins1 = 7
    print(solution.maxIceCream(costs1, coins1))  # Expected Output: 4

    # Test Case 2
    costs2 = [10,6,8,7,7,8]
    coins2 = 5
    print(solution.maxIceCream(costs2, coins2))  # Expected Output: 0

    # Test Case 3
    costs3 = [1,6,3,1,2,5]
    coins3 = 20
    print(solution.maxIceCream(costs3, coins3))  # Expected Output: 6

    # Test Case 4
    costs4 = [9,8,7,6,5]
    coins4 = 15
    print(solution.maxIceCream(costs4, coins4))  # Expected Output: 2

    # Test Case 5
    costs5 = [1]
    coins5 = 10
    print(solution.maxIceCream(costs5, coins5))  # Expected Output: 1

test_max_ice_cream()
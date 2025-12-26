from typing import List

class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        unrealized_customers = 0
        for i in range(minutes):
            unrealized_customers += customers[i] * grumpy[i]

        max_unrealized_customers = unrealized_customers

        for i in range(minutes, n):
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]

            max_unrealized_customers = max(
                max_unrealized_customers, unrealized_customers
            )

        total_customers = max_unrealized_customers
        for i in range(n):
            total_customers += customers[i] * (1 - grumpy[i])
        return total_customers

def test_max_satisfied():
    solution = Solution()

    # Test case 1
    customers1 = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy1 = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes1 = 3
    print(solution.maxSatisfied(customers1, grumpy1, minutes1))  # Expected output: 16

    # Test case 2
    customers2 = [4, 10, 10]
    grumpy2 = [1, 1, 0]
    minutes2 = 2
    print(solution.maxSatisfied(customers2, grumpy2, minutes2))  # Expected output: 24

    # Test case 3
    customers3 = [2, 6, 9, 1, 7]
    grumpy3 = [0, 0, 1, 0, 1]
    minutes3 = 1
    print(solution.maxSatisfied(customers3, grumpy3, minutes3))  # Expected output: 25

    # Test case 4
    customers4 = [1, 2, 3, 4, 5]
    grumpy4 = [1, 1, 1, 1, 1]
    minutes4 = 5
    print(solution.maxSatisfied(customers4, grumpy4, minutes4))  # Expected output: 15

    # Test case 5
    customers5 = [10, 1, 7]
    grumpy5 = [0, 1, 0]
    minutes5 = 1
    print(solution.maxSatisfied(customers5, grumpy5, minutes5))  # Expected output: 18

test_max_satisfied()
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total = 0
        while n > 0:
            total += n % k
            n //= k
        return total

def test_sum_base():
    solution = Solution()

    # Test Case 1
    n1, k1 = 34, 6
    print(solution.sumBase(n1, k1))  # Expected Output: 9

    # Test Case 2
    n2, k2 = 10, 10
    print(solution.sumBase(n2, k2))  # Expected Output: 1

    # Test Case 3
    n3, k3 = 100, 3
    print(solution.sumBase(n3, k3))  # Expected Output: 4

    # Test Case 4
    n4, k4 = 50, 5
    print(solution.sumBase(n4, k4))  # Expected Output: 5

    # Test Case 5
    n5, k5 = 25, 2
    print(solution.sumBase(n5, k5))  # Expected Output: 7

test_sum_base()
class Solution:
    def isThree(self, n: int) -> bool:
        count = 0

        for i in range(1, n +1):
            if n % i == 0:
                count += 1
        return True if count == 3 else False

def test_is_three():
    solution = Solution()

    # Test Case 1
    n1 = 2
    print(solution.isThree(n1))  # Expected output: False

    # Test Case 2
    n2 = 4
    print(solution.isThree(n2))  # Expected output: True

    # Test Case 3
    n3 = 98769
    print(solution.isThree(n3))  # Expected output: False

    # Test Case 4
    n4 = 16
    print(solution.isThree(n4))  # Expected output: False

    # Test Case 5
    n5 = 25
    print(solution.isThree(n5))  # Expected output: True

test_is_three()
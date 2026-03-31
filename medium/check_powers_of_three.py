class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

def test_check_powers_of_three():
    solution = Solution()

    # Test case 1
    n1 = 12
    print(solution.checkPowersOfThree(n1))  # Expected output: True

    # Test case 2
    n2 = 91
    print(solution.checkPowersOfThree(n2))  # Expected output: True

    # Test case 3
    n3 = 21
    print(solution.checkPowersOfThree(n3))  # Expected output: False

    # Test case 4
    n4 = 99999
    print(solution.checkPowersOfThree(n4))  # Expected output: False

    # Test case 5
    n5 = 3
    print(solution.checkPowersOfThree(n5))  # Expected output: True

test_check_powers_of_three()
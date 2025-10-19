class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

def test_is_power_of_three():
    s = Solution()

    # Test Case 1: n is a power of three
    n = 27
    print(s.isPowerOfThree(n))  # Expected: True

    # Test Case 2: n is not a power of three
    n = 10
    print(s.isPowerOfThree(n))  # Expected: False

    # Test Case 3: n is 1 (3^0)
    n = 1
    print(s.isPowerOfThree(n))  # Expected: True

    # Test Case 4: n is negative
    n = -3
    print(s.isPowerOfThree(n))  # Expected: False

    # Test Case 5: n is zero
    n = 0
    print(s.isPowerOfThree(n))  # Expected: False

    # Test Case 6: Large power of three
    n = 1162261467
    print(s.isPowerOfThree(n))  # Expected: True

    # Test Case 7: Large non-power of three
    n = 1162261466
    print(s.isPowerOfThree(n))  # Expected: False

    # Test Case 8: Smallest negative number
    n = -1
    print(s.isPowerOfThree(n))  # Expected: False

    # Test Case 9: Large positive number not a power of three
    n = 1000000000
    print(s.isPowerOfThree(n))  # Expected: False

    # Test Case 10: Edge case with n = 3
    n = 3
    print(s.isPowerOfThree(n))  # Expected: True

test_is_power_of_three()
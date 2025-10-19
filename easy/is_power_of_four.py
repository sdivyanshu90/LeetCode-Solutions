class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4
        return True

def test_is_power_of_four():
    s = Solution()

    # Test Case 1: n is a power of four
    n = 16
    print(s.isPowerOfFour(n))  # Expected: True

    # Test Case 2: n is not a power of four
    n = 8
    print(s.isPowerOfFour(n))  # Expected: False

    # Test Case 3: n is 1 (4^0)
    n = 1
    print(s.isPowerOfFour(n))  # Expected: True

    # Test Case 4: n is negative
    n = -4
    print(s.isPowerOfFour(n))  # Expected: False

    # Test Case 5: n is zero
    n = 0
    print(s.isPowerOfFour(n))  # Expected: False

    # Test Case 6: Large power of four
    n = 1073741824  # 4^15
    print(s.isPowerOfFour(n))  # Expected: True

    # Test Case 7: Large non-power of four
    n = 1073741823
    print(s.isPowerOfFour(n))  # Expected: False

    # Test Case 8: Smallest negative number
    n = -1
    print(s.isPowerOfFour(n))  # Expected: False

    # Test Case 9: Large positive number not a power of four
    n = 1000000000
    print(s.isPowerOfFour(n))  # Expected: False

    # Test Case 10: Edge case with n = 4
    n = 4
    print(s.isPowerOfFour(n))  # Expected: True

test_is_power_of_four()
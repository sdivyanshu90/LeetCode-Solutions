class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return (n & (n - 1)) == 0

def test_is_power_of_two():
    s = Solution()

    # Test Case 1: A standard power of two
    n = 16
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: True

    # Test Case 2: A number that is not a power of two
    n = 18
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: False

    # Test Case 3: The number 1 (2^0), an important edge case
    n = 1
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: True

    # Test Case 4: The number 0 (edge case)
    n = 0
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: False

    # Test Case 5: A negative number (edge case)
    n = -16
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: False

    # Test Case 6: The number 2 itself
    n = 2
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: True

    # Test Case 7: A large power of two
    n = 1073741824 # 2^30
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: True

    # Test Case 8: A large number that is not a power of two
    n = 1073741825 # 2^30 + 1
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: False
    
    # Test Case 9: A number just below a power of two
    n = 1023 # 2^10 - 1
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: False

    # Test Case 10: The maximum integer value in many systems
    n = 2147483647 # 2^31 - 1
    print(f"\nInput: {n}")
    print(f"Output: {s.isPowerOfTwo(n)}") # Expected: False

test_is_power_of_two()
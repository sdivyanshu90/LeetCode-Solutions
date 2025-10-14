# Approach 1
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count("1")

# Approach 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

def test_hamming_weight():
    s = Solution()

    # Test Case 1
    n = 11
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 3

    # Test Case 2: Zero
    n = 0
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 0

    # Test Case 3: One
    n = 1
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 1

    # Test Case 4: A power of 2
    n = 128
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 1

    # Test Case 5: A number with all bits set (2^k - 1)
    n = 15 # Binary: 1111
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 4

    # Test Case 6: A number with alternating bits
    n = 170 # Binary: 10101010
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 4
    
    # Test Case 7: A moderately large number
    n = 12345 # Binary: 11000000111001
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 6

    # Test Case 8: A large power of 2
    n = 1073741824 # 2^30
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 1

    # Test Case 9: Maximum 32-bit unsigned integer
    n = 4294967295 # 2^32 - 1
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 32

    # Test Case 10: A large number with one bit unset
    n = 4294967294 # (2^32 - 2)
    print(f"Input: {n}, Output: {s.hammingWeight(n)}") # Expected: 31

test_hamming_weight()
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans

def test_minimum_one_bit_operations():
    solution = Solution()

    # Test case 1
    n = 0
    print(solution.minimumOneBitOperations(n))  # Expected output: 0

    # Test case 2
    n = 3
    print(solution.minimumOneBitOperations(n))  # Expected output: 2

    # Test case 3
    n = 6
    print(solution.minimumOneBitOperations(n))  # Expected output: 4

    # Test case 4
    n = 9
    print(solution.minimumOneBitOperations(n))  # Expected output: 14

    # Test case 5
    n = 500000000
    print(solution.minimumOneBitOperations(n))  # Expected output: 378124799

test_minimum_one_bit_operations()
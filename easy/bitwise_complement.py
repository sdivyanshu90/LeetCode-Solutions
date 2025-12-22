class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join('1' if bit == '0' else '0' for bit in bin(n)[2:]), 2)

def test_bitwise_complement():
    solution = Solution()

    # Test case 1
    n1 = 5
    print(solution.bitwiseComplement(n1))  # Expected output: 2

    # Test case 2
    n2 = 7
    print(solution.bitwiseComplement(n2))  # Expected output: 0

    # Test case 3
    n3 = 10
    print(solution.bitwiseComplement(n3))  # Expected output: 5

    # Test case 4
    n4 = 0
    print(solution.bitwiseComplement(n4))  # Expected output: 1

    # Test case 5
    n5 = 1
    print(solution.bitwiseComplement(n5))  # Expected output: 0

test_bitwise_complement()
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        lsb = k & -k
        inverted = (k // lsb >> 1) & 1
        original = (k & 1) ^ 1
        return str(original ^ inverted)

def test_find_kth_bit():
    solution = Solution()

    # Test case 1
    n1, k1 = 3, 1
    print(solution.findKthBit(n1, k1))  # Expected output: "0"

    # Test case 2
    n2, k2 = 4, 11
    print(solution.findKthBit(n2, k2))  # Expected output: "1"

    # Test case 3
    n3, k3 = 1, 1
    print(solution.findKthBit(n3, k3))  # Expected output: "0"

    # Test case 4
    n4, k4 = 5, 16
    print(solution.findKthBit(n4, k4))  # Expected output: "0"

    # Test case 5
    n5, k5 = 6, 63
    print(solution.findKthBit(n5, k5))  # Expected output: "1"

test_find_kth_bit()
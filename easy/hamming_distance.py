class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")

def test_hamming_distance():
    s = Solution()

    # Test case 1
    x = 1
    y = 4
    print(s.hammingDistance(x, y))  # Expected output: 2

    # Test case 2
    x = 3
    y = 1
    print(s.hammingDistance(x, y))  # Expected output: 1

    # Test case 3
    x = 0
    y = 0
    print(s.hammingDistance(x, y))  # Expected output: 0

    # Test case 4
    x = 15
    y = 0
    print(s.hammingDistance(x, y))  # Expected output: 4

    # Test case 5
    x = 7
    y = 14
    print(s.hammingDistance(x, y))  # Expected output: 2

test_hamming_distance()
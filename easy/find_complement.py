class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1
        return num ^ mask

def test_find_complement():
    s = Solution()

    # Test case 1
    num = 5
    print(s.findComplement(num))  # Expected output: 2

    # Test case 2
    num = 1
    print(s.findComplement(num))  # Expected output: 0

    # Test case 3
    num = 0
    print(s.findComplement(num))  # Expected output: 1

    # Test case 4
    num = 10
    print(s.findComplement(num))  # Expected output: 5

    # Test case 5
    num = 7
    print(s.findComplement(num))  # Expected output: 0

test_find_complement()
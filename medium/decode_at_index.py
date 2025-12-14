class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():
                return char
            if char.isdigit():
                size /= int(char)
            else:
                size -= 1

        return ""

def test_decode_at_index():
    solution = Solution()

    # Test case 1
    s1 = "leet2code3"
    k1 = 10
    print(solution.decodeAtIndex(s1, k1))  # Expected output: "o"

    # Test case 2
    s2 = "ha22"
    k2 = 5
    print(solution.decodeAtIndex(s2, k2))  # Expected output: "h"

    # Test case 3
    s3 = "a2345678999999999999999"
    k3 = 1
    print(solution.decodeAtIndex(s3, k3))  # Expected output: "a"

    # Test case 4
    s4 = "abc3"
    k4 = 8
    print(solution.decodeAtIndex(s4, k4))  # Expected output: "b"

    # Test case 5
    s5 = "a2b3c4d5e6f7g8h9"
    k5 = 100
    print(solution.decodeAtIndex(s5, k5))  # Expected output: "a"


test_decode_at_index()
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            digit_sum = carry

            if i >= 0:
                digit_sum += int(num1[i])
                i -= 1

            if j >= 0:
                digit_sum += int(num2[j])
                j -= 1

            result.append(str(digit_sum % 10))
            carry = digit_sum // 10

        return ''.join(result[::-1])


def test_add_strings():
    s = Solution()

    # Test case 1
    print(s.addStrings("11", "123"))  # Expected output: "134"

    # Test case 2
    print(s.addStrings("456", "77"))   # Expected output: "533"

    # Test case 3
    print(s.addStrings("0", "0"))      # Expected output: "0"

    # Test case 4
    print(s.addStrings("999", "1"))    # Expected output: "1000"

    # Test case 5
    print(s.addStrings("1", "9999"))   # Expected output: "10000"

    # Test case 6
    print(s.addStrings("123456789", "987654321"))  # Expected output: "1111111110"

    # Test case 7
    print(s.addStrings("500", "500"))  # Expected output: "1000"

    # Test case 8
    print(s.addStrings("123", "9876")) # Expected output: "9999"

    # Test case 9
    print(s.addStrings("1000", "9000")) # Expected output: "10000"

    # Test case 10
    print(s.addStrings("12345678901234567890", "98765432109876543210")) # Expected output: "111111111011111111100"

test_add_strings()
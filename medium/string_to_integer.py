class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()        
        if not s:
            return 0
        
        sign = 1
        num = 0
        i = 0
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1
        
        num = num * sign
        num = max(min(num, 2**31 - 1), -2**31)
        return num

def test_string_to_integer():
    solution = Solution()

    # Test Case 1: Normal case with positive number
    s = "42"
    print(solution.myAtoi(s))  # Expected output: 42

    # Test Case 2: Normal case with negative number
    s = "   -42"
    print(solution.myAtoi(s))  # Expected output: -42

    # Test Case 3: Case with leading and trailing spaces
    s = "   +0 123"
    print(solution.myAtoi(s))  # Expected output: 0

    # Test Case 4: Case with non-numeric characters after number
    s = "4193 with words"
    print(solution.myAtoi(s))  # Expected output: 4193

    # Test Case 5: Case with non-numeric characters before number
    s = "words and 987"
    print(solution.myAtoi(s))  # Expected output: 0

    # Test Case 6: Overflow case (positive)
    s = "91283472332"
    print(solution.myAtoi(s))  # Expected output: 2147483647

    # Test Case 7: Overflow case (negative)
    s = "-91283472332"
    print(solution.myAtoi(s))  # Expected output: -2147483648

    # Test Case 8: Empty string
    s = ""
    print(solution.myAtoi(s))  # Expected output: 0

    # Test Case 9: String with only spaces
    s = "7 Thala for a reason"
    print(solution.myAtoi(s))  # Expected output: 7

    # Test Case 10: String with only sign
    s = "590+ Rejection still counting"
    print(solution.myAtoi(s))  # Expected output: 590

test_string_to_integer()
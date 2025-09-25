# Approach 1
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        total += values[s[-1]]
        return total

# Approach 2
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        max_right = 0
        for ch in reversed(s):
            val = values[ch]
            if val < max_right:
                total -= val
            else:
                total += val
                max_right = val
        return total

def test_roman_to_int():
    solution = Solution()

    # Test case 1
    s = "III"
    print(solution.romanToInt(s))  # Expected output: 3

    # Test case 2
    s = "IV"
    print(solution.romanToInt(s))  # Expected output: 4

    # Test case 3
    s = "IX"
    print(solution.romanToInt(s))  # Expected output: 9

    # Test case 4
    s = "LVIII"
    print(solution.romanToInt(s))  # Expected output: 58

    # Test case 5
    s = "MCMXCIV"
    print(solution.romanToInt(s))  # Expected output: 1994

    # Test case 6
    s = "XLII"
    print(solution.romanToInt(s))  # Expected output: 42

    # Test case 7
    s = "XCIX"
    print(solution.romanToInt(s))  # Expected output: 99

    # Test case 8
    s = "CDXLIV"
    print(solution.romanToInt(s))  # Expected output: 444

    # Test case 9
    s = "MMXXI"
    print(solution.romanToInt(s))  # Expected output: 2021

    # Test case 10
    s = "DCCCXC"
    print(solution.romanToInt(s))  # Expected output: 890

test_roman_to_int()
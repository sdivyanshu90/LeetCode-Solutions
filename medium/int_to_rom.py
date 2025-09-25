# # Approach 1
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         roman_numerals = {
#             1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
#             50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
#             900: "CM", 1000: "M"
#         }

#         ans = ""
#         for value, symbol in sorted(roman_numerals.items(), reverse=True):
#             while num >= value:
#                 ans += symbol
#                 num -= value

#         return ans

# Approach 2
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = []
        for value, symbol in roman_numerals:
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)

def test_int_to_roman():
    solution = Solution()

    # Test case 1
    num = 3
    print(solution.intToRoman(num))  # Expected output: "III"

    # Test case 2
    num = 4
    print(solution.intToRoman(num))  # Expected output: "IV"

    # Test case 3
    num = 9
    print(solution.intToRoman(num))  # Expected output: "IX"

    # Test case 4
    num = 58
    print(solution.intToRoman(num))  # Expected output: "LVIII"

    # Test case 5
    num = 1994
    print(solution.intToRoman(num))  # Expected output: "MCMXCIV"

    # Test case 6
    num = 1
    print(solution.intToRoman(num))  # Expected output: "I"

    # Test case 7
    num = 3999
    print(solution.intToRoman(num))  # Expected output: "MMMCMXCIX"

    # Test case 8
    num = 44
    print(solution.intToRoman(num))  # Expected output: "XLIV"

    # Test case 9
    num = 945
    print(solution.intToRoman(num))  # Expected output: "CMXLV"

    # Test case 10
    num = 2021
    print(solution.intToRoman(num))  # Expected output: "MMXXI"

test_int_to_roman()
# # Approach 1
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = 1
#         if x < 0:
#             sign = -1
#             x = abs(x)
        
#         reversed_str = str(x)[::-1]
#         reversed_int = int(reversed_str)
        
#         reversed_int *= sign        
#         if reversed_int < -2**31 or reversed_int > 2**31 - 1:
#             return 0
        
#         return reversed_int

# Approach 2
class Solution:
    def reverse(self, x: int) -> int:
        min = -2 ** 31
        max = 2 **31 -1

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            if reversed_num > (max - digit) // 10:
                return 0

            reversed_num  = reversed_num * 10 + digit

        return reversed_num * sign

def test_reverse_integer():
    solution = Solution()

    # Test Case 1: Normal case
    x = 123
    print(solution.reverse(x))  # Expected output: 321

    # Test Case 2: Negative number
    x = -123
    print(solution.reverse(x))  # Expected output: -321

    # Test Case 3: Number with trailing zeros
    x = 120
    print(solution.reverse(x))  # Expected output: 21

    # Test Case 4: Overflow case (positive)
    x = 1534236469
    print(solution.reverse(x))  # Expected output: 0

    # Test Case 5: Overflow case (negative)
    x = -1534236469
    print(solution.reverse(x))  # Expected output: 0
    
    # Test Case 6: Zero
    x = 0
    print(solution.reverse(x))  # Expected output: 0

    # Test Case 7: Single digit
    x = 5
    print(solution.reverse(x))  # Expected output: 5

    # Test Case 8: Large negative number
    x = 1234567890
    print(solution.reverse(x))  # Expected output: 987654321

    # Test Case 9: Large positive number
    x = 999999999
    print(solution.reverse(x))  # Expected output: 999999999

    # Test Case 10: Minimum 32-bit integer
    x = -2147483648
    print(solution.reverse(x))  # Expected output: 0

test_reverse_integer()
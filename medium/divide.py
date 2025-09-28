class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == 0:
            return 0
        
        if divisor == 1:
            return min(MAX_INT, max(MIN_INT, dividend))
        
        if divisor == -1:
            return min(MAX_INT, max(MIN_INT, -dividend))
        
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            dividend -= temp_divisor
            quotient += multiple
            
        return min(MAX_INT, max(MIN_INT, sign * quotient))

def test_divide():
    solution = Solution()

    # Test case 1: Basic case
    dividend1 = 10
    divisor1 = 3
    result1 = solution.divide(dividend1, divisor1)
    print(result1)  # Expected output: 3

    # Test case 2: Negative dividend
    dividend2 = -10
    divisor2 = 3
    result2 = solution.divide(dividend2, divisor2)
    print(result2)  # Expected output: -3

    # Test case 3: Negative divisor
    dividend3 = 10
    divisor3 = -3
    result3 = solution.divide(dividend3, divisor3)
    print(result3)  # Expected output: -3

    # Test case 4: Both negative
    dividend4 = -10
    divisor4 = -3
    result4 = solution.divide(dividend4, divisor4)
    print(result4)  # Expected output: 3

    # Test case 5: Dividend is zero
    dividend5 = 0
    divisor5 = 1
    result5 = solution.divide(dividend5, divisor5)
    print(result5)  # Expected output: 0

    # Test case 6: Divisor is one
    dividend6 = 7
    divisor6 = 1
    result6 = solution.divide(dividend6, divisor6)
    print(result6)  # Expected output: 7

    # Test case 7: Divisor is negative one
    dividend7 = -7
    divisor7 = -1
    result7 = solution.divide(dividend7, divisor7)
    print(result7)  # Expected output: 7

    # Test case 8: Large numbers causing overflow
    dividend8 = -2**31
    divisor8 = -1
    result8 = solution.divide(dividend8, divisor8)
    print(result8)  # Expected output: 2147483647 (MAX_INT)

    # Test case 9: Dividing by a larger number
    dividend9 = 5
    divisor9 = 10
    result9 = solution.divide(dividend9, divisor9)
    print(result9)  # Expected output: 0

    # Test case 10: Dividing by itself
    dividend10 = 12345
    divisor10 = 12345
    result10 = solution.divide(dividend10, divisor10)
    print(result10)  # Expected output: 1

test_divide()
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)

        integer_part = n // d
        remainder = n % d
        if remainder == 0:
            return sign + str(integer_part)

        result = [sign + str(integer_part), "."]
        seen = {}

        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                result.insert(idx, "(")
                result.append(")")
                break
            seen[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // d))
            remainder %= d

        return "".join(result)

def test_fraction_to_decimal():
    s = Solution()

    # Test Case 1: Zero numerator
    print(s.fractionToDecimal(0, 7)) # Expected Output: 0

    # Test Case 2: No fractional part (perfect division)
    print(s.fractionToDecimal(10, 2)) # Expected Output: 5
    
    # Test Case 3: Simple terminating decimal
    print(s.fractionToDecimal(1, 2)) # Expected Output: 0.5
    
    # Test Case 4: Simple repeating decimal
    print(s.fractionToDecimal(1, 3)) # Expected Output: 0.(3)
    
    # Test Case 5: Delayed repeating decimal
    print(s.fractionToDecimal(1, 6)) # Expected Output: 0.1(6)

    # Test Case 6: Negative numerator
    print(s.fractionToDecimal(-1, 3)) # Expected Output: -0.(3)

    # Test Case 7: Negative denominator
    print(s.fractionToDecimal(5, -8)) # Expected Output: -0.625

    # Test Case 8: Both numerator and denominator are negative
    print(s.fractionToDecimal(-4, -3)) # Expected Output: 1.(3)
    
    # Test Case 9: Long repeating cycle
    print(s.fractionToDecimal(1, 7)) # Expected Output: 0.(142857)

    # Test Case 10: Numerator is larger than the denominator
    print(s.fractionToDecimal(22, 7)) # Expected Output: 3.(142857)

test_fraction_to_decimal()
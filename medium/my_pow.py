# Approach 1: Recursive Exponentiation by Squaring
# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion stack
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1.0
            elif exponent % 2 == 0:
                return func(base * base, exponent // 2)
            else:
                return base * func(base * base, (exponent - 1) // 2)
            
        if n >= 0:
            return float(func())
        else:
            return (1/func())

# Approach 2: Simple Recursion
# Time Complexity: O(n) in the worst case (when n is negative and odd)
# Space Complexity: O(n) due to recursion stack
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1.0

#         if n % 2 == 0:
#             half_pow = self.myPow(x, n // 2)
#             return half_pow * half_pow

#         if n < 0:
#             return 1.0 / self.myPow(x, -n)
#         else:
#             return x * self.myPow(x, n - 1)

def test_my_pow():
    s = Solution()
    
    # Test case 1: Positive exponent
    print(s.myPow(2.0, 10))  # Expected output: 1024.0

    # Test case 2: Negative exponent
    print(s.myPow(2.0, -2))  # Expected output: 0.25

    # Test case 3: Zero exponent
    print(s.myPow(2.0, 0))   # Expected output: 1.0

    # Test case 4: Fractional base with positive exponent
    print(s.myPow(0.5, 3))   # Expected output: 0.125

    # Test case 5: Fractional base with negative exponent
    print(s.myPow(0.5, -3))  # Expected output: 8.0

    # Test case 6: Large positive exponent
    print(s.myPow(1.00001, 100000))  # Expected output: Approximately 2.71815

    # Test case 7: Large negative exponent
    print(s.myPow(1.00001, -100000)) # Expected output: Approximately 0.36788

    # Test case 8: Base is zero and positive exponent
    print(s.myPow(0.0, 5))   # Expected output: 0.0

    # Test case 9: Base is zero and zero exponent (undefined but often treated as 1)
    print(s.myPow(0.0, 0))   # Expected output: 1.0

    # Test case 10: Base is negative and odd exponent
    print(s.myPow(-2.0, 3))  # Expected output: -8.0

test_my_pow()
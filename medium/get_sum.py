class Solution:
    # Approach 1: Using bit manipulation (XOR and AND)
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask in hexadecimal
        mask = 0xFFFFFFFF
        
        while b != 0:
            # XOR gives sum without carry
            # AND and left shift gives carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # Handle negative numbers in Python
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
    
    # Approach 2: Using recursion with bit manipulation
    # def getSum2(self, a: int, b: int) -> int:
    #     mask = 0xFFFFFFFF
        
    #     if b == 0:
    #         return a if a <= 0x7FFFFFFF else ~(a ^ mask)
        
    #     # Sum without carry
    #     sum_without_carry = (a ^ b) & mask
    #     # Carry
    #     carry = ((a & b) << 1) & mask
        
    #     return self.getSum2(sum_without_carry, carry)
    
    # Approach 3: Using logarithm (mathematical approach)
    # def getSum3(self, a: int, b: int) -> int:
    #     import math
        
    #     if a == 0:
    #         return b
    #     if b == 0:
    #         return a
        
    #     # Handle negative numbers
    #     if a < 0 and b < 0:
    #         return -self.getSum3(-a, -b)
    #     if a < 0:
    #         return -self.getSum3(-a, -b) if -a > b else self.getSum3(b, a)
    #     if b < 0:
    #         return -self.getSum3(-b, -a) if -b > a else self.getSum3(a, b)
        
    #     # Both positive
    #     return int(math.log2(2**a * 2**b))
    
    # Approach 4: Using built-in sum (simple approach)
    # def getSum4(self, a: int, b: int) -> int:
    #     return sum([a, b])


def test_get_sum():
    solution = Solution()
    
    # Test case 1
    print(solution.getSum(1, 2)) # Expected output: 3
    
    # Test case 2
    print(solution.getSum(-1, 1)) # Expected output: 0

    # Test case 3: Edge case - both zeros
    print(solution.getSum(0, 0)) # Expected output: 0

    # Test case 4: Large positive numbers
    print(solution.getSum(1000000, 2000000)) # Expected output: 3000000
    
    # Test case 5: Large negative numbers
    print(solution.getSum(-1000000, -2000000)) # Expected output: -3000000

    # Test case 6: Mixed large numbers
    print(solution.getSum(123456789, -987654321)) # Expected output: -864197532

    # Test case 7: One zero
    print(solution.getSum(0, 5)) # Expected output: 5

    # Test case 8: Both negative and positive
    print(solution.getSum(-5, 10)) # Expected output: 5

    # Test case 9: Same negative numbers
    print(solution.getSum(-3, -3)) # Expected output: -6

    # Test case 10: Same positive numbers
    print(solution.getSum(7, 7)) # Expected output: 14

test_get_sum()
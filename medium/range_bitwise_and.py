class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_count = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift_count += 1
        return left << shift_count

def test_range_bitwise_and():
    s = Solution()

    # Test Case 1: Standard case
    left, right = 5, 7
    # 5: 101, 6: 110, 7: 111 -> AND is 100
    print(f"\nInput: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 4

    # Test Case 2: Range where the result is zero
    left, right = 0, 1
    # 0: 0, 1: 1 -> AND is 0
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 0

    # Test Case 3: Range with only one number
    left, right = 7, 7
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 7

    # Test Case 4: Range starts at zero
    left, right = 0, 15
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 0

    # Test Case 5: A range that does not cross a power of two
    left, right = 12, 15
    # 12: 1100, 13: 1101, 14: 1110, 15: 1111 -> AND is 1100
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 12

    # Test Case 6: A range that crosses a power of two
    left, right = 7, 8
    # 7: 0111, 8: 1000 -> Common prefix is empty
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 0

    # Test Case 7: A wider range with a clear common prefix
    left, right = 128, 191
    # 128: 10000000, 191: 10111111 -> Common prefix is 10000000
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 128
    
    # Test Case 8: The entire 32-bit integer range
    left, right = 0, 2147483647
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 0

    # Test Case 9: A very tight range with large numbers
    left, right = 2147483646, 2147483647
    # The only difference is the last bit.
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 2147483646

    # Test Case 10: A range where the result is the lower bound
    left, right = 1000, 1002
    # 1000: 1111101000, 1001: 1111101001, 1002: 1111101010 -> AND is 1000
    print(f"Input: left = {left}, right = {right}. Output: {s.rangeBitwiseAnd(left, right)}") # Expected: 1000

test_range_bitwise_and()
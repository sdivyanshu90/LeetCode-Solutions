from typing import List

# The provided Solution class
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        mask = x & -x
        ans1, ans2 = 0, 0
        for num in nums:
            if num & mask:
                ans1 ^= num
            else:
                ans2 ^= num
        return [ans1, ans2]

def test_single_number():
    s = Solution()

    # Test Case 1: Negative Numbers
    nums1 = [-1, -5, 2, 2, 4, 4]
    print(f"\nInput: {nums1}")
    print(s.singleNumber(nums1)) # Expected: [-1, -5] or [-5, -1]

    # Test Case 2: One Unique Number is Zero
    nums2 = [1, 1, 2, 2, 3, 3, 0, 99]
    print(f"\nInput: {nums2}")
    print(s.singleNumber(nums2)) # Expected: [0, 99] or [99, 0]

    # Test Case 3: Unique Numbers are Max and Min 32-bit Integers
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    nums3 = [INT_MAX, INT_MIN, 10, 10]
    print(f"\nInput: {nums3}")
    print(s.singleNumber(nums3)) # Expected: [2147483647, -2147483648] or vice-versa

    # Test Case 4: Unique Numbers Differ Only by the Least Significant Bit
    nums4 = [100, 100, 20, 20, 8, 9]
    print(f"\nInput: {nums4}")
    print(s.singleNumber(nums4)) # Expected: [8, 9] or [9, 8]

    # Test Case 5: Unique Numbers Differ Only by a High-Order Bit
    nums5 = [6, 2, 5, 5, 7, 7, 15, 15]
    print(f"\nInput: {nums5}")
    print(s.singleNumber(nums5)) # Expected: [6, 2] or [2, 6]

    # Test Case 6: The Smallest Possible Input (no duplicates)
    nums6 = [47, -81]
    print(f"\nInput: {nums6}")
    print(s.singleNumber(nums6)) # Expected: [47, -81] or [-81, 47]

    # Test Case 7: Unique numbers are a number and its bitwise NOT
    a = 12345
    not_a = ~a # which is -12346
    nums7 = [a, not_a, 0, 0, -5, -5]
    print(f"\nInput: {nums7}")
    print(s.singleNumber(nums7)) # Expected: [12345, -12346] or vice-versa

    # Test Case 8: All Numbers in the List are Negative
    nums8 = [-2, -2, -4, -4, -8, -16]
    print(f"\nInput: {nums8}")
    print(s.singleNumber(nums8)) # Expected: [-8, -16] or [-16, -8]
    
    # Test Case 9: Long list with unique numbers far apart
    nums9 = [5, 1000000, 10, 15, 20, -1000000, 10, 5, 15, 20]
    print(f"\nInput: {nums9}")
    print(s.singleNumber(nums9)) # Expected: [1000000, -1000000] or vice-versa
    
    # Test Case 10: Unique numbers are powers of two
    nums10 = [8, 32, 1, 1, 2, 2, 4, 4]
    print(f"\nInput: {nums10}")
    print(s.singleNumber(nums10)) # Expected: [8, 32] or [32, 8]

test_single_number()
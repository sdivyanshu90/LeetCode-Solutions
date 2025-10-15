from typing import List
import random

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        sum_of_nums = sum(nums)
        return total - sum_of_nums

def test_missing_number():
    s = Solution()

    # Test Case 1: Missing the last number (n)
    nums1 = [0, 1, 2, 3, 4]
    print(f"\nInput: {nums1}")
    print(s.missingNumber(nums1)) # Expected: 5

    # Test Case 2: Missing the first number (0)
    nums2 = [1, 2, 3, 4, 5]
    print(f"\nInput: {nums2}")
    print(s.missingNumber(nums2)) # Expected: 0

    # Test Case 3: Heavily shuffled list with a middle number missing
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"\nInput: {nums3}")
    print(s.missingNumber(nums3)) # Expected: 8

    # Test Case 4: The smallest possible list where n is missing
    nums4 = [0]
    print(f"\nInput: {nums4}")
    print(s.missingNumber(nums4)) # Expected: 1

    # Test Case 5: The smallest possible list where 0 is missing
    nums5 = [1]
    print(f"\nInput: {nums5}")
    print(s.missingNumber(nums5)) # Expected: 0

    # Test Case 6: A list sorted in descending order
    nums6 = [8, 7, 6, 5, 3, 2, 1, 0]
    print(f"\nInput: {nums6}")
    print(s.missingNumber(nums6)) # Expected: 4

    # Test Case 7: An almost sorted list
    nums7 = [0, 1, 2, 3, 5, 6, 7, 8]
    print(f"\nInput: {nums7}")
    print(s.missingNumber(nums7)) # Expected: 4
    
    # Test Case 8: Minimal non-trivial case
    nums8 = [0, 1, 3]
    print(f"\nInput: {nums8}")
    print(s.missingNumber(nums8)) # Expected: 2

    # Test Case 9: Large shuffled list
    n9 = 500
    nums9 = list(range(n9 + 1))
    nums9.remove(251)
    random.shuffle(nums9)
    print(f"\nInput: A shuffled list of 500 numbers from range [0, 500] with 251 missing.")
    print(s.missingNumber(nums9)) # Expected: 251

    # Test Case 10: A tricky shuffled sequence
    nums10 = [0, 1, 2, 3, 4, 8, 7, 6]
    print(f"\nInput: {nums10}")
    print(s.missingNumber(nums10)) # Expected: 5

test_missing_number()
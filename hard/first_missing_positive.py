from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

def test_first_missing_positive():
    s = Solution()
    
    # Test case 1: Regular case with mixed positive and negative numbers
    print(s.firstMissingPositive([3,4,-1,1]))  # Expected output: 2

    # Test case 2: Consecutive positive numbers starting from 1
    print(s.firstMissingPositive([1,2,0]))  # Expected output: 3

    # Test case 3: All negative numbers
    print(s.firstMissingPositive([-1,-2,-3]))  # Expected output: 1

    # Test case 4: Empty array
    print(s.firstMissingPositive([]))  # Expected output: 1

    # Test case 5: Single element array with positive number
    print(s.firstMissingPositive([1]))  # Expected output: 2

    # Test case 6: Single element array with negative number
    print(s.firstMissingPositive([-1]))  # Expected output: 1

    # Test case 7: Array with duplicates
    print(s.firstMissingPositive([1,1,2,2]))  # Expected output: 3

    # Test case 8: Large range of numbers with gaps
    print(s.firstMissingPositive([7,8,9,11,12]))  # Expected output: 1

    # Test case 9: Array with all numbers present from 1 to n
    print(s.firstMissingPositive([1,2,3,4,5]))  # Expected output: 6

    # Test case 10: Random order with missing number in between
    print(s.firstMissingPositive([2,3,7,6,8,-1,-10,15]))  # Expected output: 1

test_first_missing_positive()
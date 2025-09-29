from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        temp = 0

        for num in nums:
            if temp < 0:
                temp = 0
            temp += num
            res = max(res, temp)
        return res

def test_max_sub_array():
    s = Solution()

    # Test case 1: Regular case with positive and negative numbers
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected output: 6

    # Test case 2: All negative numbers
    print(s.maxSubArray([-1,-2,-3,-4]))  # Expected output: -1

    # Test case 3: Single element array
    print(s.maxSubArray([5]))  # Expected output: 5

    # Test case 4: Mixed positive and negative numbers
    print(s.maxSubArray([1,-1,2,-2,3,-3,4,-4]))  # Expected output: 4

    # Test case 5: Large array with zeros
    print(s.maxSubArray([0,0,0,0,0]))  # Expected output: 0

    # Test case 6: Increasing sequence
    print(s.maxSubArray([1,2,3,4,5]))  # Expected output: 15

    # Test case 7: Decreasing sequence
    print(s.maxSubArray([5,4,3,2,1]))  # Expected output: 15

    # Test case 8: Array with large positive and negative numbers
    print(s.maxSubArray([1000,-1001,2000,-2001,3000]))  # Expected output: 3000

    # Test case 9: Array with alternating large positive and negative numbers
    print(s.maxSubArray([1000,-999,1000,-999,1000]))  # Expected output: 2001

    # Test case 10: Array with multiple maximum subarrays
    print(s.maxSubArray([1,-1,1,-1,1,-1,1]))  # Expected output: 1

test_max_sub_array()
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0

def test_largest_perimeter():
    solution = Solution()
    
    # Test case 1
    nums = [2,1,2]
    print(solution.largestPerimeter(nums))  # Expected output: 5

    # Test case 2
    nums = [1,2,1]
    print(solution.largestPerimeter(nums))  # Expected output: 0

    # Test case 3
    nums = [3,2,3,4]
    print(solution.largestPerimeter(nums))  # Expected output: 10

    # Test case 4
    nums = [3,6,2,3]
    print(solution.largestPerimeter(nums))  # Expected output: 8

    # Test case 5
    nums = [1,2,3,4,5,10]
    print(solution.largestPerimeter(nums))  # Expected output: 12

test_largest_perimeter()
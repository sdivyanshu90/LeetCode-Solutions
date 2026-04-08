from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

def test_max_product_difference():
    solution = Solution()

    # Test case 1
    nums = [5, 6, 2, 7, 4]
    print(solution.maxProductDifference(nums))  # Expected output: 34

    # Test case 2
    nums = [1, 2, 3, 4]
    print(solution.maxProductDifference(nums))  # Expected output: 4

    # Test case 3
    nums = [10, 2, 5, 2]
    print(solution.maxProductDifference(nums))  # Expected output: 46

    # Test case 4
    nums = [1, 1, 1, 1]
    print(solution.maxProductDifference(nums))  # Expected output: 0

    # Test case 5
    nums = [1000, 999, 998, 997]
    print(solution.maxProductDifference(nums))  # Expected output: (1000*999) - (997*998) = (999000) - (995006) = 3994

test_max_product_difference()
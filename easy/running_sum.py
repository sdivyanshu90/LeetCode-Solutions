from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        return nums

def test_running_sum():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 4]
    print(solution.runningSum(nums))  # Expected output: [1, 3, 6, 10]

    # Test case 2
    nums = [1, 1, 1, 1, 1]
    print(solution.runningSum(nums))  # Expected output: [1, 2, 3, 4, 5]

    # Test case 3
    nums = [3, 1, 2, 10]
    print(solution.runningSum(nums))  # Expected output: [3, 4, 6, 16]

    # Test case 4
    nums = [0]
    print(solution.runningSum(nums))  # Expected output: [0]

    # Test case 5
    nums = [5]
    print(solution.runningSum(nums))  # Expected output: [5]

test_running_sum()
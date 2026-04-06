from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        for i in range(len(nums) // 2):
            maxSum = max(maxSum, nums[i] + nums[len(nums) - i - 1])
        return maxSum

def test_min_pair_sum():
    solution = Solution()

    # Test case 1
    nums1 = [3, 5, 2, 3]
    print(solution.minPairSum(nums1))  # Expected output: 7

    # Test case 2
    nums2 = [3, 5, 4, 2, 4, 6]
    print(solution.minPairSum(nums2))  # Expected output: 8

    # Test case 3
    nums3 = [1, 2, 3, 4]
    print(solution.minPairSum(nums3))  # Expected output: 5

    # Test case 4
    nums4 = [1, 1, 1, 1]
    print(solution.minPairSum(nums4))  # Expected output: 2

    # Test case 5
    nums5 = [1, 100000]
    print(solution.minPairSum(nums5))  # Expected output: 100001

test_min_pair_sum()
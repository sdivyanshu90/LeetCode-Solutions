from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        score = []
        i = 0
        j = len(nums)
        while i <= j - k:
            diff = nums[i + k - 1] - nums[i]
            score.append(diff)
            i += 1
        return min(score)

def test_minimum_difference():
    solution = Solution()

    # Test case 1
    nums1 = [90]
    k1 = 1
    print(solution.minimumDifference(nums1, k1))  # Expected output: 0

    # Test case 2
    nums2 = [9, 4, 1, 7]
    k2 = 2
    print(solution.minimumDifference(nums2, k2))  # Expected output: 2

    # Test case 3
    nums3 = [1, 3, 6]
    k3 = 3
    print(solution.minimumDifference(nums3, k3))  # Expected output: 5

    # Test case 4
    nums4 = [10, 100, 300, 200, 1000]
    k4 = 3
    print(solution.minimumDifference(nums4, k4))  # Expected output: 190

    # Test case 5
    nums5 = [1, 2, 3, 4, 10]
    k5 = 4
    print(solution.minimumDifference(nums5, k5))  # Expected output: 3

test_minimum_difference()
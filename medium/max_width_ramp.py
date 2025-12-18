from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [i for i in range(n)]
        indices.sort(key=lambda i: (nums[i], i))

        min_index = n
        max_width = 0

        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width

def test_max_width_ramp():
    solution = Solution()

    # Test case 1
    nums1 = [6,0,8,2,1,5]
    print(solution.maxWidthRamp(nums1))  # Expected output: 4

    # Test case 2
    nums2 = [9,8,1,0,1,9,4,0,4,1]
    print(solution.maxWidthRamp(nums2))  # Expected output: 7

    # Test case 3
    nums3 = [1,2,3,4,5]
    print(solution.maxWidthRamp(nums3))  # Expected output: 4

    # Test case 4
    nums4 = [5,4,3,2,1]
    print(solution.maxWidthRamp(nums4))  # Expected output: 0

    # Test case 5
    nums5 = [1,0,1,0,1]
    print(solution.maxWidthRamp(nums5))  # Expected output: 4

test_max_width_ramp()
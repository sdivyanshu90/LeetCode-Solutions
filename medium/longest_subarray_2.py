from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        best_len = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best_len = max(best_len, right - left + 1)

        return best_len - 1

def test_longest_subarray():
    solution = Solution()

    # Test Case 1
    nums1 = [1, 1, 0, 1]
    print(solution.longestSubarray(nums1))  # Expected output: 3

    # Test Case 2
    nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(solution.longestSubarray(nums2))  # Expected output: 5

    # Test Case 3
    nums3 = [1, 1, 1]
    print(solution.longestSubarray(nums3))  # Expected output: 2

    # Test Case 4
    nums4 = [0, 0, 0]
    print(solution.longestSubarray(nums4))  # Expected output: 0

    # Test Case 5
    nums5 = [1, 0, 1, 0, 1]
    print(solution.longestSubarray(nums5))  # Expected output: 2

test_longest_subarray()
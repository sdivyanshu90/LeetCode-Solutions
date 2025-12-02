from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        dp_lengths = [1] * n
        dp_counts = [1] * n
        max_length = 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp_lengths[i] == dp_lengths[j] + 1:
                        dp_counts[i] += dp_counts[j]
                    elif dp_lengths[i] < dp_lengths[j] + 1:
                        dp_lengths[i] = dp_lengths[j] + 1
                        dp_counts[i] = dp_counts[j]

            max_length = max(max_length, dp_lengths[i])

        result = sum(count for length, count in zip(dp_lengths, dp_counts) if length == max_length)
        return result

def test_find_number_of_LIS():
    solution = Solution()

    # Test Case 1
    nums1 = [10,9,2,5,3,7,101,18]
    print(solution.findNumberOfLIS(nums1))  # Expected: 1

    # Test Case 2
    nums2 = [2,2,2,2,2]
    print(solution.findNumberOfLIS(nums2))  # Expected: 5

    # Test Case 3
    nums3 = [1,3,5,4,7]
    print(solution.findNumberOfLIS(nums3))  # Expected: 2

    # Test Case 4
    nums4 = [1]
    print(solution.findNumberOfLIS(nums4))  # Expected: 1

    # Test Case 5
    nums5 = [1,2,4,3,5,4,7,2]
    print(solution.findNumberOfLIS(nums5))  # Expected: 3

test_find_number_of_LIS()
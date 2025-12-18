from typing import List
from collections import defaultdict

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(len(nums)):

            freq[nums[i]] = freq[nums[i]] + 1

            if freq[nums[i]] > 1:
                return nums[i]

def test_repeated_n_times():
    solution = Solution()

    # Test case 1
    nums1 = [1,2,3,3]
    print(solution.repeatedNTimes(nums1))  # Expected output: 3

    # Test case 2
    nums2 = [2,1,2,5,3,2]
    print(solution.repeatedNTimes(nums2))  # Expected output: 2

    # Test case 3
    nums3 = [5,1,5,2,5,3,5,4]
    print(solution.repeatedNTimes(nums3))  # Expected output: 5

    # Test case 4
    nums4 = [9,5,6,9]
    print(solution.repeatedNTimes(nums4))  # Expected output: 9

    # Test case 5
    nums5 = [4,4,4,4]
    print(solution.repeatedNTimes(nums5))  # Expected output: 4

test_repeated_n_times()
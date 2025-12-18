from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        min_increments = 0

        frequency_count = [0] * (n + max_val + 1)
        for val in nums:
            frequency_count[val] += 1

        for i in range(len(frequency_count)):
            if frequency_count[i] <= 1:
                continue

            duplicates = frequency_count[i] - 1
            frequency_count[i + 1] += duplicates
            frequency_count[i] = 1
            min_increments += duplicates

        return min_increments

def test_min_increment_for_unique():
    solution = Solution()

    # Test case 1
    nums1 = [1,2,2]
    print(solution.minIncrementForUnique(nums1))  # Expected output: 1

    # Test case 2
    nums2 = [3,2,1,2,1,7]
    print(solution.minIncrementForUnique(nums2))  # Expected output: 6

    # Test case 3
    nums3 = [0,0,0,0,0]
    print(solution.minIncrementForUnique(nums3))  # Expected output: 10

    # Test case 4
    nums4 = [1,1,1,1]
    print(solution.minIncrementForUnique(nums4))  # Expected output: 6

    # Test case 5
    nums5 = [2,2,2,1,1,1]
    print(solution.minIncrementForUnique(nums5))  # Expected output: 12

test_min_increment_for_unique()
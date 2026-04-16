from typing import List
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        
        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            ans = min(ans, n - count)

        return ans

def test_min_operations():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(solution.minOperations(nums1))  # Expected output: 0

    # Test case 2
    nums2 = [1, 2, 2, 3]
    print(solution.minOperations(nums2))  # Expected output: 1

    # Test case 3
    nums3 = [1, 1, 1, 1]
    print(solution.minOperations(nums3))  # Expected output: 3

    # Test case 4
    nums4 = [1, 2, 3, 5]
    print(solution.minOperations(nums4))  # Expected output: 1

    # Test case 5
    nums5 = [10, 11, 12, 13]
    print(solution.minOperations(nums5))  # Expected output: 0

test_min_operations()
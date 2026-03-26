from typing import List
import math

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            middle = (left + right) // 2

            if self._is_possible(middle, nums, maxOperations):
                right = middle
            else:
                left = middle + 1

        return left

    def _is_possible(self, max_balls_in_bag: int, nums: List[int], max_operations: int):
        total_operations = 0

        for num in nums:
            operations = math.ceil(num / max_balls_in_bag) - 1
            total_operations += operations

            if total_operations > max_operations:
                return False

        return True

def test_minimum_size():
    solution = Solution()

    # Test Case 1
    nums1 = [9]
    max_operations1 = 2
    print(solution.minimumSize(nums1, max_operations1)) # Expected Output: 3

    # Test Case 2
    nums2 = [2, 4, 8, 2]
    max_operations2 = 4
    print(solution.minimumSize(nums2, max_operations2)) # Expected Output: 2

    # Test Case 3
    nums3 = [7, 17]
    max_operations3 = 2
    print(solution.minimumSize(nums3, max_operations3)) # Expected Output: 7

    # Test Case 4
    nums4 = [1000000000]
    max_operations4 = 1000000000
    print(solution.minimumSize(nums4, max_operations4)) # Expected Output: 1

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    max_operations5 = 0
    print(solution.minimumSize(nums5, max_operations5)) # Expected Output: 1

test_minimum_size()
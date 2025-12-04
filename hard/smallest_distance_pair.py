from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        array_size = len(nums)

        low = 0
        high = nums[array_size - 1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            count = self._count_pairs_with_max_distance(nums, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low

    def _count_pairs_with_max_distance(
        self, nums: List[int], max_distance: int
    ) -> int:
        count = 0
        array_size = len(nums)
        left = 0

        for right in range(array_size):
            while nums[right] - nums[left] > max_distance:
                left += 1
            count += right - left
        return count

def test_smallest_distance_pair():
    solution = Solution()

    # Test Case 1
    nums = [1, 3, 1]
    k = 1
    print(solution.smallestDistancePair(nums, k))  # Expected: 0

    # Test Case 2
    nums = [1, 6, 1]
    k = 3
    print(solution.smallestDistancePair(nums, k))  # Expected: 5

    # Test Case 3: All elements are the same
    nums = [2, 2, 2]
    k = 2
    print(solution.smallestDistancePair(nums, k))  # Expected: 0

    # Test Case 4: Increasing sequence
    nums = [1, 2, 3, 4, 5]
    k = 4
    print(solution.smallestDistancePair(nums, k))  # Expected: 1

    # Test Case 5: Decreasing sequence
    nums = [5, 4, 3, 2, 1]
    k = 6
    print(solution.smallestDistancePair(nums, k))  # Expected: 2

    # Test Case 6: Large range of numbers
    nums = [1, 1000000]
    k = 1
    print(solution.smallestDistancePair(nums, k))  # Expected: 999999

    # Test Case 7: Mixed numbers
    nums = [10, 20, 30, 40, 50]
    k = 7
    print(solution.smallestDistancePair(nums, k))  # Expected: 20

    # Test Case 8: Single element array (edge case)
    nums = [42]
    k = 1
    print(solution.smallestDistancePair(nums, k))  # Expected: 0

    # Test Case 9: Two elements array
    nums = [1, 3]
    k = 1
    print(solution.smallestDistancePair(nums, k))  # Expected: 2

    # Test Case 10: Large array with small differences
    nums = [1] * 1000 + [2] * 1000
    k = 1500
    print(solution.smallestDistancePair(nums, k))  # Expected: 1

test_smallest_distance_pair()
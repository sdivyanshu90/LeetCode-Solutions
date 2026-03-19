from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = [1] * N
        lds_length = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals

def test_minimum_mountain_removals():
    solution = Solution()

    # Test case 1
    nums = [1, 3, 1]
    print(solution.minimumMountainRemovals(nums))  # Expected output: 0

    # Test case 2
    nums = [2, 1, 1, 5, 6, 2, 3, 1]
    print(solution.minimumMountainRemovals(nums))  # Expected output: 3

    # Test case 3
    nums = [4, 3, 2, 1, 1, 2, 3, 1]
    print(solution.minimumMountainRemovals(nums))  # Expected output: 4

    # Test case 4
    nums = [1, 2, 3, 4, 5]
    print(solution.minimumMountainRemovals(nums))  # Expected output: inf

    # Test case 5
    nums = [5, 4, 3, 2, 1]
    print(solution.minimumMountainRemovals(nums))  # Expected output: inf

test_minimum_mountain_removals()
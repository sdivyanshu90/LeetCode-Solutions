from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = 0

        for num in nums:
            total_sum = (total_sum + num) % p

        target = total_sum % p
        if target == 0:
            return 0
        mod_map = {
            0: -1
        }
        current_sum = 0
        min_len = n

        for i in range(n):
            current_sum = (current_sum + nums[i]) % p
            needed = (current_sum - target + p) % p
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            mod_map[current_sum] = i
        return -1 if min_len == n else min_len

def test_min_subarray():
    solution = Solution()

    # Test case 1
    nums = [3, 1, 4, 2]
    p = 6
    print(solution.minSubarray(nums, p))  # Expected output: 1

    # Test case 2
    nums = [6, 3, 5, 2]
    p = 9
    print(solution.minSubarray(nums, p))  # Expected output: 2

    # Test case 3
    nums = [1, 2, 3]
    p = 3
    print(solution.minSubarray(nums, p))  # Expected output: 0

    # Test case 4
    nums = [1, 2, 3]
    p = 7
    print(solution.minSubarray(nums, p))  # Expected output: -1

    # Test case 5
    nums = [1000000000,1000000000,1000000000]
    p = 3
    print(solution.minSubarray(nums, p))  # Expected output: 0

test_min_subarray()
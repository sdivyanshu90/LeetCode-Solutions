from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [0] * (2 * total_sum + 1)

        dp[nums[0] + total_sum] = 1
        dp[-nums[0] + total_sum] += 1

        for index in range(1, len(nums)):
            next_dp = [0] * (2 * total_sum + 1)
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[sum_val + total_sum] > 0:
                    next_dp[sum_val + nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
                    next_dp[sum_val - nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
            dp = next_dp

        return 0 if abs(target) > total_sum else dp[target + total_sum]

def test_find_target_sum_ways():
    solution = Solution()

    # Test case 1
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(solution.findTargetSumWays(nums, target))  # Expected output: 5

    # Test case 2
    nums = [1]
    target = 1
    print(solution.findTargetSumWays(nums, target))  # Expected output: 1

    # Test case 3
    nums = [1, 2, 3]
    target = 4
    print(solution.findTargetSumWays(nums, target))  # Expected output: 2

    # Test case 4
    nums = [0, 0, 0, 0, 0]
    target = 0
    print(solution.findTargetSumWays(nums, target))  # Expected output: 32

    # Test case 5
    nums = [2, 3, 5, 7]
    target = 10
    print(solution.findTargetSumWays(nums, target))  # Expected output: 1

test_find_target_sum_ways()
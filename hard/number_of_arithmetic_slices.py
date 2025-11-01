from typing import List
import collections

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        dp = [collections.defaultdict(int) for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result


def test_number_of_arithmetic_slices():
    s = Solution()

    # Test case 1
    nums = [2, 4, 6, 8, 10]
    print(s.numberOfArithmeticSlices(nums))  # Expected output: 7

    # Test case 2
    nums = [7, 7, 7, 7, 7]
    print(s.numberOfArithmeticSlices(nums))  # Expected output: 16

    # Test case 3
    nums = [3, -1, -5, -9]
    print(s.numberOfArithmeticSlices(nums))  # Expected output: 3

    # Test case 4
    nums = [1, 2, 3, 4]
    print(s.numberOfArithmeticSlices(nums))  # Expected output: 3

    # Test case 5
    nums = [1, 3, 5, 7, 9, 11]
    print(s.numberOfArithmeticSlices(nums))  # Expected output: 12

test_number_of_arithmetic_slices()
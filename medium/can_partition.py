from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

def test_can_partition():
    s = Solution()

    # Test case 1
    print(s.canPartition([1, 5, 11, 5]))  # Expected output: True

    # Test case 2
    print(s.canPartition([1, 2, 3, 5]))   # Expected output: False

    # Test case 3
    print(s.canPartition([2, 2, 3, 5]))   # Expected output: False

    # Test case 4
    print(s.canPartition([3, 3, 3, 4, 5])) # Expected output: True

    # Test case 5
    print(s.canPartition([1, 2, 5]))      # Expected output: False

    # Test case 6
    print(s.canPartition([1, 1]))         # Expected output: True

    # Test case 7
    print(s.canPartition([1, 2, 3, 4, 5, 6, 7])) # Expected output: True

    # Test case 8
    print(s.canPartition([100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                         100, 100, 100, 100, 100, 100, 100, 100, 100, 100])) # Expected output: True

    # Test case 9
    print(s.canPartition([1]))             # Expected output: False

    # Test case 10
    print(s.canPartition([2, 2, 2, 2]))    # Expected output: True

test_can_partition()
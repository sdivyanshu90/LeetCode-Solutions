from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(len(arr) - 1, -1, -1):
            m = 0
            for j in range(i, min(i + k, len(arr))):
                dp[i] = max(dp[i], (m := max(m, arr[j])) * (j - i + 1) + dp[j + 1])
        return dp[0]

def test_max_sum_after_partitioning():
    solution = Solution()

    # Test case 1
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    print(solution.maxSumAfterPartitioning(arr, k))  # Expected output: 84

    # Test case 2
    arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k = 4
    print(solution.maxSumAfterPartitioning(arr, k))  # Expected output: 83

    # Test case 3
    arr = [1]
    k = 1
    print(solution.maxSumAfterPartitioning(arr, k))  # Expected output: 1

    # Test case 4
    arr = [2, 3, 5, 1, 6]
    k = 2
    print(solution.maxSumAfterPartitioning(arr, k))  # Expected output: 24

    # Test case 5
    arr = [10, 20, 30]
    k = 1
    print(solution.maxSumAfterPartitioning(arr, k))  # Expected output: 60

test_max_sum_after_partitioning()
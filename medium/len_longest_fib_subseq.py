from collections import defaultdict
from bisect import bisect_left
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        max_len = 0

        for curr in range(2, n):
            start = 0
            end = curr - 1

            while start < end:
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    dp[end][curr] = dp[start][end] + 1
                    max_len = max(dp[end][curr], max_len)
                    end -= 1
                    start += 1

        return max_len + 2 if max_len else 0

def test_len_longest_fib_subseq():
    solution = Solution()

    # Test case 1
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(solution.lenLongestFibSubseq(arr1))  # Expected output: 5

    # Test case 2
    arr2 = [1, 3, 7, 11, 12, 14, 18]
    print(solution.lenLongestFibSubseq(arr2))  # Expected output: 3

    # Test case 3
    arr3 = [2, 4, 7, 11, 16, 18, 23, 29, 37, 47]
    print(solution.lenLongestFibSubseq(arr3))  # Expected output: 5

    # Test case 4
    arr4 = [1, 4, 5, 6, 7, 8, 9, 10]
    print(solution.lenLongestFibSubseq(arr4))  # Expected output: 0

    # Test case 5
    arr5 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(solution.lenLongestFibSubseq(arr5))  # Expected output: 10

test_len_longest_fib_subseq()
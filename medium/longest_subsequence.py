from collections import defaultdict
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for i in arr:
            dp[i] = dp[i - difference] + 1
        return max(dp.values())

def test_longest_subsequence():
    solution = Solution()

    # Test Case 1
    arr1 = [1,2,3,4]
    difference1 = 1
    print(solution.longestSubsequence(arr1, difference1))  # Expected Output: 4

    # Test Case 2
    arr2 = [1,3,5,7]
    difference2 = 1
    print(solution.longestSubsequence(arr2, difference2))  # Expected Output: 1

    # Test Case 3
    arr3 = [1,5,7,8,5,3,4,2,1]
    difference3 = -2
    print(solution.longestSubsequence(arr3, difference3))  # Expected Output: 4

    # Test Case 4
    arr4 = [3,0,-3,4,-4,-7,-6,-5]
    difference4 = -3
    print(solution.longestSubsequence(arr4, difference4))  # Expected Output: 4

    # Test Case 5
    arr5 = [10,13,16,19,22,25,28]
    difference5 = 3
    print(solution.longestSubsequence(arr5, difference5))  # Expected Output: 7

test_longest_subsequence()
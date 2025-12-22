from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        max_length = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if (j, diff) in dp:
                    dp[i, diff] = dp[j, diff] + 1
                else:
                    dp[i, diff] = 2
                max_length = max(max_length, dp[i, diff])

        return max_length

def test_longest_arith_seq_length():
    solution = Solution()

    # Test case 1
    nums1 = [3,6,9,12]
    print(solution.longestArithSeqLength(nums1))  # Expected output: 4

    # Test case 2
    nums2 = [9,4,7,2,10]
    print(solution.longestArithSeqLength(nums2))  # Expected output: 3

    # Test case 3
    nums3 = [20,1,15,3,10,5,8]
    print(solution.longestArithSeqLength(nums3))  # Expected output: 4

    # Test case 4
    nums4 = [1,2,3,4,5,6]
    print(solution.longestArithSeqLength(nums4))  # Expected output: 6

    # Test case 5
    nums5 = [7,7,7,7,7]
    print(solution.longestArithSeqLength(nums5))  # Expected output: 5

test_longest_arith_seq_length()
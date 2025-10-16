from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

def test_length_of_LIS():
    s = Solution()

    # Test Case 1: Typical case with mixed increasing and decreasing subsequences
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))  # Expected: 4

    # Test Case 2: Empty input
    nums = []
    print(s.lengthOfLIS(nums))  # Expected: 0

    # Test Case 3: Single element
    nums = [1]
    print(s.lengthOfLIS(nums))  # Expected: 1

    # Test Case 4: All elements are the same
    nums = [5, 5, 5, 5]
    print(s.lengthOfLIS(nums))  # Expected: 1

    # Test Case 5: Strictly increasing sequence
    nums = [1, 2, 3, 4, 5, 6]
    print(s.lengthOfLIS(nums))  # Expected: 6

    # Test Case 6: Strictly decreasing sequence
    nums = [6, 5, 4, 3, 2, 1]
    print(s.lengthOfLIS(nums))  # Expected: 1

    # Test Case 7: Mixed increasing and decreasing subsequences
    nums = [10, 9, 8, 3, 7, 5, 6, 8, 4, 10]
    print(s.lengthOfLIS(nums))  # Expected: 5

    # Test Case 8: Multiple increasing subsequences
    nums = [3, 10, 2, 1, 20]
    print(s.lengthOfLIS(nums))  # Expected: 3 (LIS = [3, 10, 20])

    # Test Case 9: Alternating increasing and decreasing elements
    nums = [1, 3, 2, 4, 3, 5]
    print(s.lengthOfLIS(nums))  # Expected: 4 (LIS = [1, 2, 3, 5])

    # Test Case 10: Long input with random numbers
    nums = [0, 8, 4, 5, 6, 7, 3, 9, 10, 1, 2]
    print(s.lengthOfLIS(nums))  # Expected: 7 (LIS = [0, 4, 5, 6, 7, 9])

# Run the test function
test_length_of_LIS()
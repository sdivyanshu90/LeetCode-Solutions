class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

        return max_prefix_sum - min_prefix_sum

def test_max_absolute_sum():
    solution = Solution()

    # Test Case 1
    nums1 = [1, -3, 2, 3, -4]
    print(solution.maxAbsoluteSum(nums1)) # Expected Output: 5

    # Test Case 2
    nums2 = [2, -5, 1, -4, 3, -2]
    print(solution.maxAbsoluteSum(nums2)) # Expected Output: 8

    # Test Case 3
    nums3 = [1, 2, 3]
    print(solution.maxAbsoluteSum(nums3)) # Expected Output: 6

    # Test Case 4
    nums4 = [-1, -2, -3]
    print(solution.maxAbsoluteSum(nums4)) # Expected Output: 6

    # Test Case 5
    nums5 = [0, 0, 0]
    print(solution.maxAbsoluteSum(nums5)) # Expected Output: 0

test_max_absolute_sum()
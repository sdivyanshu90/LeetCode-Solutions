class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        curr_sum = 0
        result = []

        for num in nums:
            curr_sum += num
            result.append(num)
            if curr_sum > total_sum - curr_sum:
                return result

def test_min_subsequence():
    solution = Solution()

    # Test case 1
    nums1 = [4, 3, 10, 9, 8]
    print(solution.minSubsequence(nums1))  # Expected output: [10, 9]

    # Test case 2
    nums2 = [4, 4, 7, 6, 7]
    print(solution.minSubsequence(nums2))  # Expected output: [7, 7, 6]

    # Test case 3
    nums3 = [6]
    print(solution.minSubsequence(nums3))  # Expected output: [6]

    # Test case 4
    nums4 = [1, 2, 3]
    print(solution.minSubsequence(nums4))  # Expected output: [3]

    # Test case 5
    nums5 = [1, 1, 1, 1]
    print(solution.minSubsequence(nums5))  # Expected output: [1, 1]

test_min_subsequence()
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums = [num for num in nums if num < target]
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                size = right - left
                res = (res + pow(2, size, MOD)) % MOD
                left += 1
        return res

def test_num_subseq():
    solution = Solution()

    # Test Case 1
    nums1 = [3, 5, 6, 7]
    target1 = 9
    print(solution.numSubseq(nums1, target1))  # Expected output: 4

    # Test Case 2
    nums2 = [3, 3, 6, 8]
    target2 = 10
    print(solution.numSubseq(nums2, target2))  # Expected output: 6

    # Test Case 3
    nums3 = [2, 3, 3, 4, 6, 7]
    target3 = 12
    print(solution.numSubseq(nums3, target3))  # Expected output: 61

    # Test Case 4
    nums4 = [5, 2, 4, 1, 7, 6, 8]
    target4 = 16
    print(solution.numSubseq(nums4, target4))  # Expected output: 127

    # Test Case 5
    nums5 = [1] * (10 ** 5)
    target5 = 2
    print(solution.numSubseq(nums5, target5))  # Expected output: (2^100000 - 1) % (10^9 + 7)

test_num_subseq()
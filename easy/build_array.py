class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans

def test_build_array():
    solution = Solution()

    # Test case 1
    nums1 = [0, 2, 1, 5, 3, 4]
    print(solution.buildArray(nums1))  # Expected output: [0, 1, 2, 4, 5, 3]

    # Test case 2
    nums2 = [5, 0, 1, 2, 3, 4]
    print(solution.buildArray(nums2))  # Expected output: [4, 5, 0, 1, 2, 3]

    # Test case 3
    nums3 = [0, 1, 2, 3, 4]
    print(solution.buildArray(nums3))  # Expected output: [0, 1, 2, 3, 4]

    # Test case 4
    nums4 = [1, 0]
    print(solution.buildArray(nums4))  # Expected output: [0, 1]

    # Test case 5
    nums5 = [0]
    print(solution.buildArray(nums5))  # Expected output: [0]

test_build_array()
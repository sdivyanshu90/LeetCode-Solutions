class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return -1
        minEle = nums[0]
        maxDiff = -1
        for i in range(1, len(nums)):
            if nums[i] <= minEle:
                minEle = nums[i]
            else:
                maxDiff = max(maxDiff, nums[i] - minEle)

        return maxDiff

def test_maximum_difference():
    solution = Solution()

    # Test case 1
    nums1 = [7, 1, 5, 4]
    print(solution.maximumDifference(nums1))  # Expected output: 4

    # Test case 2
    nums2 = [9, 4, 3, 2]
    print(solution.maximumDifference(nums2))  # Expected output: -1

    # Test case 3
    nums3 = [1, 5, 2, 10]
    print(solution.maximumDifference(nums3))  # Expected output: 9

    # Test case 4
    nums4 = [10, 8, 6, 4]
    print(solution.maximumDifference(nums4))  # Expected output: -1

    # Test case 5
    nums5 = [1, 2, 3, 4, 5]
    print(solution.maximumDifference(nums5))  # Expected output: 4

test_maximum_difference()
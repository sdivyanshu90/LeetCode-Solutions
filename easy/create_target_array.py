class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res

def test_create_target_array():
    solution = Solution()

    # Test case 1
    nums1 = [0, 1, 2, 3, 4]
    index1 = [0, 1, 2, 2, 1]
    print(solution.createTargetArray(nums1, index1))  # Expected output: [0, 4, 1, 3, 2]

    # Test case 2
    nums2 = [1, 2, 3, 4, 0]
    index2 = [0, 1, 2, 3, 0]
    print(solution.createTargetArray(nums2, index2))  # Expected output: [0, 1, 2, 3, 4]

    # Test case 3
    nums3 = [1]
    index3 = [0]
    print(solution.createTargetArray(nums3, index3))  # Expected output: [1]

    # Test case 4
    nums4 = [1, 2, 3]
    index4 = [0, 0, 0]
    print(solution.createTargetArray(nums4, index4))  # Expected output: [3, 2, 1]

    # Test case 5
    nums5 = [1, 2, 3]
    index5 = [2, 0, 1]
    print(solution.createTargetArray(nums5, index5))  # Expected output: [2, 3, 1]

test_create_target_array()
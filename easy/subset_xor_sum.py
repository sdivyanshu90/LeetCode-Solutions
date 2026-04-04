class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num
        return result << (len(nums) - 1)

def test_subset_xor_sum():
    solution = Solution()

    # Test case 1
    nums1 = [1, 3]
    print(solution.subsetXORSum(nums1))  # Expected output: 6

    # Test case 2
    nums2 = [5, 1, 6]
    print(solution.subsetXORSum(nums2))  # Expected output: 28

    # Test case 3
    nums3 = [3, 4, 5, 6, 7, 8]
    print(solution.subsetXORSum(nums3))  # Expected output: 480

    # Test case 4
    nums4 = [1]
    print(solution.subsetXORSum(nums4))  # Expected output: 1

    # Test case 5
    nums5 = [2, 3, 4]
    print(solution.subsetXORSum(nums5))  # Expected output: 28

test_subset_xor_sum()
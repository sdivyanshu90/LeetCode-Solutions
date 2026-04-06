class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        step = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                step += 1
            count += step
        return count

def test_reduction_operations():
    solution = Solution()

    # Test case 1
    nums1 = [5, 1, 3]
    print(solution.reductionOperations(nums1))  # Expected output: 3

    # Test case 2
    nums2 = [1, 1, 1]
    print(solution.reductionOperations(nums2))  # Expected output: 0

    # Test case 3
    nums3 = [1, 1, 2, 2, 3]
    print(solution.reductionOperations(nums3))  # Expected output: 4

    # Test case 4
    nums4 = [5, 5, 5, 5]
    print(solution.reductionOperations(nums4))  # Expected output: 0

    # Test case 5
    nums5 = [10, 9, 8, 7]
    print(solution.reductionOperations(nums5))  # Expected output: 6

test_reduction_operations()
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase, decrease = True, True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decrease = False
            elif nums[i] < nums[i - 1]:
                increase = False
        return increase or decrease

def test_is_monotonic():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 2, 3]
    print(solution.isMonotonic(nums1))  # Expected output: True

    # Test case 2
    nums2 = [6, 5, 4, 4]
    print(solution.isMonotonic(nums2))  # Expected output: True

    # Test case 3
    nums3 = [1, 3, 2]
    print(solution.isMonotonic(nums3))  # Expected output: False

    # Test case 4
    nums4 = [1, 2, 4, 5]
    print(solution.isMonotonic(nums4))  # Expected output: True

    # Test case 5
    nums5 = [1, 1, 1]
    print(solution.isMonotonic(nums5))  # Expected output: True

test_is_monotonic()
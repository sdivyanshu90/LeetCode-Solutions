from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        inversion_count = 0
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1

        if nums[0] < nums[n - 1]:
            inversion_count += 1

        return inversion_count <= 1

def test_check():
    solution = Solution()

    # Test Case 1
    nums1 = [3, 4, 5, 1, 2]
    print(solution.check(nums1)) # Expected Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(solution.check(nums2)) # Expected Output: True

    # Test Case 3
    nums3 = [2, 1, 3, 4, 5]
    print(solution.check(nums3)) # Expected Output: False

    # Test Case 4
    nums4 = [1]
    print(solution.check(nums4)) # Expected Output: True

    # Test Case 5
    nums5 = [1, 2]
    print(solution.check(nums5)) # Expected Output: True

test_check()
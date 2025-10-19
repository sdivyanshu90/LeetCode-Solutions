from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        length_nums = len(nums)
        ans = 0
        i = 0
        upto = 0
        while upto < n:
            if i < length_nums and nums[i] <= upto + 1:
                upto += nums[i]
                i += 1
            else:
                ans += 1
                upto += upto + 1
        return ans 

def test_min_patches():
    s = Solution()
    
    # Test Case 1: Example with missing patches
    nums = [1, 3]
    n = 6
    print(s.minPatches(nums, n))  # Expected: 1

    # Test Case 2: No patches needed
    nums = [1, 2, 2]
    n = 5
    print(s.minPatches(nums, n))  # Expected: 0

    # Test Case 3: Large n with no initial numbers
    nums = []
    n = 7
    print(s.minPatches(nums, n))  # Expected: 3

    # Test Case 4: Large array with no patches needed
    nums = [1, 2, 4, 8, 16]
    n = 31
    print(s.minPatches(nums, n))  # Expected: 0

    # Test Case 5: Large n with some patches needed
    nums = [1, 5, 10]
    n = 20
    print(s.minPatches(nums, n))  # Expected: 2

    # Test Case 6: Edge case with n = 1
    nums = []
    n = 1
    print(s.minPatches(nums, n))  # Expected: 1

    # Test Case 7: Edge case with large n and small nums
    nums = [1, 2, 31]
    n = 50
    print(s.minPatches(nums, n))  # Expected: 3

    # Test Case 8: All numbers present up to n
    nums = [1, 2, 3, 4, 5]
    n = 15
    print(s.minPatches(nums, n))  # Expected: 0

    # Test Case 9: Sparse array needing multiple patches
    nums = [2, 4, 8]
    n = 20
    print(s.minPatches(nums, n))  # Expected: 2

    # Test Case 10: Large array with gaps
    nums = [1, 3, 6, 10]
    n = 20
    print(s.minPatches(nums, n))  # Expected: 1

test_min_patches()
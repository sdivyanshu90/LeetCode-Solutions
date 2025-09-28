from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return left

def test_search_insert():
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [1,3,5,6]
    target1 = 5
    result1 = solution.searchInsert(nums1, target1)
    print(result1)  # Expected output: 2

    # Test case 2: Target not in array, should be inserted at the end
    nums2 = [1,3,5,6]
    target2 = 7
    result2 = solution.searchInsert(nums2, target2)
    print(result2)  # Expected output: 4

    # Test case 3: Target not in array, should be inserted at the beginning
    nums3 = [1,3,5,6]
    target3 = 0
    result3 = solution.searchInsert(nums3, target3)
    print(result3)  # Expected output: 0

    # Test case 4: Target not in array, should be inserted in the middle
    nums4 = [1,3,5,6]
    target4 = 2
    result4 = solution.searchInsert(nums4, target4)
    print(result4)  # Expected output: 1

    # Test case 5: Single element array (target present)
    nums5 = [1]
    target5 = 1
    result5 = solution.searchInsert(nums5, target5)
    print(result5)  # Expected output: 0

    # Test case 6: Single element array (target absent)
    nums6 = [1]
    target6 = 0
    result6 = solution.searchInsert(nums6, target6)
    print(result6)  # Expected output: 0

    # Test case 7: Empty array
    nums7 = []
    target7 = 5
    result7 = solution.searchInsert(nums7, target7)
    print(result7)  # Expected output: 0

    # Test case 8: Large array
    nums8 = list(range(1000))
    target8 = 500
    result8 = solution.searchInsert(nums8, target8)
    print(result8)  # Expected output: 500
    
    # Test case 9: Large array, target not present
    nums9 = list(range(1000))
    target9 = 1001
    result9 = solution.searchInsert(nums9, target9)
    print(result9)  # Expected output: 1000
    
    # Test case 10: Large array, target not present, should be inserted at the beginning
    nums10 = list(range(1, 1001))
    target10 = 0
    result10 = solution.searchInsert(nums10, target10)
    print(result10)  # Expected output: 0

test_search_insert()
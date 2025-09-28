from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(i):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < i:
                    l = mid + 1
                else:
                    r = mid
            return l

        l = binary_search(target)
        r = binary_search(target + 1) - 1

        if l <= r:
            return[l, r]
        return [-1, -1]

def test_search_range():
    solution = Solution()

    # Test case 1: Basic case with target present
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    result1 = solution.searchRange(nums1, target1)
    print(result1)  # Expected output: [3, 4]

    # Test case 2: Target not in array
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    result2 = solution.searchRange(nums2, target2)
    print(result2)  # Expected output: [-1, -1]

    # Test case 3: Empty array
    nums3 = []
    target3 = 0
    result3 = solution.searchRange(nums3, target3)
    print(result3)  # Expected output: [-1, -1]

    # Test case 4: Single element array (target present)
    nums4 = [1]
    target4 = 1
    result4 = solution.searchRange(nums4, target4)
    print(result4)  # Expected output: [0, 0]

    # Test case 5: Single element array (target absent)
    nums5 = [1]
    target5 = 0
    result5 = solution.searchRange(nums5, target5)
    print(result5)  # Expected output: [-1, -1]

    # Test case 6: All elements are the same and equal to target
    nums6 = [2, 2, 2, 2]
    target6 = 2
    result6 = solution.searchRange(nums6, target6)
    print(result6)  # Expected output: [0, 3]

    # Test case 7: All elements are the same but not equal to target
    nums7 = [3, 3, 3]
    target7 = 2
    result7 = solution.searchRange(nums7, target7)
    print(result7)  # Expected output: [-1, -1]

    # Test case 8: Target at the beginning of the array
    nums8 = [1, 2, 3, 4, 5]
    target8 = 1
    result8 = solution.searchRange(nums8, target8)
    print(result8)  # Expected output: [0, 0]

    # Test case 9: Target at the end of the array
    nums9 = [1, 2, 3, 4, 5]
    target9 = 5
    result9 = solution.searchRange(nums9, target9)
    print(result9)  # Expected output: [4, 4]

    # Test case 10: Large array with multiple occurrences of target
    nums10 = [1]*1000 + [2]*500 + [3]*200
    target10 = 2
    result10 = solution.searchRange(nums10, target10)
    print(result10)  # Expected output: [1000, 1499]

test_search_range()
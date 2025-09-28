from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

def test_search():
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    result1 = solution.search(nums1, target1)
    print(result1)  # Expected output: 4

    # Test case 2: Target not in array
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    result2 = solution.search(nums2, target2)
    print(result2)  # Expected output: -1

    # Test case 3: Single element array (target present)
    nums3 = [1]
    target3 = 1
    result3 = solution.search(nums3, target3)
    print(result3)  # Expected output: 0

    # Test case 4: Single element array (target absent)
    nums4 = [1]
    target4 = 0
    result4 = solution.search(nums4, target4)
    print(result4)  # Expected output: -1

    # Test case 5: No rotation (sorted array)
    nums5 = [1,2,3,4,5]
    target5 = 3
    result5 = solution.search(nums5, target5)
    print(result5)  # Expected output: 2

    # Test case 6: Full rotation (same as sorted array)
    nums6 = [1,2,3,4,5]
    target6 = 4
    result6 = solution.search(nums6, target6)
    print(result6)  # Expected output: 3

    # Test case 7: Target is the smallest element
    nums7 = [6,7,0,1,2,4,5]
    target7 = 0
    result7 = solution.search(nums7, target7)
    print(result7)  # Expected output: 2

    # Test case 8: Target is the largest element
    nums8 = [6,7,0,1,2,4,5]
    target8 = 7
    result8 = solution.search(nums8, target8)
    print(result8)  # Expected output: 1

    # Test case 9: Large array with rotation
    nums9 = list(range(1000, 2000)) + list(range(0, 1000))
    target9 = 1500
    result9 = solution.search(nums9, target9)
    print(result9)  # Expected output: 500

    # Test case 10: Large array without rotation
    nums10 = list(range(2000))
    target10 = 1999
    result10 = solution.search(nums10, target10)
    print(result10)  # Expected output: 1999

test_search()
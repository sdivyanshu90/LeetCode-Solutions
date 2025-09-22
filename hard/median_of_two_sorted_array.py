import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums) - 1
        if len(nums) % 2 == 0:
            a = ((nums[n//2]) + (math.ceil(nums[(n+1)//2])))/2
            return a
        else:
            b = math.ceil(nums[(n+1)//2])
            return b

# Approach 2
# import statistics

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         arr = nums1 + nums2
#         arr.sort()
#         return statistics.median(arr)

# Test Cases
def test_find_median_sorted_arrays():
    solution = Solution()

    # Test Case 1: Two arrays with different lengths (odd total length)
    nums1 = [1, 3]
    nums2 = [2]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 2.0

    # Test Case 2: Two arrays with the same length (even total length)
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 2.5

    # Test Case 3: Arrays with one empty array
    nums1 = []
    nums2 = [1, 2, 3]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 2.0

    # Test Case 4: Arrays with all elements being the same
    nums1 = [5, 5, 5]
    nums2 = [5, 5]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 5.0

    # Test Case 5: Arrays with negative numbers
    nums1 = [-3, -1]
    nums2 = [-2]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: -2.0

    # Test Case 6: Array with one element each
    nums1 = [1]
    nums2 = [2]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 1.5

    # Test Case 7: Arrays where the median is in the middle
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 3.5

    # Test Case 8: Large numbers
    nums1 = [1000000, 2000000]
    nums2 = [3000000, 4000000]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 2500000.0

    # Test Case 9: Arrays with odd total length and large values
    nums1 = [100]
    nums2 = [200, 300, 400]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 250.0

    # Test Case 10: Arrays with only one number each, resulting in an odd total length
    nums1 = [7]
    nums2 = [3]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected output: 5.0


# Run all the test cases
test_find_median_sorted_arrays()
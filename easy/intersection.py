from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

def test_intersection():
    s = Solution()

    # Test Case 1: Basic case with some common elements
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersection(nums1, nums2))  # Expected: [2]

    # Test Case 2: No common elements
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    print(s.intersection(nums1, nums2))  # Expected: []

    # Test Case 3: All elements are common
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    print(s.intersection(nums1, nums2))  # Expected: [1, 2, 3]

    # Test Case 4: One array is empty
    nums1 = []
    nums2 = [1, 2, 3]
    print(s.intersection(nums1, nums2))  # Expected: []

    # Test Case 5: Both arrays are empty
    nums1 = []
    nums2 = []
    print(s.intersection(nums1, nums2))  # Expected: []

    # Test Case 6: Large arrays with some common elements
    nums1 = list(range(100))
    nums2 = list(range(50, 150))
    print(s.intersection(nums1, nums2))  # Expected: [50, 51, ..., 99]

    # Test Case 7: Arrays with negative numbers
    nums1 = [-1, -2, -3, 0]
    nums2 = [-3, -4, -5, 0]
    print(s.intersection(nums1, nums2))  # Expected: [-3, 0]

    # Test Case 8: Arrays with duplicates
    nums1 = [1, 1, 1, 2, 2]
    nums2 = [2, 2, 3, 3]
    print(s.intersection(nums1, nums2))  # Expected: [2]

    # Test Case 9: Single element arrays with common element
    nums1 = [7]
    nums2 = [7]
    print(s.intersection(nums1, nums2))  # Expected: [7]

    # Test Case 10: Single element arrays with no common element
    nums1 = [8]
    nums2 = [9]
    print(s.intersection(nums1, nums2))  # Expected: []

test_intersection()
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[i] = nums[n]
                i += 1
        return i

def test_remove_duplicates():
    solution = Solution()

    # Test case 1: Basic case with duplicates
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(k1, nums1[:k1])

    # Test case 2: No duplicates
    nums2 = [0, 1, 2, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(k2, nums2[:k2])

    # Test case 3: All elements are the same
    nums3 = [5, 5, 5, 5]
    k3 = solution.removeDuplicates(nums3)
    print(k3, nums3[:k3])

    # Test case 4: Empty array
    nums4 = []
    k4 = solution.removeDuplicates(nums4)
    print(k4, nums4[:k4])

    # Test case 5: Single element array
    nums5 = [10]
    k5 = solution.removeDuplicates(nums5)
    print(k5, nums5[:k5])

    # Test case 6: Large array with multiple duplicates
    nums6 = [1]*1000 + [2]*500 + [3]*200 + [4]*100
    k6 = solution.removeDuplicates(nums6)
    print(k6, nums6[:k6])

    # Test case 7: Alternating duplicates
    nums7 = [1, 1, 2, 2, 3, 3, 4, 4]
    k7 = solution.removeDuplicates(nums7)
    print(k7, nums7[:k7])

    # Test case 8: Negative numbers with duplicates
    nums8 = [-1, -1, 0, 0, 1, 1]
    k8 = solution.removeDuplicates(nums8)
    print(k8, nums8[:k8])

    # Test case 9: Large range of numbers with duplicates
    nums9 = list(range(100)) + list(range(50)) + list(range(25))
    nums9.sort()
    k9 = solution.removeDuplicates(nums9)
    print(k9, nums9[:k9])

    # Test case 10: Duplicates at the end
    nums10 = [1, 2, 3, 4, 5, 5, 5, 5]
    k10 = solution.removeDuplicates(nums10)
    print(k10, nums10[:k10])

test_remove_duplicates()
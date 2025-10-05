from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j, k = m - 1, n - 1

        while j >= 0 and k >= 0:
            if nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                i -= 1
                j -= 1
            else:
                nums1[i] = nums2[k]
                i -= 1
                k -= 1

        while k >= 0:
            nums1[i] = nums2[k]
            i -= 1
            k -= 1

def test_merge():
    solution = Solution()

    # Test cases 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)

    # Test cases 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(nums1)

    # Test cases 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1)

    # Test cases 4
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)

    # Test cases 5
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1)

test_merge()
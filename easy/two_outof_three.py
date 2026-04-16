from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2) | set(nums1) & set(nums3) | set(nums2) & set(nums3))

def test_two_out_of_three():
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]
    print(solution.twoOutOfThree(nums1, nums2, nums3))  # Expected output: [3, 2]

    # Test case 2
    nums1 = [3, 1]
    nums2 = [2, 3]
    nums3 = [1, 2]
    print(solution.twoOutOfThree(nums1, nums2, nums3))  # Expected output: [1, 2, 3]

    # Test case 3
    nums1 = [1, 2, 2]
    nums2 = [4, 3, 3]
    nums3 = [5]
    print(solution.twoOutOfThree(nums1, nums2, nums3))  # Expected output: []

    # Test case 4
    nums1 = [1, 1, 1]
    nums2 = [1, 1, 1]
    nums3 = [1, 1, 1]
    print(solution.twoOutOfThree(nums1, nums2, nums3))  # Expected output: [1]

    # Test case 5
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    nums3 = [7, 8, 9]
    print(solution.twoOutOfThree(nums1, nums2, nums3))  # Expected output: []

test_two_out_of_three()
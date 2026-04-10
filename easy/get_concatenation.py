from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums]

def test_get_concatenation():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 1]
    print(solution.getConcatenation(nums1))  # Expected output: [1, 2, 1, 1, 2, 1]

    # Test case 2
    nums2 = [1, 3, 2]
    print(solution.getConcatenation(nums2))  # Expected output: [1, 3, 2, 1, 3, 2]

    # Test case 3
    nums3 = [0]
    print(solution.getConcatenation(nums3))  # Expected output: [0, 0]

    # Test case 4
    nums4 = [5, -5]
    print(solution.getConcatenation(nums4))  # Expected output: [5, -5, 5, -5]

    # Test case 5
    nums5 = []
    print(solution.getConcatenation(nums5))  # Expected output: []

test_get_concatenation()
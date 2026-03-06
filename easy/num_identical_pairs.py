from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i < j and nums[i] == nums[j]:
                    res += 1

        return res

def test_num_identical_pairs():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 1, 1, 2]
    print(solution.numIdenticalPairs(nums1))  # Expected output: 4

    # Test case 2
    nums2 = [1, 1, 1, 1]
    print(solution.numIdenticalPairs(nums2))  # Expected output: 6

    # Test case 3
    nums3 = [1, 2, 3]
    print(solution.numIdenticalPairs(nums3))  # Expected output: 0

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    print(solution.numIdenticalPairs(nums4))  # Expected output: 0

    # Test case 5
    nums5 = [1, 1, 2, 2, 3, 3]
    print(solution.numIdenticalPairs(nums5))  # Expected output: 3

test_num_identical_pairs()
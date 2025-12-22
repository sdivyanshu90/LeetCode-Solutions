from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

def test_longest_ones():
    solution = Solution()

    # Test case 1
    nums1 = [1,1,1,0,0,0,1,1,1,1,0]
    k1 = 2
    print(solution.longestOnes(nums1, k1))  # Expected output: 6

    # Test case 2
    nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k2 = 3
    print(solution.longestOnes(nums2, k2))  # Expected output: 10

    # Test case 3
    nums3 = [1,1,1,1]
    k3 = 0
    print(solution.longestOnes(nums3, k3))  # Expected output: 4

    # Test case 4
    nums4 = [0,0,0]
    k4 = 2
    print(solution.longestOnes(nums4, k4))  # Expected output: 2

    # Test case 5
    nums5 = [1,0,1,0,1]
    k5 = 1
    print(solution.longestOnes(nums5, k5))  # Expected output: 3

test_longest_ones()
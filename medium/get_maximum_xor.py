from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        ans = [0] * len(nums)

        mask = (1 << maximumBit) - 1

        for i in range(len(nums)):
            current_xor = prefix_xor[len(prefix_xor) - 1 - i]
            ans[i] = current_xor ^ mask

        return ans

def test_get_maximum_xor():
    solution = Solution()

    # Test Case 1
    nums1 = [0,1,1,3]
    maximumBit1 = 2
    print(solution.getMaximumXor(nums1, maximumBit1))  # Expected Output: [0, 3, 2, 3]

    # Test Case 2
    nums2 = [2,3,4,7]
    maximumBit2 = 3
    print(solution.getMaximumXor(nums2, maximumBit2))  # Expected Output: [5, 2, 6, 5]

    # Test Case 3
    nums3 = [0,1,2,3,4]
    maximumBit3 = 3
    print(solution.getMaximumXor(nums3, maximumBit3))  # Expected Output: [3, 7, 4, 6, 7]

    # Test Case 4
    nums4 = [5]
    maximumBit4 = 1
    print(solution.getMaximumXor(nums4, maximumBit4))  # Expected Output: [4]

    # Test Case 5
    nums5 = [0]
    maximumBit5 = 20
    print(solution.getMaximumXor(nums5, maximumBit5))  # Expected Output: [1048575]

test_get_maximum_xor()
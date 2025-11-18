from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        freq = Counter(nums)
        if len(freq) == 1:
            return 0

        res = 0
        for val, key in freq.items():
            if val - 1 in freq:
                res = max(res, key + freq[val - 1])

        return res

def test_find_LHS():
    s = Solution()

    # Test case 1
    nums1 = [1,3,2,2,5,2,3,7]
    print(s.findLHS(nums1)) # Expected output: 5

    # Test case 2
    nums2 = [1,2,3,4]
    print(s.findLHS(nums2)) # Expected output: 2

    # Test case 3
    nums3 = [1,1,1,1]
    print(s.findLHS(nums3)) # Expected output: 0

    # Test case 4
    nums4 = [1,2,2,1,2,3,3,4]
    print(s.findLHS(nums4)) # Expected output: 5

    # Test case 5
    nums5 = [4,6,5,3,3,1]
    print(s.findLHS(nums5)) # Expected output: 3

test_find_LHS()
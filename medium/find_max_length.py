from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len

def test_find_max_length():
    s = Solution()

    # Test case 1
    nums1 = [0, 1]
    print(s.findMaxLength(nums1)) # Expected output: 2

    # Test case 2
    nums2 = [0, 1, 0]
    print(s.findMaxLength(nums2)) # Expected output: 2

    # Test case 3
    nums3 = [0, 0, 1, 1]
    print(s.findMaxLength(nums3)) # Expected output: 4

    # Test case 4
    nums4 = [0, 0, 1, 0, 0, 0, 1, 1]
    print(s.findMaxLength(nums4)) # Expected output: 6

    # Test case 5
    nums5 = [1, 1, 1, 0, 0, 0, 1]
    print(s.findMaxLength(nums5)) # Expected output: 6

test_find_max_length()
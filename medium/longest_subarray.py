from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        n = len(nums)
        l = res = 0
        for r in range(n):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()

            min_q.append(nums[r])
            max_q.append(nums[r])
            
            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()

                l += 1
            res = max(res, r - l + 1)
        return res

def test_longest_subarray():
    solution = Solution()

    # Test case 1
    nums1 = [8,2,4,7]
    limit1 = 4
    print(solution.longestSubarray(nums1, limit1))  # Expected output: 2

    # Test case 2
    nums2 = [10,1,2,4,7,2]
    limit2 = 5
    print(solution.longestSubarray(nums2, limit2))  # Expected output: 4

    # Test case 3
    nums3 = [4,2,2,2,4,4,2,2]
    limit3 = 0
    print(solution.longestSubarray(nums3, limit3))  # Expected output: 3

    # Test case 4
    nums4 = [1]
    limit4 = 0
    print(solution.longestSubarray(nums4, limit4))  # Expected output: 1

    # Test case 5
    nums5 = [1,5]
    limit5 = 0
    print(solution.longestSubarray(nums5, limit5))  # Expected output: 1

test_longest_subarray()
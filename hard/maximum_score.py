from bisect import bisect_left
from math import inf
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def solve(nums, k):
            n = len(nums)
            left = [0] * k
            curr_min = inf
            for i in range(k - 1, -1, -1):
                curr_min = min(curr_min, nums[i])
                left[i] = curr_min

            right = []
            curr_min = inf
            for i in range(k, n):
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)

            ans = 0
            for j in range(len(right)):
                curr_min = right[j]
                i = bisect_left(left, curr_min)
                size = (k + j) - i + 1
                ans = max(ans, curr_min * size)
                
            return ans
        
        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))

def test_maximum_score():
    solution = Solution()

    # Test case 1
    nums1 = [1,4,3,7,4,5]
    k1 = 3
    print(solution.maximumScore(nums1, k1))  # Expected output: 15

    # Test case 2
    nums2 = [5,5,4,5,4,1,1,1]
    k2 = 0
    print(solution.maximumScore(nums2, k2))  # Expected output: 20

    # Test case 3
    nums3 = [100000] * 100000
    k3 = 50000
    print(solution.maximumScore(nums3, k3))  # Expected output: 10000000000

    # Test case 4
    nums4 = [1] * 100000
    k4 = 50000
    print(solution.maximumScore(nums4, k4))  # Expected output: 100000

    # Test case 5
    nums5 = [i for i in range(1, 100001)]
    k5 = 99999
    print(solution.maximumScore(nums5, k5))  # Expected output: 2500050000

test_maximum_score()
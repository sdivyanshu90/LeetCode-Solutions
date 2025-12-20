from collections import Counter
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = Counter()
        running_sum = 0
        res = 0
        for num in nums:
            running_sum += num
            if running_sum % k == 0: 
                res += 1
            res += counts[running_sum % k]
            counts[running_sum % k] += 1
        return res

def test_subarrays_div_by_k():
    solution = Solution()
    
    # Test case 1
    nums = [4,5,0,-2,-3,1]
    k = 5
    print(solution.subarraysDivByK(nums, k))  # Expected output: 7

    # Test case 2
    nums = [5]
    k = 9
    print(solution.subarraysDivByK(nums, k))  # Expected output: 0

    # Test case 3
    nums = [-1,2,9]
    k = 2
    print(solution.subarraysDivByK(nums, k))  # Expected output: 2

    # Test case 4
    nums = [7,-5,5]
    k = 5
    print(solution.subarraysDivByK(nums, k))  # Expected output: 3

    # Test case 5
    nums = [1,-1,1,-1]
    k = 1
    print(solution.subarraysDivByK(nums, k))  # Expected output: 10

test_subarrays_div_by_k()
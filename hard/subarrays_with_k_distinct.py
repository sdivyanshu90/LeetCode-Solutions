from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        distinct_count = defaultdict(int)

        total_count = 0
        left = 0
        right = 0
        curr_count = 0

        while right < len(nums):
            distinct_count[nums[right]] += 1

            if distinct_count[nums[right]] == 1:
                k -= 1

            if k < 0:
                distinct_count[nums[left]] -= 1
                if distinct_count[nums[left]] == 0:
                    k += 1
                left += 1
                curr_count = 0

            if k == 0:
                while distinct_count[nums[left]] > 1:
                    distinct_count[nums[left]] -= 1
                    left += 1
                    curr_count += 1
                total_count += (curr_count + 1)

            right += 1

        return total_count

def test_subarrays_with_k_distinct():
    solution = Solution()
    
    # Test case 1
    nums = [1,2,1,2,3]
    k = 2
    print(solution.subarraysWithKDistinct(nums, k))  # Expected output: 7

    # Test case 2
    nums = [1,2,1,3,4]
    k = 3
    print(solution.subarraysWithKDistinct(nums, k))  # Expected output: 3

    # Test case 3
    nums = [1,2,1,2,1]
    k = 2
    print(solution.subarraysWithKDistinct(nums, k))  # Expected output: 8

    # Test case 4
    nums = [1,2,3,4,5]
    k = 5
    print(solution.subarraysWithKDistinct(nums, k))  # Expected output: 1

    # Test case 5
    nums = [2,1,2,1,2]
    k = 2
    print(solution.subarraysWithKDistinct(nums, k))  # Expected output: 9

test_subarrays_with_k_distinct()